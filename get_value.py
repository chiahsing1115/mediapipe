import mediapipe as mp
import cv2
import math
face_det =mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img = cv2.imread("man.jpg") #upload picture.jpg with human face
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) #trans color from BGR to RGB
faceDetection = face_det.FaceDetection(model_selection=1)
result = faceDetection.process(img)
print(result.detections)
#cv2.imshow("people",img)
#cv2.waitKey(0)
if not result.detections: #if no identify human face
    print("no detect")
else:
    h,w,c = img.shape
    for detection in result.detections:
        print(detection)
        NOSE = face_det.get_key_point(detection,face_det.FaceKeyPoint.NOSE_TIP) #identify nose
        EAR = face_det.get_key_point(detection,face_det.FaceKeyPoint.RIGHT_EAR_TRAGION) #identify right ear
        print(NOSE.x)
        print(NOSE.y)
        print(EAR.x)
        print(EAR.y)
        pixelX = int(NOSE.x *w)
        pixelY = int(NOSE.y *h)
        #circle center_nose, radius_nose~right ear, black, solid
        cv2.circle(img,(pixelX,pixelY),int(math.sqrt((NOSE.x*w-EAR.x*w)**2+(NOSE.y*h-EAR.y*h)**2)),(0,0,0),-1)
        #print(int(math.sqrt((NOSE.x-EAR.x)**2+(NOSE.y-EAR.y)**2)))
        #mp_drawing.draw_detection(img,result)
    cv2.imshow("detection",img) #show identify result
    cv2.waitKey(0)

