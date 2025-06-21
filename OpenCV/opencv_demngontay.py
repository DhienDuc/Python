#Import library
import cv2
import time
import os
import hand as hd

#Capture video
capture = cv2.VideoCapture('Count1.mp4')
pTime = 0
detector = hd.handDetector()

#Read image
folderpath = "Fingers/edits"
list = os.listdir(folderpath)
list_image = []
for file in list:
    image = cv2.imread(f"{folderpath}/{file}")
    list_image.append(image)

#Display video, image
while True:
    ret, frame = capture.read()

    #Find hand
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)

    #Finger count
    fingerID = [4, 8, 12, 16, 20]
    if len(lmList) != 0:
        fingers = []

        #4 fingers
        for i in range(1, 5):
            if lmList[fingerID[i]][2] < lmList[fingerID[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #Thumb
        if lmList[fingerID[0]][1] < lmList[fingerID[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #Count fingers
        totalFingers = fingers.count(1)

        #Show image
        h, w, c = list_image[totalFingers].shape
        frame[:h, :w] = list_image[totalFingers]

    #Show fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, f'{int(fps)} fps', (870, 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 2)

    #Show video
    cv2.imshow('Capturing video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

#Release data
capture.release()
cv2.destroyAllWindows()
