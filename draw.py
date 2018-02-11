# Inspiration from:
# https://code-maven.com/create-images-with-python-pil-pillow
# https://stackoverflow.com/a/38629258/2532070
# https://stackoverflow.com/a/273962/2532070
# https://stackoverflow.com/a/2563883/2532070
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

ppm = "412.32"
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

enhancer = ImageEnhance.Sharpness(img)
enhancer.enhance(2.0).save('carbondoomsday_email_signature.png')
