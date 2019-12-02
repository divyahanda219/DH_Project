import numpy as np
import cv2, os

# read the video and extract info about it
video = "ch07_20190301140441.mp4"

cap = cv2.VideoCapture(video)
width, height, frate = int(cap.get(3)), int(cap.get(4)), int(cap.get(5))
folder, file = os.path.split(video)

# make the folder to save file

output = os.path.join("output", file[:-9])
if not os.path.exists(output):
	os.makedirs(output)


# get total number of frames
totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
x = [i for i in range (1, totalFrames) if divmod(i, int(frate*60))[1]==0]


print (x)
for myFrameNumber in x:
	cap.set(cv2.CAP_PROP_POS_FRAMES,myFrameNumber)
	while True:
		ret, frame = cap.read()
		out_name = os.path.join(output, (str(file[:-9])+"_"+str(myFrameNumber)+".png"))
		cv2.imwrite(out_name, frame)
		break

