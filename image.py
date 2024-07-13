from PIL import Image
from pix2tex.cli import LatexOCR

img = Image.open('data/sum.png')
model = LatexOCR()
print(model(img))