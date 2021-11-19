import pygame
from typing import List, Tuple, Optional, NamedTuple, Iterable, Union, Callable
from enum import Enum
from itertools import product, chain

# Types

Color = Tuple[int, int, int]

# Game Constants

FPS = 5

MINIMAX_DEPTH = 5
MAX_ITERATIONS = 200


BOARD_SIZE = 8

PAWN_ROW_COUNT = 3


# Window Constants
WINDOW_SIZE = 800

FIELD_SIZE = WINDOW_SIZE // BOARD_SIZE
PIECE_SIZE = FIELD_SIZE / 2 - 8
MARK_THICK = 2
POS_MOVE_MARK_SIZE = PIECE_SIZE / 2

WHITE: Color = (255, 255, 255)
BLACK: Color = (0, 0, 0)
BLUE: Color = (0, 0, 255)
RED: Color = (255, 0, 0)
GREEN: Color = (0, 255, 0)


class Player(Enum):
    BLUE = BLUE
    WHITE = WHITE

    def opponent(self) -> 'Player':
        return Player.BLUE if self == Player.WHITE else Player.WHITE


class Move(NamedTuple):
    """
    Move is a tuple that describes the possible move of a Pawn
    onto position (to_x, to_y). Possibly capturing a pawn
    """
    pawn: "Pawn"
    to_x: int
    to_y: int
    captures: Optional["Pawn"] = None

    def draw(self, window: "pygame.Surface") -> None:
        x = self.to_x * FIELD_SIZE
        y = self.to_y * FIELD_SIZE
        pygame.draw.circle(window, RED,
                           (x + FIELD_SIZE / 2, y + FIELD_SIZE / 2),
                           POS_MOVE_MARK_SIZE)


class Field(NamedTuple):
    """
    Field is a tuple that describes empty field on a board
    """
    x: int
    y: int

    def draw(self, window: "pygame.Surface") -> None:
        pass


