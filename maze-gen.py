import maze
import argparse
import pygame
import random

def defineArgs():
    parser = argparse.ArgumentParser(
        description='simple script to generate random mazes'
    )

    parser.add_argument(
        '-mw', '--mazeWidth',
        help='maze width',
        type=int,
        default=10,
    )

    parser.add_argument(
        '-mh', '--mazeHeight',
        help='maze heigth',
        type=int,
        default=10,
    )

    parser.add_argument(
        '-cw', '--cellWidth',
        help='cells width',
        type=int,
        default=30,
    )

    parser.add_argument(
        '-ch', '--cellHeight',
        help='cells heigth',
        type=int,
        default=30,
    )

    parser.add_argument(
        '-steps',
        help='show maze generation step by step',
        action='store_false'
    )

    action = parser.add_mutually_exclusive_group()
    action.add_argument(
        '-o', '--output',
        help='save maze image in specified route',
        default='output.jpg',
    )

    action.add_argument(
        '-s', '--show',
        help='show maze on screen',
        action='store_true'
    )

    return parser.parse_args()

def main(args):

    # Get canvas dimensions based on cells width and heigth
    canvasWidth = args.mazeWidth * (args.cellWidth / 2) + 30
    canvasHeigth = args.mazeHeight * args.cellHeight + 10

    # Generate maze
    genMaze = maze.Maze(
                (args.mazeWidth, args.mazeHeight),
                (args.cellWidth, args.cellHeight)
            )

    # Pygame setup
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

        if state:
            state = backtrack(genMaze, pygame, canvas, state)
            pygame.display.update(updateRect)
        else:
            done = True

    if args.show is False:
        pygame.image.save(canvas, args.output or './output.jpg')

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
                elif currentCell.index + maze.width == randomNeighbour.index:
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
                elif currentCell.index - maze.width == randomNeighbour.index:
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
