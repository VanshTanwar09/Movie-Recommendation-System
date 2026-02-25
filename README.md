# Movie Recommendation System

A simple movie recommendation system built with Streamlit and machine learning. It recommends movies based on content similarity using cosine similarity on movie overviews and genres.

## Features

- 📊 Choose the number of recommendations (1-10) with a slider
- 🎞️ Get similar movie recommendations with ratings and relevance scores
- 🌈 Colorful and clean UI with emojis
- Based on content-based filtering using movie overviews and genres

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie_recommender_system.git
   cd movie_recommender_system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the preprocessing script (if needed):
   ```bash
   python preprocess.py
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Files

- `app.py`: Main Streamlit application
- `preprocess.py`: Script to preprocess the data and create similarity matrix
- `dataset.csv`: Movie dataset (not included, you need to provide it)
- `movies_list.pkl`: Pickled movie data
- `similarity.pkl`: Pickled similarity matrix
- `requirements.txt`: Python dependencies

## Dataset

The system uses a dataset with columns: id, title, genre, original_language, overview, popularity, release_date, vote_average, vote_count.

Place your `dataset.csv` in the root directory and run `preprocess.py` to generate the pickles.
