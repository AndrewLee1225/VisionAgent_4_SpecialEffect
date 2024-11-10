# Special Effects on Images

## Project Overview

The **Special Effects on Images** project is a Python-based application that employs advanced non-photorealistic rendering (NPR) techniques to apply artistic effects to digital images. Utilizing OpenCV for image processing and PyQt5 for the graphical user interface (GUI), this project is designed to demonstrate the application of complex image manipulation methods in a user-friendly framework. The primary aim is to provide an interactive platform for exploring artistic transformations of images through computational methods.

## Features

- **Load Image**: Users can upload an image from their local storage to apply various effects.
- **Apply Special Effects**: The following image processing effects are available:
  - **Emboss Effect**: Generates a 3D-like texture by highlighting edge structures and simulating light shadows.
  - **Cartoon Effect**: Uses edge detection combined with bilateral filtering to convert the image into a cartoon-style illustration.
  - **Pencil Sketch**: Converts the image into a pencil sketch, available in both grayscale and color formats.
  - **Oil Painting Effect**: Applies an oil painting effect using a non-linear filter, producing a smooth, artistic representation.
- **Intensity Slider**: Allows for precise adjustment of the intensity of the selected effect, enabling tailored transformations.
- **Reset Image**: Resets the processed image to its original, unmodified state.
- **Save Processed Image**: Saves the modified image to the user's local storage with customizable file names and formats.
- **User-Friendly GUI**: A streamlined interface facilitates the easy navigation and application of various features without requiring prior knowledge of image processing.

## Installation

### Prerequisites

To run this application, ensure that the following software and libraries are installed:

- **Python 3.8 or higher**
- **OpenCV** (`opencv-python` and `opencv-contrib-python`): Provides fundamental image processing operations, including advanced NPR effects.
- **PyQt5**: Used to construct the graphical user interface, allowing for an interactive application experience.
- **NumPy**: Facilitates numerical computations, particularly matrix operations that are central to image processing.

### Installation Steps

1. **Clone the Repository**:

   Clone the project repository to your local machine by executing the following command:

   ```bash
   git clone <repository-url>
   cd special-effects-gui
   ```

2. **Install Dependencies**:

   Install the necessary dependencies using the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you may manually install the dependencies:

   ```bash
   pip install opencv-python opencv-contrib-python PyQt5 numpy
   ```

## Usage

To utilize the application and explore its capabilities, follow these instructions:

1. **Run the Application**:

   Start the application by executing the following command:
   
   ```bash
   python cva4.py
   ```

2. **Load an Image**:

   Click the **Load Image** button to open a file dialog, allowing you to select an image from your local storage.

3. **Select an Effect**:

   Use the dropdown combo box to select an effect you wish to apply to the image.

4. **Adjust Intensity**:

   Adjust the intensity of the selected effect using the intensity slider. The current intensity level is displayed above the slider, providing precise feedback for customization.

5. **Apply Effect**:

   Click the **Apply Effect** button to process the image with the selected effect and intensity.

6. **Reset Image**:

   If needed, click the **Reset Image** button to revert to the original, unaltered image.

7. **Save Processed Image**:

   To save the processed image, click the **Save Image** button. You will be prompted to specify the file name and destination.

8. **Quit the Application**:

   Click the **Quit** button to close the application.

## Project Structure

The project's structure is organized as follows:

```
.
├── special_effects_gui.py   # Main Python script for the GUI application
├── README.md                # Project documentation
├── requirements.txt         # List of dependencies
```

## Code Improvements

In this version of the application, several enhancements have been implemented to improve performance, usability, and overall robustness:

1. **Memory Management**: Optimized memory usage by displaying processed images in a single window, thereby minimizing memory footprint and preventing screen clutter caused by multiple image windows.

2. **Error Handling**: Incorporated comprehensive error handling to mitigate unexpected crashes. Warning messages now appear if no image is loaded or if an attempt is made to save an unavailable processed image.

3. **User Interface Enhancements**: Enhanced the user interface by utilizing `QVBoxLayout` for a cleaner layout, adding an intensity slider for better control, and repositioning buttons for a more logical and intuitive user flow.

4. **Reset Functionality**: Introduced a reset feature that allows users to revert back to the original loaded image without having to reload it, enhancing workflow efficiency.

5. **Intensity Control**: Added an intensity slider to provide users with granular control over the effects, thereby facilitating more personalized image modifications.

6. **Informative Labels and Feedback**: Added labels to display the current intensity level and provided interactive feedback, such as message boxes, for actions like saving images or handling invalid inputs.

## Future Improvements

- **Effect Stacking**: Introduce the capability to apply multiple effects sequentially, allowing for richer and more complex image transformations.
- **Additional Effects**: Expand the range of available effects by including blurring, sharpening, edge detection, and other image enhancement techniques.
- **Undo/Redo Functionality**: Add functionality to undo and redo edits, providing users with greater control and flexibility during the editing process.
- **Real-time Preview**: Implement a real-time preview feature to allow users to visualize effects before applying them, thereby improving usability and reducing trial-and-error.

## Dependencies

The following Python libraries are necessary to run the project:

- `opencv-python`: Offers fundamental image processing operations for manipulating images.
- **`opencv-contrib-python`**: Contains additional OpenCV modules required for specialized effects, such as pencil sketch and oil painting.
- **`PyQt5`**: Used for creating the graphical interface, which ensures the application is interactive and user-friendly.
- **`numpy`**: Assists in performing numerical operations required for various image processing tasks.

## License

This project is licensed under the MIT License. Refer to the LICENSE file in the repository for further information.

## Acknowledgements

- **OpenCV**: For providing extensive image processing tools that enable the application of sophisticated artistic effects.
- **PyQt5**: For offering the GUI framework that makes this application accessible and easy to use.

## Contact

For any questions or suggestions regarding this project, please contact **Andrew Lee** at **lyandrew1225@gmail.com**.
