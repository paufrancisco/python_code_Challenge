import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Define User-Product Interaction Data
data = {
    'UserID': [1, 2, 3, 4, 5],
    'ProductA': [1, 0, 1, 0, 1],
    'ProductB': [0, 1, 1, 0, 1],
    'ProductC': [1, 1, 0, 1, 0],
    'ProductD': [0, 0, 1, 1, 0],
    'ProductE': [1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)
print("User-Product Interaction Data:")
print(df)

# Step 2: Create the User-Product Matrix
user_product_matrix = df.set_index('UserID').T
print("\nUser-Product Matrix:")
print(user_product_matrix)

# Step 3: Calculate User Similarity
user_similarity = cosine_similarity(user_product_matrix.T)
user_similarity_df = pd.DataFrame(user_similarity,
                                  index=user_product_matrix.columns,
                                  columns=user_product_matrix.columns)
print("\nUser Similarity Matrix:")
print(user_similarity_df)

# Step 4: Function to Recommend Products
def recommend_products(user_id, user_product_matrix, user_similarity_df):
    # Get the user's interaction data
    user_data = user_product_matrix[user_id]

    # Get similar users sorted by similarity
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)

    # Only keep the similarity scores for users who have rated at least one product
    similar_users = similar_users[similar_users.index.isin(user_product_matrix.columns)]

    # Compute weighted sum of interactions from similar users
    recommendations = user_product_matrix.dot(similar_users) / similar_users.sum()

    # Filter out products the user has already interacted with
    recommendations = recommendations[user_data == 0]

    # Sort recommendations by score (highest first)
    return recommendations.sort_values(ascending=False)

# Step 5: Get Recommendations for a Specific User
user_id = 1
recommendations = recommend_products(user_id, user_product_matrix, user_similarity_df)
print(f"\nRecommended Products for User {user_id}:")
print(recommendations)
