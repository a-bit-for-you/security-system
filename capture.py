import cv2 
'''
OpenCV (Open Source Computer Vision Library) is a machine learning library.The library has more than 2500 optimized algorithms These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects,find similar images from an image database, remove red eyes from images taken using flash.
'''

project_path = r'F:\projects\security-system\image'
# Camera 0 is the integrated camera port. A port is an endpoint of communication.
camera_port = 1
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 retval, im = camera.read()#retval used to return value to cv2. 
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in range(ramp_frames):
 temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = rf"{project_path}/image.jpg"
cv2.imwrite(file, camera_capture)
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
