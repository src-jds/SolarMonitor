import display as screen
import time

def main():
    display = screen.display()
    display.init()
    display.showText("Hello World!")
    time.sleep(5)
    display.close()

main()
