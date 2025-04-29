# 🐦 Tweet Sentiment Classifier

This project is a Flask-based web application that allows users to enter a tweet and classify its sentiment using a pretrained machine learning model. The model predicts whether the tweet expresses a **Positive**, **Negative**, or **Neutral** sentiment and shows the **confidence score**.

---

## 🚀 Features

- Web interface built with Flask
- Confidence score for predictions
- Beautiful, responsive UI with background image
- Sentiment result cleared on refresh for better UX

---

## 🖼️ Screenshot

![App Screenshot](https://github.com/ShrihariKasar/Twitter-Sentiment-Analysis/blob/main/templates/Screenshot%20(200).png)

---

## 🛠️ Tech Stack

- **Python** (Flask)
- **HTML/CSS** (Responsive design with background image)
- **Scikit-learn** (for model training and prediction)
- **Bootstrap** (for styling)
- **Joblib** (for saving/loading model/vectorizer)

---

## 📁 Project Structure

```
Tweet-Sentiment-Classifier/
│
├── static/
│   ├── background.jpg
│   └── style.css
│
├── templates/
│   └── index.html
│
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. User enters tweet in the form.
2. Flask receives the input and passes it to the pretrained ML model.
3. The model predicts the sentiment and returns:
   - Sentiment Label (Positive, Negative, Neutral)
   - Confidence Score (e.g., 97.32%)
4. Output is displayed in the same UI box.

---

## ▶️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Tweet-Sentiment-Classifier.git
cd Tweet-Sentiment-Classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
Flask
scikit-learn
joblib
```

---

## ✅ To-Do

- Add login system
- Save analyzed tweets to database
- Deploy on Heroku or Render

---

## 👨‍💻 Developers

- **Shrihari Kasar**
- **Utkarsha Kakulte**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
