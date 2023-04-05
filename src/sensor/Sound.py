import threading
import time
import os

from pygame import mixer

from ..constant import *
from ..utils.log import log
from ..utils.play import play
from ..utils.tts import tts
from ..utils.my_queue import MyQueue

class Sound:
    def __init__(self):
        self.content = MyQueue()
        self.finished = MyQueue()

        self.play_sound = False
        self.end_service = False

        self.callback_start = None
        self.callback_end = None
        self.callback_finish = None
    
    def play(self):
        if self.play_sound:
            return
        
        _sound = self.content.get()
        
        if _sound == END:
            self.callback_finish()
            return
        
        self.finished.push(_sound)
        self.content.pop()
        
        log("Đọc nội dung: {}".format(_sound))
        
        play(_sound)
        if self.callback_start != None:
            self.callback_start()

        self.play_sound = True
        
    def loop(self):
        while not self.end_service:
            # File âm thanh đang được chạy
            #print("Sound service is running")
            if self.play_sound:
                while mixer.music.get_busy() and not self.end_service:
                    pass

                mixer.quit()         
                if self.callback_end != None:
                    self.callback_end()          
                # Tiến hành xóa file

                self.play_sound = False
        log("Kết thúc dịch vụ âm thanh")

    def service(self):
        threading.Thread(name = "sound service", target=self.loop) \
            .start()
        
    def add_sen(self, sen):
        sound_path = tts(sen)
        self.content.push(sound_path)

    def clear(self):
        while self.finished.is_empty() == False:
            f = self.finished.get()
            log("Xóa file : ".format(f))
            os.remove(f)
            self.finished.pop()
    
    def update_scallback(self, _start):
        self.callback_start = _start
    
    def update_ecallback(self, _end):
        self.callback_end =_end
    
    def update_fcallback(self, _finish):
        self.callback_finish = _finish