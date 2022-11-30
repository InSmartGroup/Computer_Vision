import cv2
import streamlit as st
import numpy as np

st.title('Image Color Segmentation')

choice = st.selectbox('Upload an image file of take a picture using webcam', ['None', 'Upload an image', 'Take a picture'])
if choice == 'None':
    image_input = None
    pass
elif choice == 'Upload an image':
    image_input = st.file_uploader('Upload an image', type=['JPG', 'JPEG', 'PNG'])
elif choice == 'Take a picture':
    image_input = st.camera_input("Take a photo")

sliders = st.columns(4)

if image_input is not None:

    # Convert the input image to a raw byte array
    raw_bytes = np.asarray(bytearray(image_input.read()), dtype=np.uint8)

    # Convert a raw byte array to a BGR image
    image_output = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    # Convert a BGR image to HSV
    image_output = cv2.cvtColor(image_output, cv2.COLOR_BGR2HSV)

    # Create sliders for color segmentation
    hue_min = sliders[0].slider('Minimal hue:', min_value=0, max_value=180, step=1)
    hue_max = sliders[1].slider('Maximal hue:', min_value=0, max_value=180, step=1)
    saturation_min = sliders[2].slider('Minimal color saturation:', min_value=0, max_value=255, step=1, )
    value_min = sliders[3].slider('Minimal lightness:', min_value=0, max_value=255, step=1)

    # Define HSV color lower and upper boundaries
    lower_bound = np.array([hue_min, saturation_min, value_min])
    upper_bound = np.array([hue_max, 255, 255])

    # Define a mask
    mask = cv2.inRange(image_output, lower_bound, upper_bound)

    # Result
    result = cv2.bitwise_and(image_output, image_output, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

    st.image(result, channels='BGR')
