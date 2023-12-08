import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import joblib

# Load the pre-trained model and label encoder
model = load_model('CNN_model.h5')
label_encoder = joblib.load('label_encoder.pkl')

# Streamlit app
def main():
    st.title("Rice Variety Prediction App")

    # Navigation bar
    menu = ["Home", "About", "Contact"]
    choice = st.sidebar.selectbox("Navigation", menu)

    # Display different sections based on the choice
    if choice == "Home":
        st.header("Home Section")
        st.write("Welcome to the Rice Variety Prediction App! Upload an image to get started.")

        # Image upload and prediction
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
            img = image.load_img(uploaded_file, target_size=(50, 50))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions)
            predicted_class_name = label_encoder.classes_[predicted_class]
            classes_mapping = {1: "Basmati", 2: "Arborio or lpsala", 3: "Jasmine", 4: "Karacadag"}
            st.write(f"Predicted Class: {classes_mapping[predicted_class_name]}")

    elif choice == "About":
        st.header("About Section")
        st.write("This app predicts the variety of rice based on the uploaded image. "
                 "It uses a deep learning model trained on different rice varieties.")

    elif choice == "Contact":
        st.header("Contact Section")
        st.write("For inquiries, please contact us at contact@ricevarietyapp.com.")

        # Apply background color to the title section
        st.markdown(
            """
            <style>
                .title h1 {
                    background-color: #3498db;  /* Light Blue background for title */
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                }
            </style>
            """
        )

        # Add some extra styling with an attractive background color
        st.markdown(
            """
            <style>
                body {
                    background-color: #3498db;  /* Light Blue background */
                }
                .sidebar .sidebar-content {
                    background-color: #0000FF;  /* Dark Blue sidebar */
                    color: white;
                }
                .css-1v3fvcr {
                    background-color: #0000FF;  /* Light Blue button */
                    color: white;
                }
            </style>
            """
        )

if __name__ == "__main__":
    main()
