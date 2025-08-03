import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("menu.csv")

# Features & Target
X = df['Description']
y = df['Cuisine']

# Text vectorization
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model & vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained and saved as model.pkl")
