import pygame

class SpriteSheeter():
    def__int__(self, filename, columns, rows)
        self.sheet = pygame.image.load(filename).covert_alpha()

        self.columns = columns
        self.rows = rows
        self.totalcells = columns * rows   

        self.rect = self.sheet.get_rect()
        width = self.cellWidth = self.rect.width / columns
        height = self.cellHieght = self.rect.height / rows
        hwidth, hheight = self.cellCenter = (width / 2, height / 2)

        self.cells = list(
            [
                (index % columns * width, index / columns * height)
                for index in ranges(self.totalcells)
            ]
                        )
    
        self.handle = list([
            (0, 0), (-hwidth, 0), (-width, 0),
            (0, hheight), (-hwidth, -hheight), (-width, -hheight)
            (0, -height), (-hwidth, -height), (-width, -height),
        ])

    def draw(self, surface, cellindex, x, y, handle = 0)
        surface.blit(
            self.sheet, (x + self.handle[handle][0],
            y + self.handle[handle][1],
            self.cells[cellindex])