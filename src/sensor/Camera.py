import cv2
import base64
import socketio
import numpy as np

from ..constant import *

class Camera:
    def __init__(self, vid : cv2.VideoCapture, cli : socketio.Client):
        self.vid = vid
        self.cli = cli
    
    def read(self):
        '''
            Hàm thực hiện gọi đọc ảnh + tiền xử lí ảnh
        '''
        __, frame = self.vid.read()
        frame = cv2.resize(frame, (CAM_HEIGHT, CAM_WIDTH))
        frame = self.__b64(frame)


    def __b64(self, frame : np.ndarray):
        __, con = cv2.imencode(".png", frame)
        con = base64.b64decode(con).decode("utf-8")
        return con