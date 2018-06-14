import cv2

cascPath = "haarcascade_frontalface_default.xml"
faseCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faseCascade.detectMultiScale{
        gray,
        scaleFactor=1.1,
        minNeighbors = 5,
        minSize = (60,60),
        flags = cv2.CV_FEATURE_PARAMS_HAAR
    }

    print("Found {0} faces!".format(len(faces)))


    for (x,y,w,g) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("face detect", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
