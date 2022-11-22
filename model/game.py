import datetime
import model.pacman as p
import model.ghost as g
import pygame


class Game:
    def __init__(self, maze, ghosts, pacmans, drawer=None, games=None, smart=False) -> None:
        self.maze = maze
        self.ghosts = []
        self.players = []
        self.gs = ghosts
        self.ps = pacmans
        self.setEntities()

        self.scores = []
        self.times = []
        self.drawer = drawer

        self.done = False
        self.n_games = games
        self.smart = smart

    def setEntities(self):
        p_c = []
        for player in self.ps:
            p_c.append(p.PacMan(player[0], player[1], self.maze))

        g_c = []
        for ghost in self.gs:
            g_c.append(g.Ghost(ghost[0], ghost[1], self.maze))

        self.ghosts = g_c
        self.players = p_c

    def checkEvents(self):
        if self.n_games is not None:
            if len(self.scores) == self.n_games:
                    self.done = True
        if self.drawer is not None:
            self.done = self.drawer.isDone()

    def checkDead(self):
        new_p = []
        for player in self.players:
            flag = True
            for ghost in self.ghosts:
                if player.getRow() == ghost.getRow() and player.getCol() == ghost.getCol():
                    player.health -= 1
                    if player.health == 0:
                        flag = False
                    break
            if flag:
                new_p.append(player)
        self.players = new_p

    def test(self, clock=None, fps=0):
        while not self.done:
            if clock is not None:
                clock.tick(fps)
            self.checkEvents()

            for player in self.players:
                if self.smart:
                    p_state = [(ghost.getRow(), ghost.getCol) for ghost in self.ghosts]
                    player.moveSmart(p_state)
                else:
                    player.moveRandom()
            if self.drawer is not None:
                self.drawer.draw(self.players, self.ghosts)

            self.checkDead()
            if len(self.players) == 0:
                self.scores.append(self.maze.getDotsEaten())
                self.setEntities()
                self.maze.resetMaze()
                if self.drawer is not None:
                    self.drawer.draw(self.players, self.ghosts)
                continue
            
            if self.maze.getDotsEaten() == 55:
                self.scores.append(self.maze.getDotsEaten())
                self.setEntities()
                self.maze.resetMaze()
                if self.drawer is not None:
                    self.drawer.draw(self.players, self.ghosts)
                continue

            for ghost in self.ghosts:
                ghost.moveRandom()
            self.checkDead()
            if self.drawer is not None:
                self.drawer.draw(self.players, self.ghosts)

            if len(self.players) == 0:
                self.scores.append(self.maze.getDotsEaten())
                self.setEntities()
                self.maze.resetMaze()

            if self.drawer is not None:
                self.drawer.draw(self.players, self.ghosts)


if __name__ == '__main__':
    g = Game()
    g.test()
