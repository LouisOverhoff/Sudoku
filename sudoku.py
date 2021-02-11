domain = {1,2,3,4,5,6,7,8,9} #Set für leere Felder (alle Zahlen die dort vorkommen können)
sudoku = [] #Liste für das Sudoku (beinhaltet alle Zahlen)
# Eine Liste ist geordnet, ein Set nicht.
# Auf eine Liste kann man mit einem Index zugreifen z.B. liste[0]
# Bei einem Set lässt sich nur überprüfen, ob ein Element enthalten ist.bin

def setupSudoku(): #Erstellt Sudoko und legt alle Zahlen an
    # Beginn
    for i in range(0,81): # 81 ist nicht mehr dabei
        sudoku.append(domain) #Setzt die Zahlen 1-9 in jedes Feld = Leer
    # Ende
    # print(f"Meldung 1: sudoku[2] {sudoku[2]}")
    setValueAtPosition(1,0,1) #Setzt die Zahl 1 in das 2. Feld
    setValueAtPosition(2,0,4)
    # print(f"Meldung 2: sudoku[2] {sudoku[2]}")
    setValueAtPosition(8,0,5)
    setValueAtPosition(3,1,9)
    setValueAtPosition(4,1,8)
    setValueAtPosition(5,1,7)
    setValueAtPosition(3,2,5)
    setValueAtPosition(6,2,8)
    setValueAtPosition(8,2,6)
    setValueAtPosition(4,3,1)
    setValueAtPosition(5,3,6)
    setValueAtPosition(1,4,8)
    setValueAtPosition(2,4,2)
    setValueAtPosition(3,4,4)
    setValueAtPosition(7,4,5)
    setValueAtPosition(5,5,5)
    setValueAtPosition(6,5,4)
    setValueAtPosition(7,5,7)
    setValueAtPosition(8,5,8)
    setValueAtPosition(1,6,6)
    setValueAtPosition(2,6,1)
    setValueAtPosition(4,6,5)
    setValueAtPosition(6,6,3)
    setValueAtPosition(7,6,4)
    setValueAtPosition(2,7,8)
    setValueAtPosition(3,7,1)
    setValueAtPosition(4,7,2)
    setValueAtPosition(6,7,5)
    setValueAtPosition(0,8,5)
    setValueAtPosition(1,8,4)
    setValueAtPosition(2,8,7)
    setValueAtPosition(4,8,9)


def setValueAtPosition(x,y,value): #Setzt eine Zahl in ein bestimmtes Sudoku Feld ein
    sudoku[y*9+x] = value

def getValueAtPosition(x,y): #Wählt eine bestimmte Zahl aus dem Sudoku aus
    return sudoku[y*9+x]


def printSudoku(): #Zeigt das Sudoku visuell an
    for i in range(0,81):
        if i % 9 == 0:
            print()
        if isinstance(sudoku[i], int):
            print(f" {sudoku[i]} ", end="") #Zeigt die dazugehörige Zahl in die Felder mit einem Integer an
        else:
            print(f" - ", end="")  #Zeigt '-' in jedes Feld das kein Integer ist an
    print()

def rowRule():
  for y in range(9):
      rownumber = set()
      for x in range(9):
        if isinstance(getValueAtPosition(y,x),int):
          rownumber.add(getValueAtPosition(y,x))
      for x in range(9):
        if not isinstance(getValueAtPosition(y,x),int):
          setValueAtPosition(y,x, getValueAtPosition(y,x)-rownumber)

def columnRule():
  for y in range(9):
    columnnumber = set()
    for x in range(9):
      if isinstance(getValueAtPosition(x,y),int):
        columnnumber.add(getValueAtPosition(x,y))
    for x in range(9):
      if not isinstance(getValueAtPosition(x,y),int):
        setValueAtPosition(x,y, getValueAtPosition(x,y)-columnnumber)

def boxRule():
  for x in range(3):
    for y in range(3):
      boxnumber = set()
      for xx in range(3):
        for yy in range(3):
          if isinstance(getValueAtPosition(yy+y*3,xx+x*3),int):
            boxnumber.add(getValueAtPosition(yy+y*3,xx+x*3))
      for xx in range(3):
        for yy in range(3):
          if not isinstance(getValueAtPosition(yy+y*3,xx+x*3),int):
            setValueAtPosition(yy+y*3,xx+x*3, getValueAtPosition(yy+y*3,xx+x*3)-boxnumber)
            
def soloveSudoku():
  changes = False
  for x in range(81):
    if isinstance(sudoku[x],set):
      if len(sudoku[x]) == 1:
        sudoku[x] = sudoku[x].pop()
        changes = True

  return changes
 
def playSudoku():
  printSudoku()
  changes = True
  while changes:
    boxRule()
    rowRule()
    columnRule()
    changes = soloveSudoku()
    printSudoku()

setupSudoku()
playSudoku()
