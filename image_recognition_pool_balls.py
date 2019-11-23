# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the cue
# ball in the HSV color space
cueLower = (219, 219, 219)
cueUpper = (255, 255, 255)

# define the lower and upper boundaries of the 8-ball
# in the HSV color space
eightLower = (0, 0, 0)
eightUpper = (92, 92, 92)
 
# initialize the list of tracked points, the frame counter,
# and the coordinate deltas (FOR THE CUE BALL)
cuePts = deque(maxlen=args["buffer"])
cueCounter = 0
# (dXc, dYc) = (0, 0)

# initialize the list of tracked points, the frame counter,
# and the coordinate deltas
eightPts = deque(maxlen=args["buffer"])
eightCounter = 0
# (dXe, dYe) = (0, 0)

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()
 
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
 
# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	frame = vs.read()
 
	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "white" for the cue ball,
	# then perform a series of dilations and erosions to remove
	# any small blobs left in the mask
	cueMask = cv2.inRange(hsv, cueLower, cueUpper)
	cueMask = cv2.erode(cueMask, None, iterations=2)
	cueMask = cv2.dilate(cueMask, None, iterations=2)

        # construct a mask for the color "black" for the eight ball,
	# then perform a series of dilations and erosions to remove
	# any small blobs left in the mask
	eightMask = cv2.inRange(hsv, eightLower, eightUpper)
	eightMask = cv2.erode(eightMask, None, iterations=2)
	eightMask = cv2.dilate(eightMask, None, iterations=2)
	
	# find contours in the masks and initialize the current
	# (x, y) centers of the balls

	cue_cnts = cv2.findContours(cueMask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cue_cnts = imutils.grab_contours(cnts)
	cue_center = None

        eight_cnts = cv2.findContours(eightMask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	eight_cnts = imutils.grab_contours(cnts)
	eight_center = None
	
	# only proceed if at least one contour was found
	if len(cue_cnts) > 0 and len(eight_cnts) > 0:
		# find the largest contour in the masks, then use
		# it to compute the minimum enclosing circle and
		# centroid
		cue_Contour = max(cue_cnts, key=cv2.contourArea)
		((x_cue, y_cue), radius_cue) = cv2.minEnclosingCircle(c)
		cue_M = cv2.moments(cue_Contour)
                # finds the center of a blob
		cue_center = (int(cue_M["m10"] / cue_M["m00"]), int(cue_M["m01"] /cue_M["m00"]))
                # uses formula to calculate centroid
                
		# only proceed if the radius meets a minimum size
		if radius_cue > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x_cue), int(y_cue)), int(radius_cue),
				(0, 255, 255), 2)
			cv2.circle(frame, cue_center, 5, (0, 0, 255), -1)
			cuePts.appendleft(cue_center)

	# loop over the set of tracked points
	for i in np.arange(1, len(cuePts)):
		# if either of the tracked points are None, ignore
		# them
		if cuePts[i - 1] is None or cuePts[i] is None:
			continue

                ### DELETE ###
                ###########################################################
		# check to see if enough points have been accumulated in
		# the buffer
		if cueCounter >= 10 and i == 1 and cuePts[-10] is not None:
			# compute the difference between the x and y
			# coordinates and re-initialize the direction
			# text variables
			dX = pts[-10][0] - pts[i][0]
			dY = pts[-10][1] - pts[i][1]
			(dirX, dirY) = ("", "")
 
			# ensure there is significant movement in the
			# x-direction
			if np.abs(dX) > 20:
				dirX = "East" if np.sign(dX) == 1 else "West"
 
			# ensure there is significant movement in the
			# y-direction
			if np.abs(dY) > 20:
				dirY = "North" if np.sign(dY) == 1 else "South"
 
			# handle when both directions are non-empty
			if dirX != "" and dirY != "":
				direction = "{}-{}".format(dirY, dirX)
 
			# otherwise, only one direction is non-empty
			else:
				direction = dirX if dirX != "" else dirY
                ###########################################################
	# otherwise, compute the thickness of the line and
	# draw the connecting lines between the points of
	# the cue and eight ball
	thickness = 6
	cv2.line(frame, cuePts[i], eightPts[i], (0, 0, 255), thickness)
	
 
	# show the frame to our screen and increment the frame counter
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	counter += 1
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()
 
# otherwise, release the camera
else:
	vs.release()
 
# close all windows
cv2.destroyAllWindows()
