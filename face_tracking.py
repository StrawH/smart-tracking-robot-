# import libraries
import cv2

# find faaces in image
face_cascade = cv2.CascadeClassifier('/home/omar/Desktop/smart_project/lbpcascade_frontalface.xml')

# deffine camera index
cap = cv2.VideoCapture(0)

# flag to take face on time
face_capture_flage = False
const_x = 0
threshold_value_right_left = 15
const_h = 0
threshold_value_up_down = 30

#  start
while True:
    # get image feom camera
    ret, image = cap.read()

    #  convert image to gray and get face dimension in image
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img)

    # make first face captured as refrence
    if face_capture_flage is False:
        for x, y, w, h in faces:
            const_x = x
            const_h = h

        face_capture_flage = True

    # check if there is a face in image
    if faces == ():
        print("no face ")
    else:
        for x, y, w, h in faces:
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            cv2.rectangle(image, pt1, pt2, color=(255, 0, 0), thickness=2)

            # moving right algorithm acoording to refrence
            # prevent distribance
            threshold_right_x = const_x + threshold_value_right_left
            threshold_left_x = const_x - threshold_value_right_left
            threshold_upper_h = const_h + threshold_value_up_down
            threshold_down_h = const_h - threshold_value_up_down

            # right and left
            if x > threshold_left_x & x < threshold_right_x:
                print("iam steady from left  and right")
            elif x < threshold_right_x:
                print(x, threshold_right_x, "moving right ")
            elif x > threshold_left_x:
                print(x, threshold_left_x, "moving left ")

            # forward and backward
            if h > threshold_upper_h & x < threshold_down_h:
                print("iam steady from upp and down ")
            elif h < threshold_down_h:
                print(x, threshold_down_h, "moving down ")
            elif h > threshold_upper_h:
                print(x, threshold_upper_h, "moving up ")

    # dsiplay the action
    cv2.imshow("omar", image)

    if cv2.waitKey(1) & 255 == ord('s'):
        break
