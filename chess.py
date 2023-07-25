rows = [["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"], ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], ["♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎"], ["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"]]
lettertonumber={
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
def render():
    for i in rows:
        rowtoprint=""
        for j in i:
            rowtoprint += "|" + j
        rowtoprint += "|"
        print(rowtoprint)
def movepiece():
    piecelocation = input("Piece Coordinate: ")
    movelocation = input("Movement Coordinate: ")


render()