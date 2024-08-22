import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import *
import cvzone
import numpy as np

harcascade = "model/haarcascade_russian_plate_number.xml"


model = YOLO('yolov8s.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('video_sample.mp4')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
# print(class_list)

count = 0
tracker = Tracker()
area1=[(1919,459),(935,477),(822,555),(1915,619)]
area2=[(496,757),(280,877),(1813,1055),(1850,914)]
wup = {}
wrongway = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue
    frame = cv2.resize(frame, (478,850))

    results = model.predict(frame)
    #   print(results)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    #    print(px)
    list = []

    # for index, row in px.iterrows():
    #     #        print(row)
    #
    #     x1 = int(row[0])
    #     y1 = int(row[1])
    #     x2 = int(row[2])
    #     y2 = int(row[3])
    #     d = int(row[5])
    #     c = class_list[d]
    #     if 'car' in c:
    #         list.append([x1, y1, x2, y2])
    bbox_idx = tracker.update(list)
    for bbox in bbox_idx:
        x3, y3, x4, y4, id = bbox
        cx = x3
        cy = y4
        cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)
        cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 1)
        cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 0, 255), 2)

    cap.set(3, 640)  # width
    cap.set(4, 480)  # height

    min_area = 500
    count = 0

    while True:
        success, img = cap.read()

        if not success:
            break  # Break the loop if there are no more frames to read

        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y + h, x:x + w]
                cv2.imshow("ROI", img_roi)

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("plates/scanned_img_" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1

    # cv2.polylines(frame, [np.array(area1, np.int32)], True, (255, 255, 255), 2)
    # cv2.polylines(frame, [np.array(area2, np.int32)], True, (255, 255, 255), 2)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
