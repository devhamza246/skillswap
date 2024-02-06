# from django.contrib.auth import get_user_model
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from accounts.models import User
from accounts.models import Skill
from matching.models import TrainedModel
import joblib

TRAINED_MODEL_NAME = "CompatibilityModel"


def calculate_match_score(profile1, profile2):
    # Implement your matching logic here
    # Example: A simple sum of weighted scores for skills and learning interests
    skill_score = calculate_skill_score(profile1.skills, profile2.skills)
    interest_score = calculate_interest_score(
        profile1.learning_interests, profile2.learning_interests
    )

    # Assign weights (you can customize these)
    skill_weight = 0.7
    interest_weight = 0.3

    # Calculate overall match score
    match_score = skill_weight * skill_score + interest_weight * interest_score

    return match_score


def calculate_skill_score(skills1, skills2):
    # Implement logic to calculate skill score
    # Example: Count the common skills
    common_skills = set(skills1) & set(skills2)
    return len(common_skills)


def calculate_interest_score(interests1, interests2):
    # Implement logic to calculate interest score
    # Example: Count the common interests
    common_interests = set(interests1.split(",")) & set(interests2.split(","))
    return len(common_interests)


# User = get_user_model()


def make_compatibility_prediction(new_user_skill_list):
    # Assuming skills and user_profiles are Django model instances
    skills = Skill.objects.values("id", "name")
    user_profiles = User.objects.values("id", "experience_level")

    # Create a DataFrame for skills
    skills_data = pd.DataFrame.from_records(skills)
    skills_data.columns = ["skill_id", "skill_name"]

    # Create a DataFrame for user profiles
    user_profiles_data = pd.DataFrame.from_records(user_profiles)
    user_profiles_data.columns = ["user_id", "experience_level"]

    # Create a matrix where each row represents a user, and each column represents a skill
    user_skill_matrix = pd.DataFrame(
        0, index=user_profiles_data["user_id"], columns=skills_data["skill_id"]
    )

    # Update the matrix based on user skills
    for user_id, skill_id in User.skills.through.objects.values_list("id", "skill__id"):
        user_skill_matrix.at[user_id, skill_id] = 1

    # Check if the number of samples in X and y are consistent
    if len(user_skill_matrix.index) != len(user_profiles_data):
        raise ValueError("Number of samples in X and y are inconsistent")

    # Assuming user_skill_matrix is prepared
    # X: Features (skills), y: Target variable (experience_level)
    # X = user_skill_matrix.drop(columns=["user_id", "experience_level"])
    X = user_skill_matrix
    y = user_profiles_data["experience_level"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Check if the number of samples in X_train and y_train are consistent
    if len(X_train) != len(y_train):
        raise ValueError("Number of samples in X_train and y_train are inconsistent")

    # Check if a trained model exists in the database
    trained_model = TrainedModel.objects.filter(model_name=TRAINED_MODEL_NAME).first()

    if trained_model:
        # Load the trained model from the database
        model = joblib.loads(trained_model.model_parameters)
    else:
        # Create and train the model
        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        # Serialize the model parameters
        model_parameters = joblib.dumps(model)

        # Save the trained model to the database
        TrainedModel.objects.create(
            model_name=TRAINED_MODEL_NAME,
            model_parameters=model_parameters,
        )

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Now, you can use the trained model to predict compatibility scores for new users
    # Assuming new_user_skills is a binary array representing the skills of a new user
    new_user_skills = user_skill_matrix.loc[new_user_skill_list].values.reshape(1, -1)
    compatibility_scores = model.predict(new_user_skills)

    # Get a list of user IDs and their compatibility scores
    users_compatibility = list(zip(user_skill_matrix.index, compatibility_scores))
    return users_compatibility
