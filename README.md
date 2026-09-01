# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Streamlit. The application recommends similar movies based on movie metadata.

## 🔗 Live Demo

https://movie-recommender-khushi.streamlit.app/

## 🚀 Features

- Select a movie from the available list
- Get 5 similar movie recommendations
- Content-based recommendation system
- Interactive web interface using Streamlit

## ⚙️ How It Works

1. Movie metadata such as genres, keywords, cast, crew, and overview is processed.
2. The important features are combined into a single `tags` column.
3. TF-IDF Vectorization converts the textual data into numerical vectors.
4. Cosine Similarity calculates the similarity between movies.
5. The application recommends the top 5 most similar movies.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle

## 📁 Project Structure

```text
movie-recommender-system/
│
├── data/
│   ├── credits.csv
│   └── movies.csv
│
├── notebook/
│   └── movie_recommendation_system(content based).ipynb
│
├── app.py
├── movies_dict.pkl
├── similarity1.pkl
├── requirements.txt
└── README.md
```

## ▶️ How to Run Locally

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application:

```bash
streamlit run app.py
```

## 🔮 Future Improvements

- Add movie posters and additional movie details
- Integrate a movie API
- Add personalized recommendations
- Implement a hybrid recommendation system
