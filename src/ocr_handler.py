import pytesseract
from PIL import Image


class OCRHandler:
    """Initializes an OCRHandler instance with a tesseract command.

    This class handles OCR operations using pytesseract.

    Args:
        tesseract_cmd (str): The path to the tesseract command."""

    def __init__(self, tesseract_cmd: str) -> None:
        """Initiates the OCRHandler instance.

        Sets the tesseract command for the pytesseract library.

        Args:
            tesseract_cmd (str): The path to the tesseract command.
        Returns:
            None"""
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def perform_ocr(self, image_path: str) -> str:
        """Performs Optical Character Recognition (OCR) on an image.

        This function uses the pytesseract library to extract text from an image.

        Args:
            image_path (str): The path to the image file.

        Returns:
            str: The extracted text from the image.

        Raises:
            FileNotFoundError: If the image file does not exist."""
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
