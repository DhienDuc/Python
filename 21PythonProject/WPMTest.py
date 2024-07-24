import curses
from curses import wrapper

def start_test(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test!")
    stdscr.addstr(1, 0, "Press any key to start!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "A good story encourages us to turn the next page and read more. We want to find out what happens next and what the main characters do and what they say to each other. We may feel excited, sad, afraid, angry or really happy. This is because the experience of reading or listening to a story is much more likely to make us 'feel' that we are part of the story, too. Just like in our 'real' lives, we might love or hate different characters in the story. Perhaps we recognise ourselves or others in some of them. Perhaps we have similar problems."
    current_text = []

    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()
        key = stdscr.getkey()
        
        # Esc button
        if ord(key) == 27:
            break
        # Backspace button
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
            
        stdscr.addstr(0, i, char, color)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_test(stdscr)
    wpm_test(stdscr)

wrapper(main)