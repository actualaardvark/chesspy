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
    print("   A B C D E F G H ")
    x = 8
    for i in rows:
        rowtoprint=str(x) + " "
        for j in i:
            rowtoprint += "|" + j
        rowtoprint += "|"
        print(rowtoprint)
        x-=1

checkmate = False

while checkmate == False:
    command = input("Chess Input> ")
    command = command.lower()
    if command == "check":
        render()
    elif command[:4] == "move":
        piecelocation = ""
        targetlocation = ""
        if command[5:][:2] and command[8:][:2]:
            piecelocation = command[5:][:2]
            targetlocation = command[8:][:2]
        else:
            piecelocation = input("Piece Select> ")
            targetlocation = input("Target Select> ")
        column = lettertonumber[piecelocation[0]]
        row = 8 - int(piecelocation[1])
        print(row, column)
        selectedpiece = rows[row][column]
        print(selectedpiece)
        validmoves = []
        letters = list(lettertonumber.keys())
        if selectedpiece == "♟︎":
            if rows[row - 1][column] not in whitepieces and rows[row - 1][column] not in blackpieces:
                validmoves.append(letters[column] + str(8 - (row - 1)))
            if row == 6 and rows[row - 2][column] not in whitepieces and rows[row - 2][column] not in blackpieces:
                validmoves.append(letters[column] + str(8 - (row - 2)))
        print(validmoves)
        if targetlocation in validmoves:
            targetcolumn = lettertonumber[targetlocation[0]]
            targetrow = 8 - int(targetlocation[1])
            rows[targetrow][targetcolumn] = selectedpiece
            rows[row][column] = " "
        else:
            print("Invalid Move")
        render()

# def movepiece():
#     validmoves = []
#     piecelocation = input("Piece Coordinate: ")
#     movelocation = input("Movement Coordinate: ")
#     print(piecelocation[1])
#     selectedpiece = rows[8 - int(piecelocation[1])][lettertonumber[piecelocation[0]]]
#     if selectedpiece == "♟︎":
#         if rows[8 - int(piecelocation[1]) - 1][lettertonumber[piecelocation[0]]] not in blackpieces and rows[8 - int(piecelocation[1]) - 1][lettertonumber[piecelocation[0]]] not in whitepieces:
#             validmoves.append(str(piecelocation[0] + str(int(piecelocation[1]) + 1)))
#         if piecelocation[1] == str(2):
#             validmoves.append(str(piecelocation[0] + str(int(piecelocation[1]) + 2)))
#         if 0 <= lettertonumber[piecelocation[0]] < len(rows[8 - int(piecelocation[1]) - 1]):
#             if rows[8 - int(piecelocation[1]) - 1][lettertonumber[piecelocation[0]]] in blackpieces:
#                 validmoves.append(str(list(lettertonumber.keys())[lettertonumber[piecelocation[0]] + 1]) + str(int(piecelocation[1]) + 1))
#         if rows[8 - int(piecelocation[1]) - 1][lettertonumber[piecelocation[0]] - 1] in blackpieces and lettertonumber[piecelocation[0]] - 1 != -1:
#             validmoves.append(str(list(lettertonumber.keys())[lettertonumber[piecelocation[0]] - 1]) + str(int(piecelocation[1]) + 1))
#     if selectedpiece == " ":
#         movepiece()
#     if movelocation in validmoves:
#         rows[8 - int(movelocation[1])][lettertonumber[movelocation[0]]] = selectedpiece
#         rows[8 - int(piecelocation[1])][lettertonumber[piecelocation[0]]] = " "
#     else:
#         print("Invalid Move")
#         movepiece()
#     print(selectedpiece)
# while True:
#     movepiece()
#     render()