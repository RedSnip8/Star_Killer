import pygame, math

class SpriteSheeter():
    def __init__(self, filename, columns, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.columns = columns
        self.rows = rows
        self.totalcells = columns * rows   

        self.rect = self.sheet.get_rect()
        cwidth = self.cellWidth = self.rect.width / columns
        cheight = self.cellHieght = self.rect.height / rows

        self.cells = list(
            [
                (index % columns * cwidth, index / columns * cheight, cwidth, cheight)
                for index in range(self.totalcells)
            ]
                        )


    def draw(self, surface, cellindex):
        surface.blit( self.sheet, (self.cells[cellindex]))