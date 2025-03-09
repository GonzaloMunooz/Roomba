import time
import pygame
import random
import concurrent.futures
from Juego import Juego
from utils import lerp



def main():
    juego = Juego()
    juego.run()

if __name__ == '__main__':
    main()
