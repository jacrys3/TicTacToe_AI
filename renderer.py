import pygame
from pygame.locals import *
import game
 
class Renderer:

    newGame = game.TicTacToe(1)

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.color = (255,255,255)
        self.board = self.newGame.getBoard()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.draw_initial_board()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 200 and pos[0] <= 440 and pos[1] >= 80 and pos[1] <= 320 and not Renderer.newGame.isWin():
                row = int((pos[1] - 80) / 80)
                col = int((pos[0] - 200) / 80)
                self.newGame.doTurn(row, col)
                    
        if self.newGame.isWin() == 1:
            self.draw_outcome(True)
        elif self.newGame.isWin() == -1:
            self.draw_outcome(False)

    def render_board(self):
        self.board = self.newGame.getBoard()
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 1:
                    self.draw_o(row, col)
                elif self.board[row][col] == -1:
                    self.draw_x(row, col)

    def draw_x(self, row, col):
        start = (((col * 80) + 215), ((row * 80) + 95))
        end = (((col * 80) + 265), ((row * 80) + 145))
        pygame.draw.line(self._display_surf, self.color, start, end, 2)
        start = (((col * 80) + 265), ((row * 80) + 95))
        end = (((col * 80) + 215), ((row * 80) + 145))
        pygame.draw.line(self._display_surf, self.color, start, end, 2)

    def draw_o(self, row, col):
        center = (((col * 80) + 240) , ((row * 80) + 120))
        pygame.draw.circle(self._display_surf, self.color, center, 30, 2)

    def draw_outcome(self, didWin):
        if didWin:
            win = pygame.font.SysFont('You win!', 40)
            winMessage = win.render('You win!', True, self.color)
            self._display_surf.blit(winMessage, (20, 100))
        else:
            lose = pygame.font.SysFont('You lose!', 40)
            loseMessage = lose.render('You lose!', True, self.color)
            self._display_surf.blit(loseMessage, (20, 100))
            
    def on_render(self):
        self.render_board()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()
    
    def draw_initial_board(self):
        pygame.draw.line(self._display_surf, self.color, (280,80), (280, 320))
        pygame.draw.line(self._display_surf, self.color, (360,80), (360, 320))
        pygame.draw.line(self._display_surf, self.color, (200,160), (440, 160))
        pygame.draw.line(self._display_surf, self.color, (200,240), (440, 240))

        pygame.draw.line(self._display_surf, self.color, (200,80), (440, 80))
        pygame.draw.line(self._display_surf, self.color, (200,320), (440, 320))
        pygame.draw.line(self._display_surf, self.color, (200,80), (200, 320))
        pygame.draw.line(self._display_surf, self.color, (440,80), (440, 320))

        title = pygame.font.SysFont('TicTacToe', 50)
        titleText = title.render('TicTacToe', True, self.color)
        self._display_surf.blit(titleText, (20, 20))
 
if __name__ == "__main__" :
    window = Renderer()
    window.on_execute()