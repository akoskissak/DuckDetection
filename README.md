# Duck Detection Script

This Python script processes images to detect and count ducks based on color filtering and contour detection. It uses a CSV file containing image paths and actual duck counts, then compares the detected duck count to the actual count, providing a mean absolute error (MAE) for accuracy assessment.

## Features

- Reads duck image paths and actual counts from a CSV file.
- Processes images to identify duck-like objects using HSV color thresholds for white, yellow, and brown hues.
- Detects contours within specified color ranges and size constraints to count likely ducks.
- Calculates and outputs the mean absolute error (MAE) between actual and detected counts to assess the detection accuracy.

## Requirements

- **Python 3.12**
- **Libraries**:
  - `numpy`
  - `opencv-python` (cv2)
  - `pandas`

Install the required libraries using:
```bash
pip install numpy opencv-python pandas
```
## Usage

Prepare the CSV file: Ensure your CSV file is named duck_count.csv and includes:
- picture: Relative paths to each duck image.
- ducks: The actual number of ducks in each image.

Run the Script:
```bash
python duck_detection.py <path_to_images>
```
- Replace `<path_to_images>` with the directory path containing your images. The script expects images to be located in the directory specified by this path, relative to each picture entry in the CSV.
Output:
- For each image, the script will print:
    - The image path
    - Actual duck count
    - Detected duck count (using contours)
- Finally, it will print the Mean Absolute Error (MAE), which reflects the accuracy of the detection.
## How it Works
Color Thresholding:
- Applies color masks to detect colors typically associated with ducks: white, yellow, and brown.
  
Contour Detection:
- Filters contours based on area to match likely duck sizes, then counts those contours.
  
Error Calculation:
- Compares the detected count to the actual count and calculates the MAE for accuracy assessment.

## Notes
-  The script currently crops each image to a specific region (`img[250:800, 180:800]`) to focus on the likely duck-containing area. Adjust these coordinates as needed.
- The color ranges and contour area thresholds are adjustable to improve detection based on your specific images.
