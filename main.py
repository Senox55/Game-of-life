import pygame

pygame.init()

white_color = (255, 255, 255)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
black_color = (0, 0, 0)


class GameBoard:
    def __init__(self, width, height, *field):
        self.__size = 3
        self.start_field = [['1' for i in range(self.__size)] for j in range(self.__size)]
        self.field = field
        self.width = width
        self.height = height
        self.screen_size = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_field(self):
        pygame.display.set_caption("Игра 'жизнь'")
        self.screen.fill(white_color)
        pygame.display.flip()
        for width_indent in range(1, self.__size):
            start_pos = ((self.width / self.__size) * width_indent, 0)
            end_pos = ((self.width / self.__size) * width_indent, self.height)
            pygame.draw.line(self.screen, black_color, start_pos, end_pos, 3)
        for height_indent in range(1, self.__size):
            start_pos = (0, (self.height / self.__size) * height_indent)
            end_pos = (self.width, (self.height / self.__size) * height_indent)
            pygame.draw.line(self.screen, black_color, start_pos, end_pos, 3)
        pygame.display.flip()

    def get_coord_cell(self, number_cell):
        center_coord = number_cell * (self.height // self.__size) * self.__size + number_cell * (
                    self.width // self.__size)
        x1 = center_coord - self.width / 2
        y1 = center_coord - self.height / 2
        x2 = center_coord + self.width / 2
        y2 = center_coord - self.height / 2
        return x1, y1, x2, y2



    def draw_cells(self):
        for row in range(len(self.field)):
            for column in range(len(self.field[row])):
                cell = self.field[row][column]
                number_cell = row * column
                print(number_cell)
                if cell != ' ':
                    coord_cell = game_board.get_coord_cell(number_cell)
                    print(coord_cell)
                    pygame.draw.rect(self.screen, black_color,
                                     coord_cell)


class Game:
    def start_game(self):
        game_board.draw_field()
        game_board.draw_cells()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def change_field(self):
        pass


game_board = GameBoard(600, 600)
game = Game()
game.start_game()
