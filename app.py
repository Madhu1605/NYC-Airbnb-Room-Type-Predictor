import streamlit as st
import requests


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NYC Stay Predictor",
    page_icon="🏠",
    layout="wide"
)

API_URL = "https://nyc-airbnb-room-type-predictor-wbmp.onrender.com/predict"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* =========================
       PAGE
    ========================= */

    .stApp {
        background: #080d18;
        color: #f5f7fb;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 45px;
        padding-bottom: 50px;
    }

    header {
        background: transparent !important;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* =========================
       HERO
    ========================= */

    .eyebrow {
        color: #67d8d0;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 52px;
        line-height: 1.05;
        font-weight: 800;
        color: #f7f8fc;
        max-width: 650px;
        margin-bottom: 18px;
    }

    .hero-text {
        color: #8e99ad;
        font-size: 16px;
        line-height: 1.65;
        max-width: 650px;
        margin-bottom: 42px;
    }


    /* =========================
       SECTION TITLES
       ========================= */

    .main-section {
        color: #f2f4f8;
        font-size: 22px;
        font-weight: 700;
        letter-spacing: 0.2px;
        margin-top: 10px;
        margin-bottom: 28px;
    }

    .sub-section {
        color: #66738a;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-top: 25px;
        margin-bottom: 12px;
    }


    /* =========================
       INPUT LABELS
       ========================= */

    label {
        color: #aeb8c8 !important;
        font-size: 12px !important;
    }


    /* =========================
       INPUT BOXES
       ========================= */

    div[data-baseweb="input"] {
        background: #0d1526;
        border: 1px solid #25334c;
        border-radius: 8px;
    }

    div[data-baseweb="select"] > div {
        background: #0d1526;
        border: 1px solid #25334c;
        border-radius: 8px;
    }

    input {
        color: #f5f7fb !important;
    }


    /* =========================
       BUTTON
       ========================= */

    .stButton > button {
        background: #f5b84b;
        color: #111827;
        border: none;
        border-radius: 8px;
        height: 50px;
        font-size: 14px;
        font-weight: 700;
        margin-top: 28px;
    }

    .stButton > button:hover {
        background: #ffc865;
        color: #111827;
    }


    /* =========================
       PREDICTION
       ========================= */

    .prediction-title {
        text-align: center;
        color: #66738a;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-top: 20px;
    }

    .prediction-name {
        text-align: center;
        color: #f6b94f;
        font-size: 36px;
        font-weight: 800;
        margin-top: 8px;
    }

    .prediction-confidence {
        text-align: center;
        color: #e8edf5;
        font-size: 22px;
        font-weight: 700;
        margin-top: 2px;
        margin-bottom: 35px;
    }


    /* =========================
       PROBABILITY
       ========================= */

    .probability-label {
        color: #aab4c5;
        font-size: 13px;
        margin-bottom: 5px;
    }

    .probability-value {
        float: right;
        color: #e7ebf2;
        font-weight: 600;
    }


    /* =========================
       RESULT INFO
       ========================= */

    .result-message {
        text-align: center;
        color: #77849a;
        font-size: 14px;
        margin-top: 25px;
        margin-bottom: 25px;
    }


    /* =========================
       DIVIDER
       ========================= */

    .divider {
        height: 1px;
        background: #1d293d;
        margin: 45px 0;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        color: #566277;
        font-size: 12px;
        margin-top: 45px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="eyebrow">NYC STAY</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-title">
        Find the room type<br>
        your listing belongs to
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-text">
        Predict whether an Airbnb listing is an entire home,
        private room, or shared room using machine learning.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LISTING INFORMATION
# =========================================================

st.markdown(
    '<div class="main-section">LISTING INFORMATION</div>',
    unsafe_allow_html=True
)


# =========================================================
# LOCATION
# =========================================================

st.markdown(
    '<div class="sub-section">LOCATION</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    latitude = st.number_input(
        "Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=40.7128,
        format="%.4f"
    )

with col2:

    longitude = st.number_input(
        "Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=-74.0060,
        format="%.4f"
    )


col1, col2 = st.columns(2)

with col1:

    neighbourhood_group = st.selectbox(
        "Borough",
        [
            "Brooklyn",
            "Manhattan",
            "Queens",
            "Bronx",
            "Staten Island"
        ]
    )

with col2:

    neighbourhood = st.text_input(
        "Neighbourhood",
        value="Williamsburg"
    )


# =========================================================
# PROPERTY
# =========================================================

st.markdown(
    '<div class="sub-section">PROPERTY</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    price = st.number_input(
        "Price per night (USD)",
        min_value=1.0,
        value=150.0,
        step=10.0
    )

with col2:

    minimum_nights = st.number_input(
        "Minimum nights",
        min_value=1,
        max_value=365,
        value=2,
        step=1
    )

with col3:

    availability_365 = st.number_input(
        "Days available",
        min_value=0,
        max_value=365,
        value=200,
        step=1
    )


# =========================================================
# REVIEWS & HOST
# =========================================================

st.markdown(
    '<div class="sub-section">REVIEWS & HOST</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    number_of_reviews = st.number_input(
        "Total reviews",
        min_value=0,
        value=50,
        step=1
    )

with col2:

    reviews_per_month = st.number_input(
        "Reviews per month",
        min_value=0.0,
        value=2.5,
        step=0.1
    )

with col3:

    calculated_host_listings_count = st.number_input(
        "Listings by this host",
        min_value=0,
        value=3,
        step=1
    )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.write("")

button_col1, button_col2, button_col3 = st.columns(
    [1, 1.4, 1]
)

with button_col2:

    predict = st.button(
        "✦  PREDICT ROOM TYPE",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-section" style="text-align:center;">'
    'PREDICTION'
    '</div>',
    unsafe_allow_html=True
)


if predict:

    if not neighbourhood.strip():

        st.warning("Please enter a neighbourhood.")

    else:

        data = {
            "latitude": latitude,
            "longitude": longitude,
            "price": price,
            "minimum_nights": minimum_nights,
            "number_of_reviews": number_of_reviews,
            "reviews_per_month": reviews_per_month,
            "calculated_host_listings_count":
                calculated_host_listings_count,
            "availability_365": availability_365,
            "neighbourhood_group":
                neighbourhood_group,
            "neighbourhood":
                neighbourhood
        }

        try:

            with st.spinner("Analyzing listing..."):

                response = requests.post(
                    API_URL,
                    json=data,
                    timeout=10
                )

            if response.status_code == 200:

                result = response.json()

                prediction = result[
                    "Predicted_room_type"
                ]

                probabilities = result[
                    "Probability"
                ]

                classes = [
                    "Entire home/apt",
                    "Private room",
                    "Shared room"
                ]

                # Find probability of predicted class
                prediction_index = classes.index(
                    prediction
                )

                confidence = (
                    probabilities[prediction_index] * 100
                )


                # -------------------------
                # Main prediction
                # -------------------------

                st.markdown(
                    '<div class="prediction-title">'
                    'MOST LIKELY'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="prediction-name">'
                    f'{prediction}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="prediction-confidence">'
                    f'{confidence:.1f}%'
                    f'</div>',
                    unsafe_allow_html=True
                )


                # -------------------------
                # Probability bars
                # -------------------------

                for room, probability in zip(
                    classes,
                    probabilities
                ):

                    percentage = probability * 100

                    st.markdown(
                        f"""
                        <div class="probability-label">
                            {room}
                            <span class="probability-value">
                                {percentage:.1f}%
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.progress(
                        float(probability)
                    )

                    st.write("")


            else:

                st.error(
                    f"FastAPI returned "
                    f"status code {response.status_code}"
                )


        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to FastAPI."
            )

            st.info(
                "Make sure FastAPI is running:\n\n"
                "`python -m uvicorn main:app --reload`"
            )


        except requests.exceptions.Timeout:

            st.error(
                "The prediction request timed out."
            )


else:

    st.markdown(
        """
        <div class="result-message">
            Enter the listing details above and click
            <b>Predict Room Type</b> to see the model's prediction.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        NYC Stay • Machine Learning • FastAPI • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)