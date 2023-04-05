import os

from .constant import *

if os.path.exists(SOUND_PATH) == False:
    os.makedirs(SOUND_PATH)