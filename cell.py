class Cell:

    def __init__(self, (p1, p2, p3)):
        self.points = (p1, p2, p3)
        self.walls = {
            'left': ((p1, p3), True),
            'bottom': ((p1, p2), True),
            'right': ((p2, p3), True)
        }
        self.orientedUp = True
        self.visited = False
        self.index = 0
        self.status = None

    def draw(self, pygame, canvas):
        for _, ((initialPoint, finalPoint), exists) in self.walls.iteritems():
            if exists:
                pygame.draw.polygon(
                    canvas,
                    (255, 255, 255),
                    [initialPoint, finalPoint],
                     1
                )
            else:
                pygame.draw.polygon(
                    canvas,
                    (0, 0, 0),
                    [initialPoint, finalPoint],
                    1
                )

    def changeOrientation(self):
        p1, p2, p3 = self.points
        (x1, y1) = p1
        (x2, y2) = p2
        (x3, y3) = p3

        p1 = (x1, y3)
        p2 = (x2, y3)
        p3 = (x3, y1)

        self.points = (p1, p2, p3)
        if self.orientedUp:
            self.walls['right'] = ((p1, p3), True)
            self.walls['bottom'] = ((p1, p2), True)
            self.walls['left'] = ((p2, p3), True)
        else:
            self.walls['left'] = ((p1, p3), True)
            self.walls['bottom'] = ((p1, p2), True)
            self.walls['right'] = ((p2, p3), True)
        self.orientedUp = not self.orientedUp

    def visit(self):
        self.visited = True

    def removeWall(self, wall):
        ((pi, pj), exists) = self.walls[wall]
        self.walls[wall] = ((pi, pj), False)

    def asStart(self, pygame, canvas):
        p1, p2, p3 = self.points
        if self.orientedUp:
            p1 = (p1[0] + 5, p1[1] - 5)
            p2 = (p2[0] - 5, p2[1] - 5)
            p3 = (p3[0], p3[1] + 5)
        else:
            p1 = (p1[0] + 5, p1[1] + 5)
            p2 = (p2[0] - 5, p2[1] + 5)
            p3 = (p3[0], p3[1] - 5)
        pygame.draw.polygon(
            canvas,
            (116, 154, 7),
            [p1, p2, p3]
        )
        self.draw(pygame, canvas)

    def asGoal(self, pygame, canvas):
        p1, p2, p3 = self.points
        if self.orientedUp:
            p1 = (p1[0] + 5, p1[1] - 5)
            p2 = (p2[0] - 5, p2[1] - 5)
            p3 = (p3[0], p3[1] + 5)
        else:
            p1 = (p1[0] + 5, p1[1] + 5)
            p2 = (p2[0] - 5, p2[1] + 5)
            p3 = (p3[0], p3[1] - 5)
        pygame.draw.polygon(
            canvas,
            (193, 59, 10),
            [p1, p2, p3]
        )
        self.draw(pygame, canvas)


    def __str__(self):
        p1, p2, p3 = self.points
        return '{} = ({}, {}, {}) - O: {}'.format(self.index, p1, p2, p3, self.orientedUp)
