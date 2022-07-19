import cv2
# Stop Sign Cascade Classifier xml
#stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')
stop_sign = cv2.CascadeClassifier('haarcascade_car.xml')
cap = cv2.VideoCapture('cars.avl')
#cap = cv2.VideoCapture(0)
while True:
    #img = cv2.imread('sign.png')
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 10)
    print(stop_sign_scaled)
    # Detect the stop sign, x,y = origin points, w = width, h = height
    for (x, y, w, h) in stop_sign_scaled:
        # Draw rectangle around the stop sign
        stop_sign_rectangle = cv2.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            (0, 255, 0), 3)
        # Write "Stop sign" on the bottom of the rectangle
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                     text="stop sign ",
                                     org=(x, y+h+30),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv2.LINE_4)
    cv2.imshow('frame', img)
    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
