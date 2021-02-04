domain = {1,2,3,4,5,6,7,8,9} #Set für leere Felder (alle Zahlen die dort vorkommen können)
sudoku = [] #Liste für das Sudoku (beinhaltet alle Zahlen)
# Eine Liste ist geordnet, ein Set nicht.
# Auf eine Liste kann man mit einem Index zugreifen z.B. liste[0]
# Bei einem Set lässt sich nur überprüfen, ob ein Element enthalten ist.bin

def setupSudoku(): #Erstellt unser Sudoko und legt alle Zahlen an
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




def Zeilenregel():
    zahlen = set()
    for i in range(9):
        if isinstance(getValueAtPosition(i,0),int): #Fügt alle Integer in das Zahlen Set
            zahlen.add(getValueAtPosition(i,0))
    #print(zahlen)

def Spaltenregel():
    Spaltenzahlen = set()
    for k in range(9):
        if isinstance(getValueAtPosition(0,k),int):
            Spaltenzahlen.add(getValueAtPosition(0,k))
    #print(Spaltenzahlen)

def Kastenregel(): #Setzt die Kastenregel in Kraft für jedes Feld
  for xx in range(3):
   for yy in range(3):
      Kastenzahl = set()
      for x in range(3):
        for y in range(3):
          # print(f"Variablen l={l} und o={o}")
          if isinstance(getValueAtPosition(yy*3+x,xx*3+y),int):
            Kastenzahl.add(getValueAtPosition(yy*3+x,xx*3+y))
            #print(f"Ausgabe Kastenregel: {Kastenzahl}")
      for x in range(3):
        for y in range(3):
          if not isinstance(getValueAtPosition(yy*3+x,xx*3+y),int):
            setValueAtPosition(yy*3+x,xx*3+y, getValueAtPosition(yy*3+x,xx*3+y)-Kastenzahl)
            
def Loesung():
  for s in range(81):
    if isinstance(sudoku[s],set):
      if len(sudoku[s]) == 1:
        sudoku[s] = list(sudoku[s])[0]

def playSudoku():
  x = 1
  sudokutest1 = 0
  sudokutest2 = 1
  botschritt = 0
  while x == 1:
    while sudokutest1 != sudokutest2 :
      sudokutest1 = list(sudoku)
      Kastenregel()
      Zeilenregel()
      Spaltenregel()
      Loesung()
      sudokutest2 = list(sudoku)
      if sudokutest1 == sudokutest2:
        break
      botschritt = botschritt + 1
      print(f'Bot Schritt: {botschritt}')
      printSudoku()
      print('_____________________________________________')
      ende = 0
      for i in range(81):
        if isinstance(sudoku[i],int):
          ende += 1
      if ende == 81:
        x = 0
        print(f'Bot konnte das Sudoku nach {botschritt} Schritten lösen')
        break
    if sudokutest1 == sudokutest2: 
      print(f'Bot konnte das Sudoku nach {botschritt} Schritten nicht lösen')
      x = 0

playSudoku()