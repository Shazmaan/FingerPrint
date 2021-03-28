# FingerPrint

DISCLAIMER: This project is still under development and will be updated as we move forward.

## Libraries used

1) OpenCV
2) Skimage
3) numpy
4) math
5) fingerprint_enhancer ([Utkarsh Deshmukh GitHub](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python) [pip](https://pypi.org/project/fingerprint-enhancer/#description)) 

## Getting started

Please make sure to do `pip install -r requirements.txt` to install all the required dependencies for the project to execute.

### Images Path

Make sure to store all UNENHANCED images in the directory `Unenhanced Images`. Enhanced Images will be stored in `Images` directory.

### Steps to get Enhanced Image

NOTE: Currently on jpg format is supported. Make sure the images stored in `Unenhanced Images` directory is in jpg format.

From your respective terminal run the command `python Enhance_image.py <image name>`. This should process your image and store it in the `Images` directory.