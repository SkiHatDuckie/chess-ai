def getchessboard():
  def getfen():
    x=list(input())
    return x

  fen=getfen()
  fenlength = len(fen)
  x=0
  line = 0
  chessboard=[[],[],[],[],[],[],[],[]]
  while x<fenlength:
    if fen[x].isdigit():
      fenNum=int(fen[x])
      i=0
      while i < fenNum:
        chessboard[line].append("")
        i=i+1
      x=x+1
    elif fen[x] == "/":
      x=x+1
      line = line + 1
    else:
      chessboard[line].append(fen[x])
      x=x+1
  return chessboard
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQNR

#8/8/8/8/8/8/8/8
chessboard=getchessboard()
for i in chessboard:
  print(i)

def searchpos(pos,chessboard):
  pos=list(pos)
  if pos[0] == "a":
    x=0
  elif pos[0] == "b":
    x=1
  elif pos[0] == "c":
    x=2
  elif pos[0] == "d":
    x=3
  elif pos[0] == "e":
    x=4
  elif pos[0] == "f":
    x=5
  elif pos[0] == "g":
    x=6
  elif pos[0] == "h":
    x=7
  if pos[1] == "8":
    y=0
  elif pos[1] == "7":
    y=1
  elif pos[1] == "6":
    y=2
  elif pos[1] == "5":
    y=3
  elif pos[1] == "4":
    y=4
  elif pos[1] == "3":
    y=5
  elif pos[1] == "2":
    y=6
  elif pos[1] == "1":
    y=7
  return chessboard[y][x]
def case(x):
  uppercase = list("QWERTYUIOPASDFGHJKLZXCVBNM")
  lowercase = list("qwertyuiopasdfghjklzxcvbnm")
  if x in uppercase:
    return "uppercase"
  elif x in lowercase:
    return "lowercase"
  else:
    return "none"
def legality(startpos,endpos,board):
  x=searchpos(startpos,board)
  y=searchpos(endpos,board)
  if case(x)==case(y) or case(x)=="none":
    return False
  else:
    if x.lower == "r" :
    elif x.lower = "b":
    elif x.lower = "n":
    elif x.lower = "k":
    elif x.lower = "q":
      
    return True

# def move(startpos,endpos):
#   if legality == True
