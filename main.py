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

def getImages():
    paths = Path("images").glob("**/*.jpg")
    print(paths)
    for path in paths:

      convert(path)

    paths = Path("images").glob("**/*.jpeg")
    print(paths)
    for path in paths:
        convert(path)

def convert(path):
    im = Image.open(path).convert("RGB")

    filename=os.path.basename(path).split('/')[-1].replace(".jpg","")


    print(filename,"aqui")

    width, height = im.size
    print(width, height)
    ratio = width / height
    new_width_mobile = 400
    new_height_mobile = int(new_width_mobile / ratio)
    size_mobile = (new_width_mobile, new_height_mobile)

    new_width_normal = 1200
    new_height_normal = int(new_width_normal / ratio)
    size_normal = (new_width_normal, new_height_normal)

    new_width_thumbmail = 200
    new_height_thumbnail = int(new_width_thumbmail / ratio)
    size_thumbnail = (new_width_thumbmail, new_height_thumbnail)

    print(im.size)
    im_mobile = im.resize(size_mobile)

    im_thumbnail = im.resize(size_thumbnail)
    im_normal = im.resize(size_normal)
    image_path_mobile = "images/mobile"
    image_path_thumbnail = "images/thumbnail"
    image_path_normal = "images/normal"

    im_mobile.save(f"{image_path_mobile}/{filename}({new_width_mobile}x{new_width_thumbmail}).webp", "webp", quality=55)
    im_normal.save(f"{image_path_normal}/{filename}({new_width_normal}x{new_height_normal}).webp", "webp", quality=55)
    im_thumbnail.save(f"{image_path_thumbnail}/{filename}({new_width_thumbmail}x{new_height_normal}).webp", "webp", quality=55)
    im.save("test1.webp", "webp", quality=55)

def main():
     getImages()


"""
   im= Image.open("test.jpg").convert("RGB")
     filename = Image.open("test.jpg").filename.replace(".jpg", "")
     print(filename)
     width, height = im.size
     print(width, height)
     ratio = width / height
     new_width_mobile = 400
     new_height_mobile = int(new_width_mobile / ratio)
     size_mobile = (new_width_mobile, new_height_mobile)

     new_width_normal = 1200
     new_height_normal = int(new_width_normal / ratio)
     size_normal = (new_width_normal, new_height_normal)

     new_width_thumbmail = 200
     new_height_thumbnail = int(new_width_thumbmail/ ratio)
     size_thumbnail = (new_width_thumbmail, new_height_thumbnail)

     print(im.size)
     im_mobile = im.resize(size_mobile)
     im_thumbnail = im.resize(size_thumbnail)
     im_normal  = im.resize(size_normal)
     image_path_mobile = "images/mobile"
     image_path_thumbnail = "images/thumbnail"
     image_path_normal = "images/normal"


     im_mobile.save(f"{image_path_mobile}/{filename}.webp", "webp", quality=55)
     im_normal.save(f"{image_path_normal}/{filename}.webp", "webp", quality=55)
     im_thumbnail.save(f"{image_path_thumbnail}/{filename}.webp", "webp", quality=55)
     im.save( "test1.webp", "webp", quality=55)
  """


main()