import streamlit as st
from PIL import Image, ImageEnhance

# App title
st.title("Image Enhancer")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open image with PIL
    image = Image.open(uploaded_file)

    # Display original image
    st.subheader("Original Image")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Sliders for adjustments
    st.subheader("Enhancement Settings")
    brightness = st.slider("Brightness", 0.0, 2.0, 1.0, 0.1)
    contrast = st.slider("Contrast", 0.0, 2.0, 1.0, 0.1)
    color = st.slider("Color", 0.0, 2.0, 1.0, 0.1)
    sharpness = st.slider("Sharpness", 0.0, 2.0, 1.0, 0.1)

    # Apply enhancements
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(color)

    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sharpness)

    # Display enhanced image
    st.subheader("Enhanced Image")
    st.image(image, caption="Enhanced Image", use_column_width=True)

    # Option to download the enhanced image
    st.subheader("Download Enhanced Image")
    output = st.button("Download")
    if output:
        image.save("enhanced_image.png")
        with open("enhanced_image.png", "rb") as file:
            st.download_button(label="Download Enhanced Image", data=file, file_name="enhanced_image.png", mime="image/png")