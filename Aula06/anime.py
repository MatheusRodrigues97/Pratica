import sys

from PIL import Image

imagens =[]

for arg in sys.argv:
    image = Image.open(arg)
    imagens.append(image)

imagens[0] = save(
    "costumes.git", save_all = True, append_imagens = [imagens[1]], duration = 200, loop = 0
)
