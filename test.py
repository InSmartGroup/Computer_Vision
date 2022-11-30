import cv2
import streamlit as st
import numpy as np
import base64
from io import BytesIO
from PIL import Image

# Page title
st.title("OpenCV Deep Learning based Face Detection")

# Define user's choice
image_buffer = st.radio("Please select:", ["Upload an image", "Take a picture using webcam"])

placeholders = st.columns(2)  # display both input and output images

if image_buffer == 'Upload an image':

    image_input = st.file_uploader("Upload an image file", type=['JPG', 'JPEG', 'PNG'])

    if image_input is not None:

        # Convert the input image file to a raw bytes format
        raw_bytes = np.asarray(bytearray(image_input.read()), dtype=np.uint8)

        # Convert the raw bytes to a BGR image file
        image_input = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

        # Set a threshold slider
        st.slider('Set confidence threshold:', min_value=0.0, max_value=1.0, step=0.01, value=0.5)

        placeholders[0].header("Input image")
        placeholders[0].image(image_input, channels='BGR')

        image_output = cv2.cvtColor(image_input, cv2.COLOR_BGR2HSV)
        image_output[:, :, 2] = cv2.equalizeHist(image_output[:, :, 2])
        image_output = cv2.cvtColor(image_output, cv2.COLOR_HSV2BGR)

        placeholders[1].header("Output image")
        placeholders[1].image(image_output, channels='BGR')

elif image_buffer == 'Take a picture using webcam':

    image_input = st.camera_input("Take a picture")

    if image_input is not None:

        # Convert the input image file to a raw bytes format
        raw_bytes = np.asarray(bytearray(image_input.read()), dtype=np.uint8)

        # Convert the raw bytes to a BGR image file
        image_input = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

        # Set a threshold slider
        st.slider('Set confidence threshold:', min_value=0.0, max_value=1.0, step=0.01, value=0.5)

        placeholders[0].header("Input picture")
        placeholders[0].image(image_input, channels='BGR')

        image_output = cv2.cvtColor(image_input, cv2.COLOR_BGR2HSV)
        image_output[:, :, 2] = cv2.equalizeHist(image_output[:, :, 2])
        image_output = cv2.cvtColor(image_output, cv2.COLOR_HSV2BGR)

        placeholders[1].header('Output picture')
        placeholders[1].image(image_output, channels='BGR')
