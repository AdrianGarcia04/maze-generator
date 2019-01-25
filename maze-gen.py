import maze
import argparse
import pygame
import random

mazeWidth = 50
mazeHeigth = 30

cellsWidth = 30
cellsHeigth = 30

canvasWidth = mazeWidth * (cellsWidth / 2) + 40
canvasHeigth = mazeHeigth * cellsHeigth + 10

def defineArgs():
    parser = argparse.ArgumentParser(
        description='simple script to generate random mazes'
    )

    return parser.parse_args()

def main(args):
    genMaze = maze.Maze((mazeWidth, mazeHeigth), (cellsWidth, cellsHeigth))

    pygame.init()
    canvas = pygame.display.set_mode((canvasWidth, canvasHeigth))
    pygame.display.set_caption('Maze generator')


    # Choose a random cell and mark it as visited
    currentCell = random.choice(genMaze.cells)
    currentCell.currentCell = True
    genMaze.visitCell(currentCell)

    updateRect = pygame.Rect(0, 0, canvasWidth, canvasHeigth)

    done = False

    state = ([], currentCell, updateRect)
    genMaze.draw(pygame, canvas)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # While there are unvisited cells
            if state:
                state = backtrack(genMaze, pygame, canvas, state)
                pygame.display.update(updateRect)
            else:
                done = True
                pygame.image.save(canvas, './output.jpg')


def backtrack(maze, pygame, canvas, (stackOfCells, currentCell, updateRect)):
    if maze.existsUnvisitedCells():

        neighbours = maze.neighbours(currentCell)
        unvisitedNeighbours = maze.getUnvisited(neighbours)

        # If the current cell has any unvisited neighbours
        if unvisitedNeighbours:
            # Pick a random neighbour
            randomNeighbour = random.choice(unvisitedNeighbours)

            # Push the current cell to stack
            stackOfCells.append(currentCell)

            # Remove the wall between the current cell and the neighbour
            if currentCell.orientedUp:
                if currentCell.index - 1 == randomNeighbour.index:
                    currentCell.removeWall('left')
                    randomNeighbour.removeWall('left')
                    updateRect = maze.genUpdateRect(currentCell, 'left')
                elif currentCell.index + mazeWidth == randomNeighbour.index:
                    currentCell.removeWall('bottom')
                    randomNeighbour.removeWall('bottom')
                    updateRect = maze.genUpdateRect(currentCell, 'bottom')
                else:
                    currentCell.removeWall('right')
                    randomNeighbour.removeWall('right')
                    updateRect = maze.genUpdateRect(currentCell, 'right')
            else:
                if currentCell.index + 1 == randomNeighbour.index:
                    currentCell.removeWall('left')
                    randomNeighbour.removeWall('left')
                    updateRect = maze.genUpdateRect(randomNeighbour, 'left')
                elif currentCell.index - mazeWidth == randomNeighbour.index:
                    currentCell.removeWall('bottom')
                    randomNeighbour.removeWall('bottom')
                    updateRect = maze.genUpdateRect(randomNeighbour, 'bottom')
                else:
                    currentCell.removeWall('right')
                    randomNeighbour.removeWall('right')
                    updateRect = maze.genUpdateRect(randomNeighbour, 'right')

            # Draw cells
            currentCell.draw(pygame, canvas)
            randomNeighbour.draw(pygame, canvas)

            # Make the neighbour the current cell and mark it as visited
            currentCell.currentCell = False
            currentCell = randomNeighbour
            currentCell.currentCell = True
            maze.visitCell(currentCell)
            updateRect = pygame.Rect(updateRect)

        elif stackOfCells:
            cell = stackOfCells.pop()
            currentCell = cell
            currentCell.poped = True
        return (stackOfCells, currentCell, updateRect)
    else:
        return None

main(defineArgs())
