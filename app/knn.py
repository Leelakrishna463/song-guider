import pandas as pd

#TODO: Add file in app folder
df = pd.read_csv('../dataset.csv')

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pickle
import numpy as np

# Define a set of unique tags (genres) to filter the data
unique_tags = {
    'black metal', 'acoustic', 'psychedelic', 'thrash metal', 'House', 
    'heavy metal', 'funk', 'Hip-Hop', 'post-rock', 'female vocalists', 'pop', 
    'alternative', 'soul', 'industrial', 'punk rock', 'blues', 'jazz', 'rap', 
    'metalcore', 'chillout', 'hardcore', 'hard rock', 'Progressive rock', 
    'ambient', 'british', 'Progressive metal', 'hip hop', 'indie rock', 'german', 
    'experimental', 'folk', 'techno', 'punk', 'death metal', 'japanese', 
    'singer-songwriter', 'electronica', '80s', 'electronic', 'metal', 'rock', 
    'seen live', 'alternative rock', 'Classical', 'Soundtrack', 'instrumental', 
    '90s', 'classic rock', 'dance', 'indie'
}

# Assuming df is a pandas DataFrame containing your data
# Extract the unique genres from the DataFrame
unique_genres = set(df['track_genre'].to_list())

# Filter the DataFrame to include only rows with genres in unique_tags
filtered_df = df[df['track_genre'].isin(unique_tags)]

# Shuffle the filtered DataFrame
filtered_df = shuffle(filtered_df)

# Sample up to 50 rows per genre
sampled_df = filtered_df.groupby('track_genre').head(50)

# Plot a scatterplot of energy vs. valence, styled and colored by genre
sns.scatterplot(x=sampled_df['energy'], y=sampled_df['valence'], style=sampled_df['track_genre'], hue=sampled_df['track_genre'])
plt.show()

# Prepare data for training
X = sampled_df.drop('track_genre', axis=1)
Y = sampled_df['track_genre']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a K-Nearest Neighbors classifier with k=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Calculate and print the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Find the best k value using cross-validation
k_values = [i for i in range(1, 31)]
scores = []

# Scale the entire dataset
X_scaled = scaler.fit_transform(X)

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn, X_scaled, Y, cv=5)
    scores.append(np.mean(score))

# Plot accuracy scores for different k values
sns.lineplot(x=k_values, y=scores, marker='o')
plt.xlabel("K Values")
plt.ylabel("Accuracy Score")
plt.show()

# Get the best k value
best_index = np.argmax(scores)
best_k = k_values[best_index]
print(f"Best k: {best_k}")

# Train the final model with the best k value
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)

# Make predictions with the final model
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

print(f"Final Model Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

# Save the model and scaler to disk
with open('knn_model.pkl', 'wb+') as model_file:
    pickle.dump(knn, model_file)

with open('scaler.pkl', 'wb+') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Load the model and scaler from disk
with open('knn_model.pkl', 'rb') as model_file:
    loaded_knn = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)

# Make predictions on new data
X_new_data = sampled_df[:1].drop('track_genre', axis=1)
X_new_scaled = loaded_scaler.transform(X_new_data)
predictions = loaded_knn.predict(X_new_scaled)
print(f"Predictions for new data: {predictions}")