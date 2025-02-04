import pytesseract
from PIL import Image


class OCRHandler:

    def __init__(self, tesseract_cmd):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def perform_ocr(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text


def main():
    ocr = OCRHandler("/usr/bin/tesseract")
    text = ocr.perform_ocr("balance_sheet.png")
    print(text)


if __name__ == "__main__":
    main()
