from __future__ import annotations
from model.entities import Field
from src.model.constants import MARKER_EMPTY


class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def check_win(self, marker) -> bool:
        pass

    def check_draw(self) -> bool:
        pass

    def __check_win_by_row(self, field) -> bool:

        for cell in field(0, self.__field):

            if cell[0] == cell[1] == cell[2]:
                return True

        return False

    def __check_win_by_column(self, field) -> bool:

        for col in range(0, 3, 1):

            if field[0][col] == field[1][col] == field[2][col]:

                return True

        return False

    def __check_win_by_diagonal(self, field) -> bool:

        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:

            return True

        return False


class Game:

    def __init__(self):
        self.__current_player = MARKER_EMPTY

        self.__field = Field(3, 3)
        self.__referee = Referee(self.__field)


    def set_up(self) -> None:
        pass

    def make_move(self, x, y) -> bool:

        player = self.__current_player

        if not player.try_make_move(): return False

        player.make_move()

        return True


    def finish(self) -> None:
        pass

