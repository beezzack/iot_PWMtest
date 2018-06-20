import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('Video streaming', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('Close')
cap.release()
cv2.destroyAllWindows()
