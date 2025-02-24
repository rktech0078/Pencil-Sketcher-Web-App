import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Function to create pencil sketch
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return final_img

# Streamlit UI
st.set_page_config(page_title="Pencil Sketcher", layout="wide")  # Better layout

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f5f5f5;
        }
        .title {
            text-align: center;
            color: #4A90E2;
        }
        .stImage {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>🎨 Pencil Sketcher App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Convert your photos into realistic pencil sketches.</p>", unsafe_allow_html=True)

st.sidebar.header("Upload Your Image")
file_image = st.sidebar.file_uploader("Choose a file", type=['jpeg', 'jpg', 'png'])

if file_image is None:
    st.warning("⚠️ Please upload an image to continue.")
else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))

    col1, col2 = st.columns(2)  # Layout for side-by-side images
    with col1:
        st.write("### 🖼️ Original Image")
        st.image(input_img, use_container_width=True)

    with col2:
        st.write("### ✏️ Pencil Sketch")
        st.image(final_sketch, use_container_width=True)

st.markdown(
    "<p style='text-align:center;'>Made with ❤️ by Abdul Rafay Khan | <a href='https://github.com/rktech0078' target='_blank'>Source Code</a></p>",
    unsafe_allow_html=True
)
