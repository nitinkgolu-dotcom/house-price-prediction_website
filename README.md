# House Price Prediction Website

A Flask website that uses a Linear Regression model trained on `Housing.csv` to estimate house prices from five area/property features.

## Project structure

```text
house_price_prediction_website/
├── app.py
├── Housing.csv              # Add your dataset here (not included in this ZIP)
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally (Windows / VS Code)

1. Install Python.
2. Put your original `Housing.csv` file in the same folder as `app.py`.
3. Open this project folder in VS Code.
4. Open Terminal and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

5. Open the local address shown in the terminal (usually http://127.0.0.1:5000).

If PowerShell blocks activation, run this once in the terminal and then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Dataset columns

The CSV must contain these columns exactly:

- `Avg. Area Income`
- `Avg. Area House Age`
- `Avg. Area Number of Rooms`
- `Avg. Area Number of Bedrooms`
- `Area Population`
- `Price`

The `Address` column is optional; the app removes it if present.

## Upload to GitHub

1. Create a new repository on GitHub, for example `house-price-prediction-website`.
2. Choose Public or Private. Do not initialize it with a README if you plan to push this folder as-is.
3. In VS Code, open the project folder.
4. Open Terminal and run:

```powershell
git init
git add .
git commit -m "Initial house price prediction website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/house-price-prediction-website.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. GitHub may ask you to sign in in a browser.

If `git` is not recognized, install Git for Windows from https://git-scm.com/download/win, restart VS Code, and check:

```powershell
git --version
```

Then run the Git commands above.

## Important

- `Housing.csv` is not included in this ZIP because it was not attached to the chat. Copy your dataset into this folder before running the website.
- If you want the website to work for other people after they clone the GitHub repository, include the dataset only if you have permission to share it. Otherwise document how to obtain it.
- This project is a local Flask app. Uploading the source code to GitHub does not by itself publish a live website. Deployment requires a hosting service that supports Python/Flask.
