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
        """Initializes the OCRHandler instance.

        Sets the tesseract command for the pytesseract library.

        Args:
            tesseract_cmd (str): The path to the tesseract command.

        Returns:
            None"""
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def perform_ocr(self, image_path: str) -> str:
        """Performs Optical Character Recognition (OCR) on an image.

        This function opens an image using PIL, then uses pytesseract to extract text from the image.

        Args:
            image_path (str): The path to the image file.

        Returns:
            str: The extracted text.

        Raises:
            IOError: If the image file cannot be opened."""
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text


def main() -> None:
    """Main function.

    Runs the OCRHandler on a sample image.

    This function demonstrates the usage of the OCRHandler class by creating an instance
    and performing OCR on a sample image.

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
