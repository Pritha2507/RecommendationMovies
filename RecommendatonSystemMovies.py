import pandas as pd
from scipy.spatial.distance import pdist, squareform

# Load data
file_path = '/Users/admin/Desktop/RecommendationMovies/u.data'  # Adjust file path as per your data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
data = pd.read_csv(file_path, sep='\t', names=column_names, engine='python')

# Create a user-item matrix
user_item_matrix = data.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)

# Calculate cosine similarity matrix for users
distance_matrix = pdist(user_item_matrix, metric='cosine')
similarity_matrix = 1 - squareform(distance_matrix)
similarity_df = pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get recommendations for a specific user
def get_recommendations(user_id, num_recommendations=10):
    # Get similarity scores for the user and sort them
    similar_users = similarity_df[user_id].sort_values(ascending=False)

    # Get items rated by similar users
    recommendations = pd.Series(dtype="float64")
    for similar_user, similarity_score in similar_users.items():
        if similar_user == user_id:
            continue
        user_ratings = user_item_matrix.loc[similar_user]
        recommendations = recommendations.add(user_ratings * similarity_score, fill_value=0)
    
    # Filter out items already rated by the user
    already_rated = user_item_matrix.loc[user_id][user_item_matrix.loc[user_id] > 0].index
    recommendations = recommendations.drop(already_rated)
    
    # Get the top N recommendations
    top_recommendations = recommendations.nlargest(num_recommendations)
    
    return top_recommendations

# Example usage
user_id = 2  # Change to desired user ID
num_recommendations = 10  # Change to desired number of recommendations
print(f"Recommendations for user {user_id}:")
recommendations = get_recommendations(user_id, num_recommendations)
for item_id, score in recommendations.items():
    print(f"Item ID: {item_id}, Score: {score}")
