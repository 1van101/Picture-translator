from PIL import Image
from pytesseract import pytesseract
from googletrans import Translator

# you can download Tesseract here -> https://github.com/UB-Mannheim/tesseract/wiki
# make a path to the folder where Tesseract is installed
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# make a path to the folder with the photos
path_to_images_folder = r"C:\my_folder\test\\"

pytesseract.tesseract_cmd = path_to_tesseract

current_image = input("Please enter the name of the picture you want to translate "
                      "(add the extension of the file after the name): ")

# opening the image from the source path + name of the image
img = Image.open(path_to_images_folder + current_image)

# converts the image to result and saves it into res variable
res = pytesseract.image_to_string(img)

translator = Translator()

# translates the text into BG language. You can choose any language from here:
# https://github.com/1van101/My-projects/blob/main/picture_translator/supported_languages_from_google_translator.txt
translated_text = translator.translate(res, dest='bg')

print(f"Original text here:\n{res}")
print("\n")
print(f"Translated text here:\n{translated_text.text}")
