class Cell:

    def __init__(self, (p1, p2, p3)):
        self.points = (p1, p2, p3)
        self.walls = {
            'left': ((p1, p3), True),
            'bottom': ((p1, p2), True),
            'right': ((p2, p3), True)
        }
        self.orientedUp = True

    def draw(self, pygame, canvas):
        for _, ((initialPoint, finalPoint), exists) in self.walls.iteritems():
            if exists:
                pygame.draw.polygon(
                    canvas,
                    (255, 255, 255),
                    [initialPoint, finalPoint],
                     2
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
        self.orientedUp = not self.orientedUp
        self.walls['left'] = ((p1, p3), True)
        self.walls['bottom'] = ((p1, p2), True)
        self.walls['right'] = ((p2, p3), True)

    def __str__(self):
        p1, p2, p3 = self.points
        return '({}, {}, {}) - O: {}'.format(p1, p2, p3, self.orientedUp)
