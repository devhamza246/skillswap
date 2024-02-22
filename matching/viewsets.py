from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.models import User
from .serializers import MatchUserSerializer
from matching.training_model import calculate_similarity, match_users
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


class MatchUsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MatchUserSerializer

    def get_queryset(self):
        return None

    def get_matching_users(self, request, *args, **kwargs):
        # users = super().get_queryset()
        # Create a list of dictionaries, each containing the data of a user
        # data = []
        # for user in users:
        #     if user.skills and user.learning_interests and user.experience_level:
        #         data.append(
        #             {
        #                 "id": user.id,
        #                 "skills": " ".join([skill.name for skill in user.skills.all()]),
        #                 "learning_interests": user.learning_interests,
        #                 "experience_level": user.experience_level,
        #             }
        #         )
        # if len(data) < 2:
        #     return Response(
        #         {"error": "No matching users found"}, status=status.HTTP_404_NOT_FOUND
        #     )
        # # Convert the list of dictionaries to a DataFrame
        # df = pd.DataFrame(data)
        # cosine_sim = calculate_similarity(df)
        # matched_users = match_users(request.user.id, cosine_sim, df)
        # # Get the IDs of the matched users
        # matched_user_ids = matched_users["id"].tolist()
        # # Get the User objects corresponding to these IDs
        # matched_user_objects = users.filter(id__in=matched_user_ids).exclude(
        #     id=request.user.id
        # )
        # # Sort the User objects based on the order of matched_user_ids
        # matched_user_objects = sorted(
        #     matched_user_objects, key=lambda user: matched_user_ids.index(user.id)
        # )

        # # Separate matched users with high priority from the remaining users
        # high_priority_users = []
        # remaining_users = []

        # for user in matched_user_objects:
        #     if user.id in matched_user_ids:
        #         high_priority_users.append(user)
        #     else:
        #         remaining_users.append(user)

        # serializer = MatchUserSerializer(
        #     high_priority_users + remaining_users, many=True
        # )
        current_user = request.user
        vectorizer = CountVectorizer()
        current_user_skills = list(current_user.skills.values_list("name", flat=True))
        current_user_learning_interests = current_user.learning_interests.split(",")
        current_user_location = (
            current_user.city,
            current_user.state,
            current_user.country,
        )
        current_user_experience_level = current_user.experience_level

        # Calculate scores for each user
        users = User.objects.exclude(id=current_user.id)
        scores = []
        for user in users:
            # Calculate scores for skills
            user_skills = list(user.skills.values_list("name", flat=True))
            skills_matrix = vectorizer.fit_transform(user_skills)
            current_user_skills_text = ",".join(current_user_skills)
            current_user_skills_vector = vectorizer.transform(
                [current_user_skills_text]
            )
            skills_score = cosine_similarity(current_user_skills_vector, skills_matrix)[
                0
            ][0]

            # Calculate scores for learning interests
            interests_score = len(
                set(current_user_learning_interests).intersection(
                    user.learning_interests.split(",")
                )
            ) / len(
                set(current_user_learning_interests).union(
                    user.learning_interests.split(",")
                )
            )

            # Calculate scores for location
            geolocator = Nominatim(user_agent="matching_users")
            location_query = f"{user.city}, {user.state}, {user.country}"
            location = geolocator.geocode(location_query)
            if location:
                user_location = (location.latitude, location.longitude)
                distance_km = geodesic(current_user_location, user_location).kilometers
                location_score = 1 / (1 + distance_km)
            else:
                location_score = 0

            # Calculate scores for experience level
            exp_score = (
                1 if current_user_experience_level == user.experience_level else 0
            )

            # Calculate overall score
            overall_score = (
                0.4 * skills_score
                + 0.3 * interests_score
                + 0.2 * location_score
                + 0.1 * exp_score
            )

            scores.append((user, overall_score))

        # Sort users based on scores
        sorted_users = sorted(scores, key=lambda x: x[1], reverse=True)
        serializer = MatchUserSerializer(sorted_users, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
