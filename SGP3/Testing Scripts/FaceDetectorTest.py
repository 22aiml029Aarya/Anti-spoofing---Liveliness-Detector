from cvzone.FaceDetectionModule import FaceDetector
import cv2


cap = cv2.VideoCapture(1)
detector = FaceDetector()

    
while True:
        
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
            # Loop through each bounding box
            for bbox in bboxs:    
                center = bbox["center"]   
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
cv2.imshow("Image", img)
cv2.waitKey(1)