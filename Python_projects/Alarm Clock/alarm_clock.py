import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm.mp3"  # Make sure this file is in the same folder
    
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end="\r")   # keeps updating in place instead of spamming new lines

        if current_time == alarm_time:
            print("\n⏰ WAKE UP!!!")

            # Initialize pygame mixer only once at alarm time
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Keep playing until user stops
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        
        time.sleep(1)

# Show current time before setting alarm
current_time = datetime.datetime.now().strftime("%H:%M:%S")
alarm_time = input(f"Current time: {current_time} \nEnter the alarm time (HH:MM:SS): ")

set_alarm(alarm_time)
