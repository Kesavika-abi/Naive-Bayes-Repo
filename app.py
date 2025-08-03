from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
model, vectorizer = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        description = request.form["description"]

        # Transform input
        description_vec = vectorizer.transform([description])

        # Prediction
        prediction = model.predict(description_vec)[0]

        return render_template("result.html", description=description, cuisine=prediction)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
