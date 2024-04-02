#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import joblib
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


model_path = "email_phishing_detection.0.1.0.joblib"
vectorizer_path = "vectorizer.joblib"


def home(req: HttpRequest) -> HttpResponse:
    return render(req, "index.html")


def contact(req: HttpRequest) -> HttpResponse:
    return render(req, "contact.html")


def showform(req: HttpRequest) -> HttpResponse:
    return render(req, "form.html")


def getform(req: HttpRequest) -> HttpResponse:
    if req.method == "POST":
        text = req.POST["text"]
        res, words = classify(str(text))
        data = {"Prediction": "Prediction", "res": res, "words": words}
        return render(req, "prediction.html", data)


def classify(text: str) -> int:
    try:
        import numpy as np
        from warnings import filterwarnings

        filterwarnings("always")
        filterwarnings("ignore")

        vec_file = os.path.join(os.path.dirname(__file__), vectorizer_path)
        model_file = os.path.join(os.path.dirname(__file__), model_path)
        loaded_model = joblib.load(model_file)
        vectorizer = joblib.load(vec_file)
        model, _ = loaded_model

        transformed_text = vectorizer.transform([str(text)])
        prediction = model.predict(transformed_text)
        indices = transformed_text.indices

        words_used = np.array(vectorizer.get_feature_names_out())[indices].tolist()
        label = int(prediction)

    except ImportError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An exception error occurred: {e}")

    return label, words_used
