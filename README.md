Color Detection using Python, OpenCV, Pandas, and AI (KNN)
============================================================

Overview:
This project is a color detection tool enhanced with machine learning (AI). It allows users to click on any part of an image and get the predicted color name and its RGB values using a trained K-Nearest Neighbors (KNN) model, rather than relying on manual color matching.

Requirements:
Python 3.6+

OpenCV

NumPy

Pandas

scikit-learn

Install dependencies using pip:
bash
Copy code
pip install opencv-python numpy pandas scikit-learn
Files Included:
color_detection.py : Main script with AI-powered color name prediction.

colors.csv : Dataset with 865 color names and their RGB/hex values.

colorpic.jpg : Sample image to test color detection.

How to Run:
Use the command line to run the project. Provide the image path using the -i argument.

bash
Copy code
python color_detection.py -i colorpic.jpg
Instructions:
Double-click anywhere on the displayed image.

The application will:

Detect the RGB value of the clicked pixel.

Predict the closest color name using a trained KNN model.

Display the color name and RGB values as an overlay on the image.

What's New (AI Integration):
Replaced manual distance-based color name matching with a K-Nearest Neighbors classifier trained on the colors.csv dataset.

Improved accuracy and scalability.

Future-ready for further ML enhancements (e.g., clustering, contextual color recognition).
- Press 'Esc' to exit.

Credits:
--------
Project inspired by DataFlair Python.
