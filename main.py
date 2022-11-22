from view.drawer import Drawer
from view.ploter import Plotter
from model.maze import Maze
from model.game import Game
import pygame
from sys import exit


def createGame():
    pygame.init()
    window = pygame.display.set_mode((550, 550))
    maze = Maze()
    d = Drawer(window, maze)
    pacmans = [[1, 9], [9, 1], [9, 1]]
    ghosts = [[5, 5], [5, 6]]
    # game takes window parameter in order to be able to close the window
    g = Game(maze=maze, pacmans=pacmans, ghosts=ghosts, games=1000,smart=True)
    return g

game = createGame()
#game.test(pygame.time.Clock(), fps=0)
game.test()
Plotter.plot(game.scores, "Average score ---> ")
