from PIL import Image
from PIL import ImageChops

image_one = Image.open("../screen_shot/screen_fail_load_vn_language.png").convert('RGB')
image_two = Image.open("../screen.png").convert('RGB')

diff = ImageChops.difference(image_one, image_two)

if diff.getbbox():
    print("images are different")
else:
    print("images are the same")
