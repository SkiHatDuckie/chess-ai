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


def searchpos(pos,chessboard):
  pos=list(pos)
  cols = "abcdefgh"
  rows = "87654321"
  x = pos[0] in cols
  y = pos[1] in rows

  return chessboard[y][x]


def case(x):
  uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
  lowercase = "qwertyuiopasdfghjklzxcvbnm"
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
        pass
    elif x.lower == "b":
        pass
    elif x.lower == "n":
        pass
    elif x.lower == "k":
        pass
    elif x.lower == "q":
        pass
      
    return True

if __name__ == "__main__":
    #rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQNR

    #8/8/8/8/8/8/8/8
    chessboard=getchessboard()
    for i in chessboard:
        print(i)