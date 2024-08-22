# import cv2
# import pandas as pd
# from ultralytics import YOLO
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# from Lane_Detection_Sliding_Windows.LaneDetection import frame
#
# # Load the model
# model = YOLO('my_coco.pt')
#
# # Process the data from the model
# results = model.predict(frame)
# detections = results[0].boxes.data
#
# # Extract relevant information for wrong-way detections
# wrong_way_detections = []
# for detection in detections:
#     x1, y1, x2, y2, conf, cls = detection
#     if cls == 'wrong_way':
#         wrong_way_detections.append((x1, y1, x2, y2, conf))
#
# # Visualization techniques
#
# ## Graphs
# # Plot detection accuracy, false positives, true negatives, etc.
# plt.figure(figsize=(8, 6))
# plt.plot(wrong_way_detections[:, 4], label='Wrong-Way Detections')
# plt.xlabel('Detection Index')
# plt.ylabel('Confidence Score')
# plt.title('Wrong-Way Detection Confidence')
# plt.title('Wrong-Way Detection Heatmap')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.savefig('wrong_way_detection_heatmap.png')