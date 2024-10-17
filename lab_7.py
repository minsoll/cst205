# MINSOL CHO
# cst205 

#1
from PIL import Image
im2 = Image.open('rgb.jpg')
new_list = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000,) * 3 for a in im2.getdata()]
im2.putdata(new_list)
im2.show()
im2.save("rgb_1.jpg")

#2
from PIL import Image
im2 = Image.open('rgb.jpg')
new_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
                   for a in im2.getdata() ]
im2.putdata(new_list)
im2.show()
im2.save("rgb_2.jpg")

#3
from colorthief import ColorThief
from PIL import Image

color_thief = ColorThief('rgb.jpg')
dominant_color = color_thief.get_color(quality=1)
print(f"dominant color: {dominant_color}")

image = Image.open('rgb.jpg')
pixels = image.load()
width, height = image.size
dominant_color_count = 0
for i in range(width):
    for j in range(height):
        if pixels[i, j] == dominant_color:
            dominant_color_count += 1

print(f" the number of dominat colors : {dominant_color_count}번")

#4
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy
def patch_asscalar(a):
  return a.item()
setattr(numpy, "asscalar", patch_asscalar)
color1_rgb = sRGBColor(176, 63, 81, True)
color2_rgb = sRGBColor(185, 77, 89, True)
color1_lab = convert_color(color1_rgb, LabColor)
color2_lab = convert_color(color2_rgb, LabColor)
delta_e = delta_e_cie2000(color1_lab, color2_lab)
print(f"Apple 1 L*a*b* value: {color1_lab}")
print(f"Apple 2 L*a*b* value: {color2_lab}")

#5
import math
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy

apple1_rgb = (176, 63, 81) 
apple2_rgb = (185, 77, 89)

def color_distance2(c1, c2):
    val = 0
    for i in range(3):
        val += math.pow((c1[i]-c2[i]), 2)
    return math.sqrt(val)

euclidean_dist = color_distance2(apple1_rgb, apple2_rgb)
print(f"euclidean: {euclidean_dist:.2f}")

def patch_asscalar(a):
  return a.item()
setattr(numpy, "asscalar", patch_asscalar)
color1_rgb = sRGBColor(176, 63, 81, True)
color2_rgb = sRGBColor(185, 77, 89, True)

color1_lab = convert_color(color1_rgb, LabColor)
color2_lab = convert_color(color2_rgb, LabColor)

delta_e = delta_e_cie2000(color1_lab, color2_lab)
print(f'L*a*b* {delta_e}')