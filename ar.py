import sys
import time

class AR:

    @staticmethod                                                                             
    def animation(text, delay = 0.015, space = True,wbw = False):                                
        print("\033[?25l", end="")
        if wbw == False:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
        else:
            WBW = text.split()
            for word in WBW:
                sys.stdout.write(word+" ")
                sys.stdout.flush()
                time.sleep(delay)
        print("\033[?25h", end="")
        if space:
            print()

    @staticmethod
def draw(title, *texts, delay=0.015, wbw=False):
    width = len(max(texts, key=len))
    border = "-" * (width + 4)

    print(title)
    print(border)
    for text in texts:
        AR.animation(
            "| " + text.ljust(width) + " |",
            delay=delay,
            wbw=wbw
        )
    print(border)
