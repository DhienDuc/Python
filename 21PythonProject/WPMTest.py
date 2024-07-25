import curses
from curses import wrapper
import time
import random

TEXTS = [
         "A good story encourages us to turn the next page and read more.",
         "You will face many defeats in life, but never let yourself be defeated.",
         "The way to get started is to quit talking and begin doing.",
         "The future belongs to those who believe in the beauty of their dreams.",
         "It is during our darkest moments that we must focus to see the light."
        ]


def start_test(stdscr):
    stdscr.clear()
    # add welcome string in line 0, no space
    stdscr.addstr("Welcome to the typing test!")
    # add press any key string in line 1, no space
    stdscr.addstr(1, 0, "Press any key to start!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = random.choice(TEXTS)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # if not input key, continue while loop to calculate the wpm
        try:
            key = stdscr.getkey()
        except:
            continue
        
        # Esc button
        if ord(key) == 27:
            break
        # Backspace button
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        # add input key to current text 
        elif len(current_text) < len(target_text):
            current_text.append(key)

def display_text(stdscr, target, current, wpm=0):
    # display target
    stdscr.addstr(target)
    # display wpm
    stdscr.addstr(1, 0, f"WPM : {wpm}")
    # display overwrite by current input text
    for i, char in enumerate(current):
        # traverse through target string
        correct_char = target[i]
        # default overwrite by green color
        color = curses.color_pair(1)
        # if input not equal target, overwrite by red color
        if char != correct_char:
            color = curses.color_pair(2)
        # over write char at index i    
        stdscr.addstr(0, i, char, color)

def main(stdscr):
    # init text color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # call function
    start_test(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the test. Press any key to start again!")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)