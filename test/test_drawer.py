from gendraw import GeneticDrawer
from PIL import Image
import os


__author__ = 'Ilya'


if __name__ == '__main__':
    pic_path = os.path.join(os.path.abspath('../'), 'pic')
    pic_name = 'duck.jpg'
    pic_filename = os.path.join(pic_path, pic_name)
    pic = Image.open(pic_filename)
    pic = pic.convert('RGB')
    drawer = GeneticDrawer(pic, n_circles=256, n_generations=10e6)
    drawer.draw()
