
from PIL import Image
import pytesseract

image_path = 'text_img.png'
img = Image.open(image_path)
text = pytesseract.image_to_string(img)

print(text)