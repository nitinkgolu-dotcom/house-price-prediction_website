from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

app = Flask(__name__)

model = None
model_score = None
error_message = None

def train_model():
    global model, model_score, error_message
    try:
        df = pd.read_csv("Housing.csv")
        if "Address" in df.columns:
            df = df.drop("Address", axis=1)

        required = [
            "Avg. Area Income",
            "Avg. Area House Age",
            "Avg. Area Number of Rooms",
            "Avg. Area Number of Bedrooms",
            "Area Population",
            "Price",
        ]
        missing = [col for col in required if col not in df.columns]
        if missing:
            raise ValueError("Missing columns in Housing.csv: " + ", ".join(missing))

        df = df[required].dropna()
        X = df.drop("Price", axis=1)
        y = df["Price"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = LinearRegression()
        model.fit(X_train, y_train)
        model_score = r2_score(y_test, model.predict(X_test))
        error_message = None
    except Exception as exc:
        model = None
        model_score = None
        error_message = str(exc)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    form_values = {}
    error = error_message

    if request.method == "POST":
        try:
            form_values = {
                "income": request.form["income"],
                "house_age": request.form["house_age"],
                "rooms": request.form["rooms"],
                "bedrooms": request.form["bedrooms"],
                "population": request.form["population"],
            }
            if model is None:
                raise ValueError("The model is not ready. Check that Housing.csv is in the project folder.")
            values = [[
                float(form_values["income"]),
                float(form_values["house_age"]),
                float(form_values["rooms"]),
                float(form_values["bedrooms"]),
                float(form_values["population"]),
            ]]
            prediction = float(model.predict(values)[0])
        except Exception as exc:
            error = str(exc)

    return render_template(
        "index.html",
        prediction=prediction,
        form_values=form_values,
        model_score=model_score,
        error=error,
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
