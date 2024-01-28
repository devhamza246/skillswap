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
