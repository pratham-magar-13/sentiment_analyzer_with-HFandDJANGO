# Hugging Face Model Integration with Django UI

A lightweight, fully functional web application that demonstrates how to seamlessly integrate a Hugging Face machine learning model (Sentiment Analysis) into a Django backend with a clean, responsive user interface.

This project avoids common performance pitfalls by initializing the deep learning model **once** in memory when the Django server boots up, ensuring fast, real-time inference during user requests.

---

## 🚀 Features
- **Instant Inference:** Runs sentiment analysis on user-submitted text instantly.
- **Persistent Memory Loading:** The Hugging Face pipeline is loaded on startup, preventing server crashes or heavy processing delays per request.
- **Minimalist UI:** Clean, modern interface powered by Water.css.
- **Zero Configuration Setup:** Automatically downloads and caches open-source model weights locally from the public Hugging Face Hub (no account or API keys required).

---

## 📂 Project Structure

```text
hf_django/
│
├── hf_django/               # Project configuration folder
│   ├── __init__.py
│   ├── settings.py          # App registration & settings
│   ├── urls.py              # Root routing configuration
│   └── wsgi.py
│
├── classifier/              # Main application folder
│   ├── templates/
│   │   └── classifier/
│   │       └── index.html   # Main web UI template
│   ├── __init__.py
│   ├── apps.py              # Model lifecycle initialization
│   ├── views.py             # Inference handling logic
│   └── urls.py              # App-specific routing pathways
│
└── manage.py                # Django administrative utility