class Pawn(NamedTuple):
    """
    Field represents an object on the board
    """
    x: int
    y: int
    player: Player
    king: bool = False

    def draw(self, window: "pygame.Surface") -> None:
        x = self.x * FIELD_SIZE
        y = self.y * FIELD_SIZE

        pygame.draw.circle(window, self.player.value,
                           (x + FIELD_SIZE / 2, y + FIELD_SIZE/2),
                           PIECE_SIZE)

        if self.king:
            pygame.draw.circle(window, GREEN,
                               (x + FIELD_SIZE / 2, y + FIELD_SIZE / 2),
                               PIECE_SIZE / 2)

    def _maybe_jumps(self) -> List[Tuple[int, int]]:
        if self.king:
            return [
                (self.x + 1, self.y + 1),
                (self.x + 1, self.y - 1),
                (self.x - 1, self.y + 1),
                (self.x - 1, self.y - 1)
            ]
        elif self.player == Player.BLUE:
            return [
                (self.x + 1, self.y + 1),
                (self.x - 1, self.y + 1)
            ]
        else:
            return [
                (self.x + 1, self.y - 1),
                (self.x - 1, self.y - 1)
            ]

    def possible_jumps(self, size: int) -> Iterable[Tuple[int, int]]:
        return filter(
            lambda point: all(0 <= x and x < size for x in point),
            self._maybe_jumps()
        )

    def _maybe_captures(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        if self.king:
            return [
                ((self.x + 2, self.y + 2), (self.x + 1, self.y + 1)),
                ((self.x + 2, self.y - 2), (self.x + 1, self.y - 1)),
                ((self.x - 2, self.y + 2), (self.x - 1, self.y + 1)),
                ((self.x - 2, self.y - 2), (self.x - 1, self.y - 1)),
            ]
        elif self.player == Player.BLUE:
            return [
                ((self.x + 2, self.y + 2), (self.x + 1, self.y + 1)),
                ((self.x - 2, self.y + 2), (self.x - 1, self.y + 1)),
            ]
        else:
            return [
                ((self.x + 2, self.y - 2), (self.x + 1, self.y - 1)),
                ((self.x - 2, self.y - 2), (self.x - 1, self.y - 1)),
            ]

    def possible_captures(self, size: int) -> Iterable[Tuple[Tuple[int, int], Tuple[int, int]]]:
        return filter(
            lambda points: all(all(0 <= x and x < size for x in point)
                               for point in points),
            self._maybe_captures()
        )

    def moved(self, new_x: int, new_y: int, size: int) -> "Pawn":
        king = self.king or new_y == (
            0 if self.player == Player.WHITE else (size - 1))
        return Pawn(new_x, new_y, self.player, king)

    def to_field(self) -> Field:
        return Field(self.x, self.y)


Entity = Union[Pawn, Field]


def is_field_black(point: Tuple[int, int]) -> bool:
    x, y = point
    return bool((x % 2) ^ (y % 2))


class Board:
    def __init__(self, size: int = BOARD_SIZE, max_iterations: int = MAX_ITERATIONS) -> None:
        self.player = Player.WHITE
        self.size = size
        self.board: List[List[Entity]] = [
            [Field(x, y) for x in range(size)] for y in range(size)
        ]
        self._marked: Optional[Pawn] = None
        self.iterations = max_iterations
        self.blue = 0
        self.white = 0

    def copy(self) -> 'Board':
        board = Board(self.size)
        board.board = [row.copy() for row in self.board]
        return board

    @classmethod
    def populate_with_pawns(cls,
                            size: int = BOARD_SIZE,
                            pawn_row_count: int = PAWN_ROW_COUNT) -> 'Board':
        self = cls(size)

        blue_pawns = filter(
            is_field_black,
            product(range(size), range(pawn_row_count))
        )

        for x, y in blue_pawns:
            self.board[y][x] = Pawn(x, y, Player.BLUE)
            self.blue += 1

        white_pawns = filter(
            is_field_black,
            product(range(size), range(size - pawn_row_count, size))
        )

        for x, y in white_pawns:
            self.board[y][x] = Pawn(x, y, Player.WHITE)
            self.white += 1

        return self

    def get_pawns(self, player: Optional[Player] = None) -> List[Pawn]:
        pawns: List[Pawn] = []
        for rows in self.board:
            for field in rows:
                if isinstance(field, Pawn) and (player is None or field.player == player):
                    pawns.append(field)
        return pawns

    def is_empty(self, x: int, y: int) -> bool:
        return isinstance(self.board[y][x], Field)

    def possible_moves(self, pawn: Pawn) -> List[Move]:
        moves: List[Move] = []

        for x, y in pawn.possible_jumps(self.size):
            if self.is_empty(x, y):
                moves.append(Move(pawn, x, y))

        enemy = pawn.player.opponent()

        for (x, y), (capture_x, capture_y) in pawn.possible_captures(self.size):
            capture = self.board[capture_y][capture_x]
            if self.is_empty(x, y) and isinstance(capture, Pawn) and capture.player == enemy:
                moves.append(Move(pawn, x, y, capture))

        return moves

    def all_possible_moves(self, player: Optional[Player] = None) -> List[Move]:
        if player is None:
            player = self.player

        return list(chain.from_iterable(
            self.possible_moves(pawn) for pawn in self.get_pawns(player)
        ))

    def perform_move(self, move: Move) -> None:
        if move.captures:
            self.board[move.captures.y][move.captures.x] = move.captures.to_field()

        self.board[move.pawn.y][move.pawn.x] = move.pawn.to_field()

        self.board[move.to_y][move.to_x] = move.pawn.moved(
            move.to_x, move.to_y, self.size)

        if move.captures:
            if move.captures.player == Player.WHITE:
                self.white -= 1
            else:
                self.blue -= 1

        self.player = self.player.opponent()
        self.iterations -= 1

    def copy_and_perform_move(self, move: Move) -> 'Board':
        copy = self.copy()
        copy.perform_move(move)
        return copy

    def should_end(self) -> bool:
        possibilities = len(self.all_possible_moves())
        return self.blue == 0 or self.white == 0 or possibilities == 0 or self.iterations == 0

    def draw(self, window: "pygame.Surface") -> None:
        window.fill(WHITE)

        for row in range(self.size):
            for col in range((row+1) % 2, self.size, 2):
                y = row * FIELD_SIZE
                x = col * FIELD_SIZE
                pygame.draw.rect(window, BLACK, (x, y, FIELD_SIZE, FIELD_SIZE))

        if self._marked:
            pygame.draw.circle(window, RED,
                               (self._marked.x * FIELD_SIZE + FIELD_SIZE / 2,
                                self._marked.y * FIELD_SIZE + FIELD_SIZE / 2),
                               PIECE_SIZE + MARK_THICK, MARK_THICK)
            moves = self.possible_moves(self._marked)
            for move in moves:
                move.draw(window)

        for row in range(self.size):
            for col in range((row+1) % 2, self.size, 2):
                y = row * FIELD_SIZE
                x = col * FIELD_SIZE
                self.board[row][col].draw(window)

    def show_popup(self, window: "pygame.Surface") -> None:

        if len(self.get_pawns(Player.WHITE)) == 0:
            msg = 'Blue won!'
        elif len(self.get_pawns(Player.BLUE)) == 0:
            msg = 'White won!'
        else:
            if self.iterations == 0:
                msg = 'Draw!'
            elif self.player == Player.WHITE:
                msg = 'Blue won!'
            else:
                msg = 'White won!'

        window.fill(BLACK)
        pygame.font.init()
        pygame.display.set_caption('Game Ended!')
        my_font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = my_font.render(msg, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE // 2)
        window.blit(text_surface, text_rect)
        pygame.display.update()

    def clicked_at(self, x: int, y: int) -> None:
        field = self.board[y][x]

        if isinstance(field, Field) and self._marked != None:
            # Case 1: perform a move
            possible_moves = self.possible_moves(self._marked)
            for move in possible_moves:
                if move.to_y == y and move.to_x == x:
                    self.perform_move(move)
                    self._marked = None

        elif isinstance(field, Pawn):
            # Case 2: toggle mark
            if self.player == field.player:
                if self._marked == field:
                    self._marked = None
                else:
                    self._marked = field


EVALUATION_FUNCTION = Callable[[Board], float]
MINIMAX = Callable[[Board, int, EVALUATION_FUNCTION], float]


def ai_function(
        board: Board,
        depth: int,
        evaluation_function: EVALUATION_FUNCTION,
        minimax: MINIMAX) -> Move:

    function = max if board.player == Player.BLUE else min
    moves = board.all_possible_moves()

    best_move = function(
        moves,
        key=lambda move:  minimax(
            board.copy_and_perform_move(move),
            depth - 1, evaluation_function
        )
    )
    return best_move


class Game:
    def __init__(self, window: "pygame.Surface"):
        self.window = window
        self.board = Board.populate_with_pawns()

    def draw(self):
        if not self.board.should_end():
            self.board.draw(self.window)
        else:
            self.board.show_popup(self.window)
        pygame.display.update()

    def mouse_to_indexes(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        return (int(pos[0]//FIELD_SIZE), int(pos[1]//FIELD_SIZE))

    def clicked_at(self, pos: Tuple[int, int]):
        x, y = self.mouse_to_indexes(pos)
        self.board.clicked_at(x, y)

    @staticmethod
    def player_contra_ai(
            evaluation_funciton: EVALUATION_FUNCTION,
            minimax: MINIMAX,
            depth: int = MINIMAX_DEPTH):
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        is_running = True
        clock = pygame.time.Clock()
        game = Game(window)  # type: ignore
        game.draw()

        while is_running:
            clock.tick(FPS)

            if not game.board.should_end() and game.board.player == Player.BLUE:
                move = ai_function(game.board, depth,
                                   evaluation_funciton, minimax)
                # move = get_random_move(game.board)
                game.board.perform_move(move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    game.clicked_at(pos)

            game.draw()

        pygame.quit()

    @staticmethod
    def ai_contra_ai_with_display(
            evaluation_funciton_1: EVALUATION_FUNCTION,
            evaluation_funciton_2: EVALUATION_FUNCTION,
            minimax_1: MINIMAX,
            minimax_2: MINIMAX,
            depth_1: int,
            depth_2: int):
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        is_running = True
        clock = pygame.time.Clock()
        game = Game(window)  # type: ignore
        game.draw()

        while is_running:
            clock.tick(FPS)

            if not game.board.should_end():
                if game.board.player == Player.BLUE:
                    move = ai_function(game.board, depth_1,
                                       evaluation_funciton_1, minimax_1)
                else:
                    move = ai_function(game.board, depth_2,
                                       evaluation_funciton_2, minimax_2)
                game.board.perform_move(move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    game.clicked_at(pos)

            game.draw()

        pygame.quit()

    @staticmethod
    def ai_contra_ai(
            evaluation_funciton_1: EVALUATION_FUNCTION,
            evaluation_funciton_2: EVALUATION_FUNCTION,
            minimax_1: MINIMAX,
            minimax_2: MINIMAX,
            depth_1: int,
            depth_2: int) -> Optional[Player]:
        game = Game(None)  # type: ignore

        while True:
            if not game.board.should_end():
                if game.board.player == Player.BLUE:
                    move = ai_function(game.board, depth_1,
                                       evaluation_funciton_1, minimax_1)
                else:
                    move = ai_function(game.board, depth_2,
                                       evaluation_funciton_2, minimax_2)
                game.board.perform_move(move)
            else:
                break
        print(MAX_ITERATIONS - game.board.iterations)
        if game.board.iterations == 0:
            return None
        return game.board.player.opponent()
