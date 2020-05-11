#!/usr/bin/env python3

from PIL import Image
import sys


def convert (filename):
    img = Image.open(filename, 'r').convert("RGBA")
    pix_val = list(img.getdata())
    _, _, xmax, ymax = img.getbbox()
    
    ansi_text = ''

    for y in range(ymax):
        for x in range(xmax):
            r, g, b, a = img.getpixel((x,y))
            if a ==  0: ansi_text += '\033[0m  '
            else: ansi_text += '\x1b[48;2;{!s};{!s};{!s}m  '.format( r, g, b)
        ansi_text += '\033[0m\n'

    return ansi_text


def main():
    if len(sys.argv) == 1:
        print("usage: $ ./convert.py {CONVERT_FILE_PATH}")
    else:
        art = convert(sys.argv[1])
        print(art)


if __name__ == "__main__":
    main()
