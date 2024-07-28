from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        sencond_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in {minute_left:02d}:{sencond_left:02d}")

    playsound("Alarm-clock.mp3")

seconds = input("Please input alarm timer: ")    
if seconds.isdigit():
    alarm(int(seconds))
