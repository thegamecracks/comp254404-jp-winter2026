from typing import NamedTuple, cast


class GameEntry(NamedTuple):
    name: str
    score: int

    def __str__(self) -> str:
        return f"{self.name}:{self.score}"


class Scoreboard:
    num_entries: int
    board: list[GameEntry | None]

    def __init__(self, capacity: int) -> None:
        self.num_entries = 0
        self.board = [None] * capacity

    def __repr__(self) -> str:
        return f"<{type(self).__name__} board={self.board} num_entries={self.num_entries}>"

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self.board))}]"

    def add(self, new: GameEntry, /) -> None:
        board = cast(list[GameEntry], self.board)

        # Is the new entry really a high score?
        if (
            self.num_entries >= len(board)
            and new.score <= board[self.num_entries - 1].score
        ):
            return

        if self.num_entries < len(board):
            self.num_entries += 1

        # Shift any lower scores rightward to make room for the new entry
        i = self.num_entries - 1
        while i > 0 and board[i - 1].score < new.score:
            board[i] = board[i - 1]
            i -= 1

        board[i] = new

    def remove(self, i: int, /) -> GameEntry:
        board = cast(list[GameEntry], self.board)

        if i < 0 or i > self.num_entries:
            raise IndexError(f"Index {i} out of range")

        entry = board[i]
        for j in range(i, self.num_entries - 1):
            board[j] = board[j + 1]

        self.board[self.num_entries - 1] = None
        self.num_entries -= 1

        return entry


def main() -> None:
    scoreboard = Scoreboard(5)
    names = ["Rob", "Mike", "Rose", "Jill", "Jack", "Anna", "Paul", "Bob"]
    scores = [750, 1105, 590, 740, 510, 660, 720, 400]
    entries = [GameEntry(name, score) for name, score in zip(names, scores)]

    for e in entries:
        print("Adding", e)
        scoreboard.add(e)
        print(" Scoreboard:", scoreboard)

    for i in (3, 0, 1, 0):
        print(f"Removing score at index {i}")
        print(f" {scoreboard.remove(i)}")
        print(f" {scoreboard}")


if __name__ == "__main__":
    main()
