import sys
import numpy as np
import cv2
import pandas as pd

df = pd.read_csv(sys.argv[1] + 'duck_count.csv')

suma = 0

for index, row in df.iterrows():
    image_path = row['picture']

    actual_duck_count = row['ducks']
    print(sys.argv[1] + image_path)
    print(f'actual: {actual_duck_count}')

    img = cv2.cvtColor(cv2.imread(sys.argv[1] + image_path), cv2.COLOR_BGR2HSV)

    img = img[250:800, 180:800]


    # GPT
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([179, 30, 255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([35, 255, 255])

    lower_brown = np.array([10, 100, 20])
    upper_brown = np.array([20, 255, 200])

    mask_white = cv2.inRange(img, lower_white, upper_white)
    mask_yellow = cv2.inRange(img, lower_yellow, upper_yellow)
    mask_brown = cv2.inRange(img, lower_brown, upper_brown)

    combined_mask = cv2.bitwise_or(mask_white, cv2.bitwise_or(mask_yellow, mask_brown))
    #

    kernel_3x3_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
    kernel_5x5_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    dilate = cv2.dilate(combined_mask, kernel_5x5_rect, iterations=3)
    erode = cv2.erode(dilate, kernel_3x3_ellipse, iterations=1)
    dilate = cv2.dilate(erode, kernel_5x5_rect, iterations=3) 

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    contours_ducks = []

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 2100 and area < 13000:
            contours_ducks.append(contour)

    print('pred: %d' % len(contours_ducks))
    suma += abs(len(contours_ducks) - actual_duck_count)

mae = suma / df.shape[0]

print(mae)