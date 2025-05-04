Color Detection using Python, OpenCV, and Pandas
================================================

Overview:
---------
This project is a simple color detection tool built using Python. It allows the user to click on any part of an image and get the name of the color at that pixel along with its RGB values.

Requirements:
-------------
- Python 3.6+
- OpenCV
- NumPy
- Pandas

Install dependencies using pip:
> pip install opencv-python numpy pandas

Files Included:
---------------
- color_detection.py : Main script to run the application.
- colors.csv         : Dataset with 865 color names and RGB/hex values.
- colorpic.jpg       : Sample image to test color detection.

How to Run:
-----------
Use the command line to run the project. Provide the image path using the `-i` argument.

Example:
> python color_detection.py -i colorpic.jpg

Instructions:
-------------
- Double-click anywhere on the displayed image.
- The application will show the closest color name and its RGB values.
- Press 'Esc' to exit.

Credits:
--------
Project inspired by DataFlair Python.
