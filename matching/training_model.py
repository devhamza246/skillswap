from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def calculate_similarity(users):
    # Combine the skills and learning interests of each user into one string
    users['combined_features'] = users.apply(lambda row: ' '.join([str(row['skills']), str(row['learning_interests']), str(row['experience_level'])]), axis=1)

    # Create the CountVectorizer object
    count_matrix = CountVectorizer().fit_transform(users['combined_features'])

    # Compute the cosine similarity matrix
    cosine_sim = cosine_similarity(count_matrix)

    return cosine_sim

def match_users(user_id, cosine_sim, users):

    # Get the pairwise similarity scores of all users with the given user
    similarity_scores = list(enumerate(cosine_sim[user_id]))

    # Sort the users based on the similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar users
    similarity_scores = similarity_scores[1:11]

    # Get the user indices
    user_indices = [i[0] for i in similarity_scores]

    # Return the top 10 most similar users
    return users.iloc[user_indices]
