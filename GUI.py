import sys, pygame as pg
import solver

pg.init()

screenSize = 750, 825

screen = pg.display.set_mode(screenSize)

font = pg.font.SysFont(None, 80)

grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

myButton = button((0,255,0), 15, 750, 200, 70, "Solve")

def redrawWindow():
    myButton.draw(screen, (0,0,0))

def drawBackround():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while i * 80 < 720:
        lineWidth = 5 if i%3 > 0 else 10
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i*80) + 15, 15), pg.Vector2((i*80) + 15, 735), lineWidth)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 80) + 15), pg.Vector2(735, (i * 80) + 15), lineWidth)
        i+=1


def drawNumbers():
    row = 0
    offset = 35
    while row < 9:
        col = 0

        while col < 9:

            output = grid[row][col]
            if output != 0:
                numberText = font.render(str(output), True, pg.Color("black"))
                screen.blit(numberText, pg.Vector2((col*80) + offset + 5, (row*80) + offset - 2))
            col += 1

        row += 1



def gameLoop():
    global grid
    drawBackround()
    drawNumbers()
    redrawWindow()
    pg.display.flip()
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT: sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if myButton.isOver(pos) and myButton.text == "Solve":
                solver.solve(grid)
                drawBackround()
                drawNumbers()
                pg.display.flip()
                myButton.text = "Reset"
                myButton.color = (255,0,0)
            elif myButton.isOver(pos) and myButton.text == "Reset":
                grid = [
                        [7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]
                drawBackround()
                drawNumbers()
                pg.display.flip()
                myButton.text = "Solve"
                myButton.color = (0, 255, 0)

while True:
    gameLoop()