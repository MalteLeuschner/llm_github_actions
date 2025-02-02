import pytesseract
from PIL import Image


class OCRHandler:
    """
A handler for performing OCR using Tesseract.

Initializes with a Tesseract command and provides functionality to extract text from
images using OCR.

Args:
    tesseract_cmd (str): Path to the Tesseract executable.
"""

    def __init__(self, tesseract_cmd: str) ->None:
        """<think>
Okay, so I need to create a Google-style docstring for the __init__ method of the OCRHandler class. Let me think about how to approach this.

First, I remember that Google docstrings typically start with a one-line summary, followed by a more detailed explanation if needed. Then, they list the arguments, and any returns or raises sections if applicable.

Looking at the __init__ method, it's a constructor that takes tesseract_cmd as an argument. The purpose of this method is to initialize the OCRHandler instance by setting the Tesseract command path. So the one-line summary should reflect that.

Next, I should explain what tesseract_cmd is. It's the path to the Tesseract executable. So in the Args section, I'll list tesseract_cmd with its type, which is a string.

Since __init__ doesn't return anything, I don't need a Returns section. Also, are there any exceptions this method might raise? If tesseract_cmd is not a valid path, maybe it could raise an error, but the code doesn't explicitly do that. So perhaps I should include a Raises section for a ValueError if the path is invalid.

Putting it all together, the docstring should have the summary, followed by the Args, and then the Raises section. I need to make sure the types are correctly specified, using str instead of string, and any exceptions with their explanations.

I should also avoid any repetition of the function name or body in the docstring, as per the instructions. So I'll focus on clearly describing each part without being redundant.

Finally, I'll structure it according to Google's style, ensuring each section is properly formatted and concise.
</think>

    Initializes the OCRHandler with the Tesseract command path.

    Args:
        tesseract_cmd (str): Path to the Tesseract executable.

    Raises:
        ValueError: If tesseract_cmd is not a valid path."""
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def perform_ocr(self, image_path: str) ->str:
        """Performs OCR on an image file and returns the extracted text.

Uses Tesseract OCR to process the image and extract readable text.

Args:
    image_path (str): The path to the image file to perform OCR on.

Returns:
    str: The extracted text from the image.

Raises:
    FileNotFoundError: If the image file is not found.
"""
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text


def main():
    """Runs the OCR process on a balance sheet image and prints the extracted text.
    
    Initializes the OCR handler with the Tesseract command path, performs OCR on the
    specified image, and prints the resulting text.
    
    Returns:
        None
    """
    ocr = OCRHandler('/usr/bin/tesseract')
    text = ocr.perform_ocr('balance_sheet.png')
    print(text)


if __name__ == '__main__':
    main()
