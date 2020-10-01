from pygame import mixer
from datetime import datetime
from time import time


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("Welcome to Stay Fit Management ...Please enter your name:")
    aa = input("Please enter your name:")

    speak(
        f"........Having a good health not only help you relive your life and work to full, but also you can turn out as a good individual in a society, where others can look up to you.")
    speak(
        f"Let me tell you about this software {aa}.......This software is basically for people who continuosly works for 8 to 10 hours on laptop.......This software will make sure that you are drinking water on proper interval of time.. and will also tell you to take 5 minute eye rest by closing your eye    because  people shows negelence towards their health specially..when on work")


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("forhealth.logs.txt", "a") as s:
        s.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()

    watersecs = 60*60
    eyessecs = 40*60

    while True:
        if time() - init_water > watersecs:
            print(f"Water Drinking time....Please drink a glass of water{aa}... Enter 'Drank' to stop the alarm.")
            speak(f"This you your water drinking time...Please drink a glass of water{aa}")

            musiconloop('water.mp3', 'Drank')

            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye rest time. Enter 'Done' to stop the alarm.")
            speak(f"This you your eye rest time...Please close your eyes and take rest for 5 minutes {aa}")
            musiconloop('water.mp3', 'Done')

            init_eyes = time()
            log_now("Eyes Relaxed at")
