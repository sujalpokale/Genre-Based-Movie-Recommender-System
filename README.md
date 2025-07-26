# 🎬 Genre-Based Movie Recommender System

This is a simple and effective **content-based movie recommender** system that suggests movies based on genres like *Action*, *Comedy*, *Horror*, etc. Built using Python and Streamlit for easy interaction.

---

## 🎯 Objective

To build a basic movie recommendation system that recommends the **top 5 movies** based on a user-selected genre using content-based filtering.

---

## 🛠️ Tech Stack

| Component     | Description                             |
|---------------|-----------------------------------------|
| Python        | Programming language                    |
| Pandas        | Data manipulation                       |
| Scikit-learn  | Feature extraction (CountVectorizer)    |
| Streamlit     | Lightweight web interface for UI        |
| MovieLens     | Public movie dataset                    |

---

## 📂 Dataset Used

- **MovieLens Latest Small Dataset (ml-latest-small)**
- 📥 [Download Link](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip)
- Contains:
  - `movies.csv` — `movieId`, `title`, `genres`

---

## 📊 Features Used

- **Genres** are treated as textual data
- Vectorized using **CountVectorizer**
- Recommendations based on genre frequency match

---

## 💡 How It Works

1. User enters a **movie genre** (e.g., "Comedy", "Horror", "Action")
2. The system vectorizes genre data using **bag-of-words**
3. Returns the **top 5 movies** matching the selected genre

---

## 📸 Sample UI (Streamlit)
![image_alt](https://github.com/sujalpokale/Genre-Based-Movie-Recommender-System/blob/ee0c4ab3b6e5a6d43314f7473fdc789ff547161b/Screenshot%202025-07-26%20210727.png)

