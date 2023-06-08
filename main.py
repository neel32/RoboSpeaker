# This is a sample Python script.
import os
import pyttsx3

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
engine = pyttsx3.init()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome To Robo Speaker 1.1. Created By Neel")
    while True:
        x = input("Enter What you want me to speak : ")
        if x=="01":
            break
        # command = f"say {x}"
        # os.system(command)

        engine.say(x)
        engine.runAndWait()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
