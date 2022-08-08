import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

# face detection thingy
face_Cascade = cv2.CascadeClassifier("venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

# tell if rectangle is on screen (initial conditions)
prevx = 0
prevy = 0
x = 0
y = 0

# loop to run webcam image continuously (break with "esc")
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)

    # drawing the box around my face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    if prevx - x != 0 and prevy - y != 0:
        print(f"Face dectected! {x}, {y}")

    prevx = x
    prevy = y

    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break


vc.release()
cv2.destroyWindow("preview")
