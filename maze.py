import graph
import cell

class Maze:

    def __init__(self, (cols, rows), (cellWidth, cellHeigth), pygame, canvas):
        self.cols = cols
        self.rows = rows
        self.cellWidth = cellWidth
        self.cellHeigth = cellHeigth
        self.cellsGraph = graph.Graph()
        self.cells = []

        for row in range(0, rows):
            for col in range(0, cols):
                x = (cellWidth / 2) * col
                y = cellHeigth * (row + 1)
                newCell = cell.Cell((
                    (x, y),
                    (x + cellWidth, y),
                    (x + (cellWidth / 2), cellHeigth * row)
                ))

                if col % 2 != 0:
                    newCell.changeOrientation()
                if row % 2 != 0:
                    newCell.changeOrientation()

                self.cells.append(newCell)


        for c in self.cells:
            c.draw(pygame, canvas)
