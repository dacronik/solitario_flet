import flet
from flet import *
from solitaire import Solitaire

def main(page:Page):
    solitaire = Solitaire()
    page.add(solitaire)

if __name__ == '__main__':
    flet.app(target=main, assets_dir="images")