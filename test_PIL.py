from PIL import Image, ImageEnhance

image = Image.open("files/sun.jpg")
enhancer = ImageEnhance.Contrast(image)
enhanced_image = enhancer.enhance(1.5)  # Increase contrast

enhanced_image.save('files/PIL_sun_output.png')

enhanced_image.show()
