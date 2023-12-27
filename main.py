import pygame
import time
from random import randint

pygame.init()

white_color = (255, 255, 255)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
black_color = (0, 0, 0)


class GameBoard:
    def __init__(self, width: int, height: int):
        self.__size = 40
        self.button_size = 100
        self.field = [[0 for column in range(self.__size)] for row in range(self.__size)]
        self.width = width
        self.height = height
        self.cell_width = self.width // self.__size
        self.cell_height = self.height // self.__size
        self.screen_size = [self.width, self.height + self.button_size]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.line_thickness = 3

    def draw_field(self):
        pygame.display.set_caption("Игра 'жизнь'")
        self.screen.fill(white_color)
        pygame.display.flip()
        for width_indent in range(1, self.__size):
            start_pos = ((self.width / self.__size) * width_indent, 0)
            end_pos = ((self.width / self.__size) * width_indent, self.height)
            pygame.draw.line(self.screen, black_color, start_pos, end_pos, self.line_thickness)
        for height_indent in range(1, self.__size):
            start_pos = (0, (self.height / self.__size) * height_indent)
            end_pos = (self.width, (self.height / self.__size) * height_indent)
            pygame.draw.line(self.screen, black_color, start_pos, end_pos, self.line_thickness)
        pygame.display.flip()

    def create_glider(self):
        for raw in range(self.__size):
            for column in range(self.__size):
                draw_condition = ((raw == 0 and column == 0) or
                                  (raw == 1 and (column == 1 or column == 2)) or
                                  (raw == 2 and (column == 0 or column == 1)))

                if draw_condition:
                    self.field[raw][column] = 1

    def create_blinker(self):
        for raw in range(self.__size):
            for column in range(self.__size):
                draw_condition = ((raw == 20 and column in [19, 20, 21]))

                if draw_condition:
                    self.field[raw][column] = 1

    def get_coord_cell(self, row: int, column: int):
        x = column * self.cell_width + (self.cell_width // 2)
        y = row * self.cell_height + (self.cell_height // 2)
        x1 = x - self.cell_width // 2 + self.line_thickness - 1
        y1 = y - self.cell_height // 2 + self.line_thickness - 1
        x2 = self.cell_width - self.line_thickness
        y2 = self.cell_height - self.line_thickness
        return x1, y1, x2, y2

    def draw_cells(self):
        for row in range(len(self.field)):
            for column in range(len(self.field[row])):
                cell = self.field[row][column]
                if cell == 1:
                    coord_cell = game_board.get_coord_cell(row, column)
                    pygame.draw.rect(self.screen, red_color,
                                     coord_cell)
                if cell == 0:
                    coord_cell = game_board.get_coord_cell(row, column)
                    pygame.draw.rect(self.screen, white_color,
                                     coord_cell)
        pygame.display.flip()

    def draw_buttons(self):
        pygame.draw.rect(self.screen, red_color,
                         (0, self.height, self.button_size, self.button_size))
        pygame.draw.rect(self.screen, red_color,
                         (self.width - self.button_size, self.height, self.button_size, self.button_size))
        pygame.display.flip()

    def count_alive_neighbors(self, row: int, column: int):
        alive_neighbors = 0
        for row_neighbors in range(max(0, row - 1), min(self.__size, row + 2)):
            for column_neighbors in range(max(0, column - 1), min(self.__size, column + 2)):
                if (row_neighbors, column_neighbors) != (row, column) and self.field[row_neighbors][column_neighbors]:
                    alive_neighbors += 1
        return alive_neighbors

    def apply_rules_and_update_cells(self):
        new_field = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        for row in range(self.__size):
            for column in range(self.__size):
                alive_neighbors = self.count_alive_neighbors(row, column)
                if self.field[row][column]:
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        new_field[row][column] = 1
                    else:
                        new_field[row][column] = 0
                else:
                    if alive_neighbors == 3:
                        new_field[row][column] = 1
                    else:
                        new_field[row][column] = 0
        self.field = new_field


class Game:
    def start_game(self):
        running = True
        game_board.draw_cells()
        game_board.draw_buttons()
        game_board.draw_cells()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if y in range(600, 700):
                        if x in range(0, game_board.button_size):
                            game_board.create_glider()
                        if x in range(game_board.width - game_board.button_size, game_board.width):
                            game_board.create_blinker()
            game_board.apply_rules_and_update_cells()
            game_board.draw_cells()
            time.sleep(0.01)


game_board = GameBoard(600, 600)
game = Game()
game.start_game()
