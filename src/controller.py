from __future__ import annotations
from model.entities import Field

class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def check_win(self, marker) -> bool:
        pass

    def check_draw(self) -> bool:
        pass

    def __check_win_by_row(self) -> bool: pass

    def __check_win_by_column(self) -> bool: pass

    def __check_win_by_diagonal(self) -> bool: pass



