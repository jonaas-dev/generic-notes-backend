
"""
Resum: Scrip per automatitzar la vinculació entre el text i l'imatge.

Dependencies:

pip3 install pillow
pip3 install matplotlib
"""

from PIL import Image,ImageDraw,ImageFont, ImageOps
import textwrap



# Vars
backgroundImage = "Frases Ludwig Von Mises.png"

text_1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it"

font_1 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",45)

# Tindria que ser estandar per a totes les imatges



# main
img = Image.open(backgroundImage)

draw = ImageDraw.Draw(img)  

font = font_1
text = text_1

FOREGROUND = (255, 255, 255)
WIDTH = 500
HEIGHT = 50

# draw.text((w,h),text,font = font)

lines = textwrap.wrap(text, width=39)
print(lines)
y_text = HEIGHT + 550
for line in lines:
    print(line)
    width, height = font.getsize(line)
    draw.text((10, y_text), line, font=font, fill=FOREGROUND)
    print((WIDTH - width) / 2)
    print(y_text)
    y_text += height



img.save("output_"+"Frases Ludwig Von Mises.png", "PNG")











"""
----------------------------------------------------------------------------------
PETIT EXEMPLE: 

# the rest is like the original code:
# sample text and font
unicode_text = u"Hello World!"

# get the line size
text_width, text_height = font.getsize(unicode_text)

# create a blank canvas with extra space between lines
canvas = Image.new('RGB', (text_width + 10, text_height + 10), "orange")

# draw the text onto the text canvas, and use black as the text color
draw = ImageDraw.Draw(canvas)
draw.text((5,5), u'Hello World!', 'blue', font)

# save the blank canvas to a file
canvas.save("unicode-text.png", "PNG")
canvas.show()

"""
