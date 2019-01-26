import graph
import cell

class Maze:

    def __init__(self, (width, heigth), (cellWidth, cellHeigth)):
        self.width = width
        self.heigth = heigth
        self.cellWidth = cellWidth
        self.cellHeigth = cellHeigth
        self.cellsGraph = graph.Graph()
        self.cells = []
        self.cellsVisited = 0

        i = 0
        for row in range(0, heigth):
            for col in range(0, width):
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

                newCell.index = i
                self.cells.append(newCell)
                i += 1

        for i in range(0, len(self.cells)):
            currentCell = self.cells[i]
            if currentCell.orientedUp:
                if i - 1 > 0 and not self.cells[i - 1].orientedUp:
                    cellToConnect = self.cells[i - 1]
                    self.cellsGraph.addConnection(currentCell, cellToConnect)
                if i + 1 < len(self.cells) and not self.cells[i + 1].orientedUp:
                    cellToConnect = self.cells[i + 1]
                    self.cellsGraph.addConnection(currentCell, cellToConnect)
                if i + self.width < len(self.cells):
                    cellToConnect = self.cells[i + self.width]
                    self.cellsGraph.addConnection(currentCell, cellToConnect)

    def existsUnvisitedCells(self):
        return self.cellsVisited < len(self.cells)

    def getCell(self, cell):
        if cell in self.cells:
            cellIndex = self.cells.index(cell)
            return self.cells[cellIndex]

    def visitCell(self, cell):
        cell = self.getCell(cell)
        cell.visit()
        self.cellsVisited += 1

    def neighbours(self, cell):
        cell = self.getCell(cell)
        return self.cellsGraph.getConnections(cell)

    def getUnvisited(self, cells):
        unvisited = []
        for cell in cells:
            if not cell.visited:
                unvisited.append(cell)

        return unvisited

    def draw(self, pygame, canvas):
        for cell in self.cells:
            cell.draw(pygame, canvas)

    def genUpdateRect(self, refCell, direction):
        # The reference cell is always oriented upwards
        p1, p2, p3 = refCell.points

        x = y = width = heigth = 0

        if direction == 'left':
            x = p1[0] - 5
            y = p3[1] - 5
            width = p3[0] - x + 5
            heigth = p1[1] - y + 5
        elif direction == 'bottom':
            x = p1[0] - 5
            y = p1[1] - 5
            width = p2[0] - x + 5
            heigth = 10
        elif direction == 'right':
            x = p3[0] - 5
            y = p3[1] - 5
            width = p2[0] - x + 5
            heigth = p2[1] - y + 5

        return (x, y, width, heigth)

    def makeEntranceAndExit(self, pygame, canvas):
        self.cells[0].removeWall('left')
