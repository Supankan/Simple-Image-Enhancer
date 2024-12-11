from PIL import Image, ImageEnhance
import streamlit as st

st.title("Simple Image Enhancer with Pillow")

# Get the image input from user.
image_input = st.file_uploader("Upload your image here.", type=['jpg', 'png', 'jpeg'])


# Function to get the input image details.
# Returns a dictionary with the values of each detail.
def get_image_details(image):
    result_dict = {}
    img_bri = ImageEnhance.Brightness(image)
    img_col = ImageEnhance.Color(image)
    img_con = ImageEnhance.Contrast(image)
    img_sha = ImageEnhance.Sharpness(image)

    result_dict['brightness'] = img_bri
    result_dict['color'] = img_col
    result_dict['contrast'] = img_con
    result_dict['sharpness'] = img_sha

    return result_dict


def enhance_image(image, bri, col, con, sha):
    input_details = get_image_details(image)
    new = input_details['brightness'].enhance(bri)
    new = ImageEnhance.Color(new).enhance(col)
    new = ImageEnhance.Contrast(new).enhance(con)
    new_img_final = ImageEnhance.Sharpness(new).enhance(sha)

    return new_img_final


# Get the desired values for each detail from the user.
new_bri = st.slider("Adjust Brightness: ", 0.0, 1.0, 0.5, 0.1)
new_col = st.slider("Adjust Color: ", 0.0, 1.0, 0.5, 0.1)
new_con = st.slider("Adjust Contrast: ", 0.0, 1.0, 0.5, 0.1)
new_sha = st.slider("Adjust Sharpness: ", 0.0, 1.0, 0.5, 0.1)

if image_input is not None:
    try:
        image = Image.open(image_input)
        with st.expander("Uploaded Image: ", expanded=False):
            st.image(image, 'Uploaded image', use_column_width=True)

        new_img = enhance_image(image, new_bri, new_col, new_con, new_sha)

        with st.expander("Enhanced Image: ", expanded=True):
            st.image(new_img, 'Enhanced Image', use_column_width=True)

    except Exception as e:
        st.error(f"An Error Occurred: {e}")

