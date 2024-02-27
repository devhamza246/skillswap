from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.models import User
from .serializers import MatchUserSerializer


class MatchUsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MatchUserSerializer

    def get_queryset(self):
        return None

    def get_matching_users(self, request, *args, **kwargs):
        current_user = request.user

        # Get all users except the current user
        users = User.objects.exclude(pk=current_user.pk)

        # Calculate a combined score for each user
        for user in users:
            # Calculate exact matches and partial matches as before
            exact_matches_count = user.skills.filter(
                pk__in=current_user.learning_interests.values_list("pk", flat=True)
            ).count()
            partial_matches_count = sum(
                1
                for interest in current_user.learning_interests.all()
                for skill in user.skills.all()
                if interest.name == skill.name or (interest.name and skill.name)
            )
            # Check if both users have city and country information
            if current_user.city and user.city and current_user.country == user.country:
                # Consider using a library like geopy for more advanced comparison
                # Alternatively, a simple string comparison can also work
                if current_user.city == user.city:
                    location_score = 1  # Highest similarity (same city)
                else:
                    location_score = 0.5  # Moderate similarity (same country)
            else:
                location_score = 0  # No location information or different countries

            # Calculate a weighted score based on matches and experience level
            # Here, you can adjust the weights according to your preference
            score = (
                (exact_matches_count * 2)
                + partial_matches_count
                + user.experience_level
                + location_score
            )

            # Add the user to the list with their score
            user.score = score

        # Order users by their score in descending order (highest score first)
        users = sorted(users, key=lambda u: u.score, reverse=True)
        serizlized_data = MatchUserSerializer(users, many=True).data
        return Response({"data": serizlized_data}, status=status.HTTP_200_OK)
