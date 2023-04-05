import time
import os
from gtts import gTTS
from ..constant import *
from ..utils.log import log

def tts(sentence, prefix = ""):
    storage = '{}/{}-{}.mp3'.format(SOUND_PATH, time.time(), sentence)
    if prefix != "":
        p = '{}/{}'.format(SOUND_PATH, prefix)
        if os.path.exists(p) == False:
            os.makedirs(p)
        storage = '{}/{}-{}.mp3'.format(p, time.time(), sentence)
    _tts = gTTS(sentence, lang="vi", slow=True)
    _tts.save(storage)
    log("Lưu trữ : {}".format(storage))
    return storage