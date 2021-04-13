from PIL import Image
import argparse
import os

wd = os.getcwd()

parser = argparse.ArgumentParser(description="resize and rotate images in directory")
parser.add_argument('-i','--input_dir', type=str, metavar='',required=True,help='folder containing the images you want to resize')
parser.add_argument('-n', '--resize', type=int, metavar='',required=True, help='resizing factor')
args = parser.parse_args()



#target directory
f = str(wd)+"/"+str(args.input_dir)+"/"

# rotate images if vertical
for i in range(0, len(os.listdir(f))):
  f_img = f+os.listdir(f)[i]
  im = Image.open(f_img)
  width, height = im.size
  if width < height:
    im = im.rotate(90, expand = True)
    im.save(f_img)


# resize images
for i in range(0, len(os.listdir(f))):
  f_img = f+os.listdir(f)[i]
  im = Image.open(f_img)
  width, height = im.size
  if width > 800:
      im_rs = im.resize((int(width/args.resize), int(height/args.resize)))
      im_rs.save(f_img)
