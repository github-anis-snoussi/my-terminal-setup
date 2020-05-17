#!/usr/bin/env python3

from PIL import Image
import sys

# the image I drew has height of 48 pixels, so this script would work fine, 
# and that's why I'm no bothering doing any kind of check or transformation before converting into ANSI art

# my_name = [
# "",
# "",
# "",
# "",
# "",
# "\033[38;2;64;130;241m     ██      ▄   ▄█    ▄▄▄▄▄          ▄▄▄▄▄    ▄  █ ████▄   ▄ ▄       █▀▄▀█ ▄███▄   \033[0m",
# "\033[38;2;64;130;241m     █ █      █  ██   █     ▀▄       █     ▀▄ █   █ █   █  █   █      █ █ █ █▀   ▀  \033[0m",
# "\033[38;2;64;130;241m     █▄▄█ ██   █ ██ ▄  ▀▀▀▀▄       ▄  ▀▀▀▀▄   ██▀▀█ █   █ █ ▄   █     █ ▄ █ ██▄▄    \033[0m",
# "\033[38;2;64;130;241m     █  █ █ █  █ ▐█  ▀▄▄▄▄▀         ▀▄▄▄▄▀    █   █ ▀████ █  █  █     █   █ █▄   ▄▀ \033[0m",
# "\033[38;2;64;130;241m        █ █  █ █  ▐                              █         █ █ █         █  ▀███▀   \033[0m",
# "\033[38;2;64;130;241m       █  █   ██                                ▀           ▀ ▀         ▀           \033[0m",
# "\033[38;2;64;130;241m      ▀                                                                             \033[0m",
# "\033[38;2;64;130;241m       ▄ ▄    ▄  █ ██     ▄▄▄▄▀     ▀▄    ▄ ████▄   ▄         ▄▀  ████▄    ▄▄▄▄▀    \033[0m",
# "\033[38;2;64;130;241m      █   █  █   █ █ █ ▀▀▀ █          █  █  █   █    █      ▄▀    █   █ ▀▀▀ █       \033[0m",
# "\033[38;2;64;130;241m     █ ▄   █ ██▀▀█ █▄▄█    █           ▀█   █   █ █   █     █ ▀▄  █   █     █       \033[0m",
# "\033[38;2;64;130;241m     █  █  █ █   █ █  █   █            █    ▀████ █   █     █   █ ▀████    █        \033[0m",
# "\033[38;2;64;130;241m      █ █ █     █     █  ▀           ▄▀           █▄ ▄█      ███          ▀         \033[0m",
# "\033[38;2;64;130;241m       ▀ ▀     ▀     █                             ▀▀▀                              \033[0m",
# "\033[38;2;64;130;241m                    ▀                                                               \033[0m",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# ]

def convert (filename):
    img = Image.open(filename, 'r').convert("RGBA")
    _, _, xmax, ymax = img.getbbox()
    
    ansi_text = ''

    for y in range(0,ymax,2):
        for x in range(xmax):
            r1, g1, b1, a1 = img.getpixel((x,y))
            r2, g2, b2, a2 = img.getpixel((x,y+1))
            if a1 ==  0 and a2 == 0:
                ansi_text += ' '
            elif a1 ==  0:
                ansi_text += '\033[38;2;{!s};{!s};{!s}m▄\033[0m'.format( r2, g2, b2)
            elif a2 == 0:
                ansi_text += '\033[38;2;{!s};{!s};{!s}m▀\033[0m'.format( r1, g1, b1)
            else: 
                ansi_text += '\033[48;2;{!s};{!s};{!s}m\033[38;2;{!s};{!s};{!s}m▄\033[0m'.format( r1, g1, b1 ,r2, g2, b2)
        # ansi_text += my_name[int(y/2)]
        ansi_text += '\n'

    return ansi_text


def main():
    if len(sys.argv) == 1:
        print("usage: $ ./new_script.py {CONVERT_FILE_PATH}")
    else:
        art = convert(sys.argv[1])
        # if you want to export the generated image:
        # print(repr(art))
        print(art)


if __name__ == "__main__":
    main()