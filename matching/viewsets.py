from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.models import User
from .serializers import MatchUserSerializer
from matching.training_model import calculate_similarity, match_users
import pandas as pd


class MatchUsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MatchUserSerializer

    def get_queryset(self):
        return None

    def match_users(self, request, *args, **kwargs):
        users = super().get_queryset()
        if len(users) < 2:
            return Response(["No users found"], status=status.HTTP_404_NOT_FOUND)
        # Create a list of dictionaries, each containing the data of a user
        data = []
        for user in users:
            data.append(
                {
                    "id": user.id,
                    "skills": " ".join([skill.name for skill in user.skills.all()]),
                    "learning_interests": user.learning_interests,
                    "experience_level": user.experience_level,
                }
            )
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
        cosine_sim = calculate_similarity(df)
        matched_users = match_users(request.user.id, cosine_sim, df)
        # Get the IDs of the matched users
        matched_user_ids = matched_users["id"].tolist()
        # Get the User objects corresponding to these IDs
        matched_user_objects = users.filter(id__in=matched_user_ids).exclude(id=request.user.id)
        # Sort the User objects based on the order of matched_user_ids
        matched_user_objects = sorted(
            matched_user_objects, key=lambda user: matched_user_ids.index(user.id)
        )
        serializer = MatchUserSerializer(matched_user_objects, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
