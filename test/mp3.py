import sys
sys.path.append("./")

from src.sensor.Sound import Sound
sound = Sound()
sound.add_sen("Nguyễn Đức Bảo Lâm")
sound.add_sen("là người cực kỳ dễ thương")
sound.add_sen("nó hoàn toàn là sự thật")

sound.service()

try:
    while True:
        sound.play()
except:
    print("Thoát chương trình")
    sound.end_service = True
    sys.exit(0)
# print(sound.content.get())
# sound.content.pop()
# print(sound.content.get())