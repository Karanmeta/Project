from mtcnn import MTCNN
detector = MTCNN()
import cv2

img=cv2.imread('images/casual.webp')
output=detector.detect_faces(img)
for i in output:
    x,y,width,height=i['box']
    left_eyeX,left_eyeY=i['keypoints']['left_eye']
    right_eyeX,right_eyeY=i['keypoints']['right_eye']
    mouse_leftX,mouse_leftY=i['keypoints']['mouth_left']
    mouse_rightX,mouse_rightY=i['keypoints']['mouth_right']
    noseX,noseY=i['keypoints']['nose']

    cv2.circle(img,center=(left_eyeX,left_eyeY),radius=5,color=(0,255,0),thickness=-1)
    cv2.circle(img,center=(right_eyeX,right_eyeY),radius=5,color=(0,255,0),thickness=-1)
    cv2.circle(img,center=(mouse_leftX,mouse_leftY),radius=5,color=(0,255,0),thickness=-1)
    cv2.circle(img,center=(mouse_rightX,mouse_rightY),radius=5,color=(0,255,0),thickness=-1)
    cv2.circle(img,center=(noseX,noseY),radius=5,color=(0,255,0),thickness=-1)
    cv2.rectangle(img,pt1=(x,y),pt2=(x+width,y+height),color=(0,255,0),thickness=2)

    print(output)
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
