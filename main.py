from csi_camera import CSI_Camera
from detect import *
from camera import *
from track import *
import os

os.system ('sudo systemctl restart nvargus-daemon')

if __name__ == "__main__":
    cam = Camera()
    det = Detect(cam) 
    while True:
        img,info = det.captureimage()
        
        det.track.trackobject(info)
        
        det.track.visualise(img)
        
        cv2.imshow("Capture",img)
        
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    cv2.destroyAllWindows()
        
        
    