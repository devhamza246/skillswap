from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from matching.models import Match
from matching.training_model import calculate_similarity, match_users
from matching.utils import make_compatibility_prediction
import pandas as pd


@receiver(post_save, sender=User)
def user_profile_updated(sender, instance, **kwargs):
    # Get all User objects
    users = User.objects.all()

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
    matched_users = match_users(instance.id, cosine_sim, df)
    
    # skills = instance.skills.values_list("id", flat=True)
    # if skills:
    #     new_user_skill_list = list(skills)
    #     # Make compatibility prediction using the utility function
    #     compatibility_score = make_compatibility_prediction(new_user_skill_list)
    #     if compatibility_score:
    #         print(compatibility_score)
    #         # Save the compatibility score to the database
    #         try:
    #             Match.objects.create(
    #                 user1=instance, user2=instance, compatibility_score=compatibility_score
    #             )
    #         except Exception as e:
    #             print(e)
