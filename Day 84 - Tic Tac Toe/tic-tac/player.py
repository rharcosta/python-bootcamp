from typing import NamedTuple


class Player(NamedTuple):
    label: str  # X or O
    color: str


DEFAULT_PLAYERS = (Player(label="X", color="blue"), Player(label="O", color="green"))
