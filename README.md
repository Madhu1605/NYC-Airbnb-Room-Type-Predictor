# 🏠 NYC Airbnb Room Type Predictor

A Machine Learning project that predicts the room type of an Airbnb listing in New York City based on listing, location, pricing, review, and host-related information.

The project uses a **Scikit-learn Machine Learning pipeline**, **FastAPI** for the backend API, and **Streamlit** for the user interface.

---

## 🚀 Project Overview

The model predicts one of the following room types:

- Entire home/apt
- Private room
- Shared room

The user enters Airbnb listing details through the Streamlit interface. The data is sent to the FastAPI backend, which loads the trained Machine Learning pipeline and returns the prediction along with prediction probabilities.

### Project Flow

```text
User
  ↓
Streamlit UI
  ↓
FastAPI API
  ↓
Preprocessing Pipeline
  ↓
Random Forest Classifier
  ↓
Room Type Prediction
  ↓
Probability