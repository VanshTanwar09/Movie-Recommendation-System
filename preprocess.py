import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv('dataset.csv')

# Feature selection
movies = movies[['id', 'title', 'overview', 'genre', 'vote_average', 'release_date']]

# Strip whitespace
movies['title'] = movies['title'].str.strip()
movies['overview'] = movies['overview'].str.strip()
movies['genre'] = movies['genre'].str.strip()

# Create tags
movies['tags'] = movies['overview'] + movies['genre']

# Drop unnecessary columns
new_data = movies.drop(columns=['overview', 'genre'])

# Vectorize
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()

# Compute similarity
similarity = cosine_similarity(vector)

# Save pickles
pickle.dump(new_data, open('movies_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Preprocessing complete. Pickles saved.")
