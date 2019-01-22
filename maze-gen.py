import maze
import argparse
import pygame

def defineArgs():
    parser = argparse.ArgumentParser(
        description='simple script to generate random mazes'
    )

    return parser.parse_args()

def main(args):
    pygame.init()
    canvas = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Maze generator')

    genMaze = maze.Maze((30, 10), (40, 40), pygame, canvas)


    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()



main(defineArgs())
