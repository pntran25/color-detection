Color Detection using Python, OpenCV, Pandas, and AI (KNN)
==========================================================

Overview:
---------
This project is a color detection tool enhanced with a machine learning model (K-Nearest Neighbors). It allows the user to click on any part of an image and get the predicted name of the color at that pixel, along with its RGB values. The color name is determined using an AI-based classifier instead of a manual distance calculation.

Requirements:
-------------
- Python 3.6+
- OpenCV
- NumPy
- Pandas
- scikit-learn

Install dependencies using pip:
> pip install opencv-python numpy pandas scikit-learn

Files Included:
---------------
- color_detection.py : Main script with AI-powered color name prediction.
- colors.csv         : Dataset with 865 color names and RGB/hex values.
- colorpic.jpg       : Sample image to test color detection.

How to Run:
-----------
Use the command line to run the project. Provide the image path using the -i argument.

Example:
> python color_detection.py -i colorpic.jpg

Instructions:
-------------
- Double-click anywhere on the displayed image.
- The application will:
    - Detect the RGB value of the clicked pixel.
    - Predict the closest color name using a trained KNN model.
    - Display the color name and RGB values as an overlay.

What's New (AI Integration):
----------------------------
- Replaced manual color name matching with a K-Nearest Neighbors (KNN) classifier.
- KNN is trained on the colors.csv dataset to predict the closest color name based on RGB input.
- More scalable and accurate than traditional nearest-distance matching.

