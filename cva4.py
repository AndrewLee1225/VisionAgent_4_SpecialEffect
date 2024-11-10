import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QComboBox, QVBoxLayout, QWidget, QSlider, QMessageBox
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.original_img = None  # Original loaded image
        self.processed_img = None  # Processed image after applying effects

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Special Effects on Images')
        self.setGeometry(200, 200, 400, 300)

        # Create main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create buttons, labels, combo box, and slider
        self.pictureButton = QPushButton('Load Image')  # Button to load an image
        self.effectCombo = QComboBox()  # Combo box to select different effects
        self.effectCombo.addItems(['Emboss', 'Cartoon', 'Pencil Sketch (Gray)', 'Pencil Sketch (Color)', 'Oil Painting'])
        self.applyButton = QPushButton('Apply Effect')  # Button to apply the selected effect
        self.saveButton = QPushButton('Save Image')  # Button to save the processed image
        self.resetButton = QPushButton('Reset Image')  # Button to reset the image to the original
        self.quitButton = QPushButton('Quit')  # Button to quit the application
        self.intensitySlider = QSlider()  # Slider to adjust the intensity of the effect
        self.intensitySlider.setMinimum(1)
        self.intensitySlider.setMaximum(100)
        self.intensitySlider.setValue(50)
        self.intensitySlider.setOrientation(1)  # Horizontal slider
        self.label = QLabel('Intensity: 50')  # Label to show the current intensity value

        # Add widgets to layout
        self.layout.addWidget(self.pictureButton)
        self.layout.addWidget(self.effectCombo)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.intensitySlider)
        self.layout.addWidget(self.applyButton)
        self.layout.addWidget(self.saveButton)
        self.layout.addWidget(self.resetButton)
        self.layout.addWidget(self.quitButton)

        # Connect buttons to their respective functions
        self.pictureButton.clicked.connect(self.pictureOpenFunction)  # Load image button
        self.applyButton.clicked.connect(self.applyEffectFunction)  # Apply effect button
        self.saveButton.clicked.connect(self.saveFunction)  # Save image button
        self.resetButton.clicked.connect(self.resetFunction)  # Reset image button
        self.quitButton.clicked.connect(self.quitFunction)  # Quit application button
        self.intensitySlider.valueChanged.connect(self.updateLabel)  # Update intensity label when slider changes

    def pictureOpenFunction(self):
        # Open a file dialog to load an image
        fname, _ = QFileDialog.getOpenFileName(self, 'Open Image', './', "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if fname:
            self.original_img = cv.imread(fname)  # Read the selected image
            self.processed_img = self.original_img.copy()  # Create a copy for processing
            if self.original_img is not None:
                cv.imshow('Loaded Image', self.original_img)  # Display the loaded image
            else:
                QMessageBox.critical(self, "Error", "Failed to load image.")  # Show error message if loading fails

    def updateLabel(self):
        # Update the intensity label based on slider value
        intensity = self.intensitySlider.value()
        self.label.setText(f'Intensity: {intensity}')

    def applyEffectFunction(self):
        # Apply the selected effect to the loaded image
        if self.original_img is None:
            QMessageBox.warning(self, "Warning", "Please load an image first.")  # Warn if no image is loaded
            return

        effect = self.effectCombo.currentText()  # Get the selected effect from combo box
        intensity = self.intensitySlider.value()  # Get the intensity value from slider
        if effect == 'Emboss':
            self.applyEmbossEffect(intensity)  # Apply emboss effect
        elif effect == 'Cartoon':
            self.applyCartoonEffect(intensity)  # Apply cartoon effect
        elif effect == 'Pencil Sketch (Gray)':
            self.applyPencilSketchEffect(intensity, color=False)  # Apply gray pencil sketch effect
        elif effect == 'Pencil Sketch (Color)':
            self.applyPencilSketchEffect(intensity, color=True)  # Apply color pencil sketch effect
        elif effect == 'Oil Painting':
            self.applyOilPaintingEffect(intensity)  # Apply oil painting effect
        
        if self.processed_img is not None:
            cv.imshow('Processed Image', self.processed_img)  # Display the processed image

    def applyEmbossEffect(self, intensity):
        # Apply emboss effect to the image
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])  # Emboss filter kernel
        gray = cv.cvtColor(self.original_img, cv.COLOR_BGR2GRAY)  # Convert image to grayscale
        gray16 = np.int16(gray)  # Convert to 16-bit to prevent overflow
        self.processed_img = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + intensity, 0, 255))  # Apply filter and adjust intensity

    def applyCartoonEffect(self, intensity):
        # Apply cartoon effect to the image
        sigma_s = 60  # Spatial window size
        sigma_r = 0.01 * intensity  # Range filter parameter based on intensity
        self.processed_img = cv.stylization(self.original_img, sigma_s=sigma_s, sigma_r=sigma_r)  # Apply cartoon effect

    def applyPencilSketchEffect(self, intensity, color):
        # Apply pencil sketch effect to the image
        sigma_s = 60  # Spatial window size
        sigma_r = 0.01 * intensity  # Range filter parameter based on intensity
        if color:
            _, self.processed_img = cv.pencilSketch(self.original_img, sigma_s=sigma_s, sigma_r=sigma_r, shade_factor=0.02)  # Apply color sketch
        else:
            self.processed_img, _ = cv.pencilSketch(self.original_img, sigma_s=sigma_s, sigma_r=sigma_r, shade_factor=0.02)  # Apply gray sketch

    def applyOilPaintingEffect(self, intensity):
        # Apply oil painting effect to the image
        size = max(1, intensity // 10)  # Adjust size based on intensity
        self.processed_img = cv.xphoto.oilPainting(self.original_img, size, 1, cv.COLOR_BGR2Lab)  # Apply oil painting effect

    def resetFunction(self):
        # Reset the image to the original
        if self.original_img is not None:
            self.processed_img = self.original_img.copy()  # Copy the original image
            cv.imshow('Loaded Image', self.original_img)  # Display the original image

    def saveFunction(self):
        # Save the processed image to a file
        if self.processed_img is None:
            QMessageBox.warning(self, "Warning", "No processed image to save.")  # Warn if no processed image
            return

        fname, _ = QFileDialog.getSaveFileName(self, 'Save File', './', "Images (*.png *.jpg *.bmp)")
        if fname:
            cv.imwrite(fname, self.processed_img)  # Save the processed image
            QMessageBox.information(self, "Saved", f'Image saved to {fname}')  # Inform the user that the image has been saved

    def quitFunction(self):
        # Quit the application
        cv.destroyAllWindows()  # Close all OpenCV windows
        self.close()  # Close the application window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SpecialEffect()  # Create an instance of the main window
    win.show()  # Show the main window
    sys.exit(app.exec_())  # Execute the application
