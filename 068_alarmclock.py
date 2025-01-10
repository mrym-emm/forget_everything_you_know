# Python alarm clock

import time
import datetime
import pygame # for sounf effect

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "C:\\Users\\Maryam M\\atbs\\pythonProject\\Non-Stop.mp3"
    is_running = True

    while is_running:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime)

        if currenttime == alarm_time:
            print("WakeUp!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)

            pygame.mixer.music.play()

            # # will allow music to keep on playing
            # while pygame.mixer.music.get_busy():
            #     time.sleep(1)

            # play alarm for 10 seconds before ending
            time.sleep(10)

            is_running = False

        time.sleep(1)

        # is_running = False

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

