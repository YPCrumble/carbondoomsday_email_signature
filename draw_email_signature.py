# Inspiration from:
# https://code-maven.com/create-images-with-python-pil-pillow
# https://stackoverflow.com/a/38629258/2532070
# https://stackoverflow.com/a/273962/2532070
# https://stackoverflow.com/a/2563883/2532070
# add_border_radius method:
# https://stackoverflow.com/a/11291419/2532070
import sys
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


# ppm = "412.32"
ppm = sys.argv[1]


def add_border_radius(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def create_email_signature(ppm):
    img = Image.new('RGB', (200, 70), color="#FF5964")

    large_font = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 24)
    small_font = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 12)

    size = 16, 16
    skull_image = Image.open('./skull.png', 'r')
    skull_image.thumbnail(size, Image.ANTIALIAS)

    d = ImageDraw.Draw(img)
    d.text((15, 10), ppm, font=large_font, fill="#FFF")
    d.text((103, 20), "PPM", font=small_font, fill="#FFB3B8")
    d.text((140, 10), "CO", font=large_font, fill="#FFF")
    d.text((175, 30), "2", font=small_font, fill="#FFF")
    d.text((35, 44), "Carbon Doomsday API", font=small_font, fill="#FFB3B8")

    img.paste(skull_image, (15, 42), mask=skull_image)

    img = add_border_radius(img, 15)

    enhancer = ImageEnhance.Sharpness(img)
    enhancer.enhance(2.0).save('carbondoomsday_email_signature.png')

if __name__ == '__main__':
    create_email_signature(ppm)
