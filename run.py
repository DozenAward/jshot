#coding=utf-8
import cv2


from SimpleHRNet  import SimpleHRNet
from draw import draw
import numpy as np

model = SimpleHRNet(48, 17, "./pose_hrnet_w48_384x288.pth")
imagePath = "test2/yoga_jav.webp"
image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

joints = model.predict(image)
print(type(joints))
print(joints[0][0]) # mang 3 chieu: chieu 1 so nguoi, chieu 2: 18 vị trí của trên body của mỗi người
arr_define = np.array(['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear',
 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist',
  'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle'])

arr_draw = ['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear',
 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist',
  'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle']

# for x in joints[0]:
#   print(x)
drawImage = draw.getImageFromImagePath(imagePath,joints,arr_define,arr_draw)