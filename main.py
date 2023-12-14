# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pathlib import Path
from PIL import Image
import os

def convert_to_webp(source):
    destination = source.with_suffix(".webp")
    image = Image.open(source)
    image.save(destination,format="wepb")
    return destination


def main():
  # paths= Path("images").glob("**/*.png")
   # for path in paths:
  #      webp_path = convert_to_webp(path)
     #   print(webp_path)



     im= Image.open("test.jpg").convert("RGB")


     width, height = im.size
     print(width, height)
     ratio = width / height
     new_width = 600
     new_height = int(new_width / ratio)
     size = (new_width, new_height)
     print(new_height)
     print(im.size)
     im2 = im.resize(size)
     image_path = "images/mobile"


     im2.save(f"{image_path}/test2.webp", "webp", quality=55)
     im.save( "test1.webp", "webp", quality=55)

main()