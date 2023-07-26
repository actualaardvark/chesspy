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
blackpieces=["♙", "♖", "♘", "♗", "♕", "♔"]
whitepieces=["♟︎", "♜", "♞", "♝", "♚", "♛"]
def render():
    for i in rows:
        rowtoprint=""
        for j in i:
            rowtoprint += "|" + j
        rowtoprint += "|"
        print(rowtoprint)

def movepiece():
    validmoves = []
    piecelocation = input("Piece Coordinate: ")
    movelocation = input("Movement Coordinate: ")
    print(piecelocation[1])
    selectedpiece = rows[8 - int(piecelocation[1])][lettertonumber[piecelocation[0]]]
    if selectedpiece == "♟︎":
        if rows[8 - int(piecelocation[1]) - 1][lettertonumber[piecelocation[0]]] not in blackpieces and rows[8 - int(piecelocation[1]) - 1][lettertonumber[piecelocation[0]]] not in whitepieces:
            validmoves.append(str(piecelocation[0] + str(int(piecelocation[1]) + 1)))
            print(validmoves)
        if piecelocation[1] == str(2):
            validmoves.append(str(piecelocation[0] + str(int(piecelocation[1]) + 2)))
            print(validmoves)
    if selectedpiece == " ":
        print("Invalid Piece")
        movepiece()
    if movelocation in validmoves:
        rows[8 - int(movelocation[1])][lettertonumber[movelocation[0]]] = selectedpiece
        rows[8 - int(piecelocation[1])][lettertonumber[piecelocation[0]]] = " "
    else:
        print("Invalid Move")
        movepiece()
    print(selectedpiece)
while True:
    movepiece()
    render()