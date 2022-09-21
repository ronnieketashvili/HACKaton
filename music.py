from pygame import mixer


def typing_sound():
    mixer.init()
    mixer.music.load('SoundEffects/typing sound.wav')
    mixer.music.play()

