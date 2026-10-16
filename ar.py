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
            import re
            WBW = re.split(r'(\s+)', text)
            for part in WBW:
                sys.stdout.write(part)
                sys.stdout.flush()
                if part.strip():
                    time.sleep(delay)
        print("\033[?25h", end="")
        if space:
            print()

    @staticmethod
    def draw(title="Default Title", *texts, delay=0.015, wbw=False):
        if not texts:
            texts = ("Default Label",)
        width = max(len(title), max(len(text) for text in texts))
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
