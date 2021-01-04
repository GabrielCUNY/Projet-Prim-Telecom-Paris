import cv2
import sys
print(cv2.__version__)
vidcap = cv2.VideoCapture(str(sys.argv[1]))
success,image = vidcap.read()
success = True
for i in range(int(sys.argv[2])):
  cv2.imwrite("data/video/img1/frame%d.jpg" % i, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
