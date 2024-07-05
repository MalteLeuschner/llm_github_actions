import pytesseract
from PIL import Image


class OCRHandler:
    """:
    Initializes an OCRHandler instance with a tesseract command.

    The OCRHandler class is used to perform Optical Character Recognition (OCR) on images.
    It uses the pytesseract library to interact with the Tesseract OCR engine.

    Args:
        tesseract_cmd (str): The path to the Tesseract command-line tool.

    Raises:
        OSError: If the Tesseract command-line tool is not found at the specified path.
    """

    def __init__(self, tesseract_cmd: str) -> None:
        """Initiates the OCRHandler with the path to the Tesseract command.

        The OCRHandler class requires the path to the Tesseract command to function correctly.

        Args:
            tesseract_cmd (str): The path to the Tesseract command.

        Returns:
            None"""
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def perform_ocr(self, image_path: str) -> str:
        """Performs Optical Character Recognition (OCR) on an image.

        This function opens an image, reads the text in it using Tesseract OCR engine,
        and returns the extracted text.

        Args:
            image_path (str): The path to the image file.

        Returns:
            str: The extracted text from the image.

        Raises:
            IOError: If the image file cannot be opened."""
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text


def main() -> None:
    """Main function.

    Runs the OCRHandler to extract text from an image.

    Args:
        None
    Returns:
        None
    Raises:
        None"""
    ocr = OCRHandler("/usr/bin/tesseract")
    text = ocr.perform_ocr("balance_sheet.png")
    print(text)


if __name__ == "__main__":
    main()
