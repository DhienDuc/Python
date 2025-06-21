import cv2 as cv
import numpy as np

# Read the images
big_img = cv.imread('Game asset/township.jpg', cv.IMREAD_REDUCED_COLOR_2)
search_img = cv.imread('Game asset/tree.jpg', cv.IMREAD_REDUCED_COLOR_2)

#Compare the images
result = cv.matchTemplate(big_img, search_img, cv.TM_CCOEFF_NORMED)

#Get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

#check if the best match is above a certain threshold
threshold = 0.5
if max_val >= threshold:
    print('Found the object')

    #Draw a rectangle around the best match
    h, w = search_img.shape[:2]
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(big_img, top_left, bottom_right, (255,255,255), 2)
    cv.imshow('Result', big_img)
else:
    print('Object not found')

cv.waitKey(0)