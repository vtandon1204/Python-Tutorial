# pip install rembg

from rembg import remove

from PIL import Image

original_img = 'my_picture.jpg'
bg_remove_img = 'my_image.png'
get_image = Image.open(original_img)
remove_bg = remove(get_image)
remove_bg.save(bg_remove_img)
