from pygame import mixer

def play(sound_path):
    mixer.init()
    mixer.music.load(sound_path)
    mixer.music.play()