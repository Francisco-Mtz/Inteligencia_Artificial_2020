import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Aspiradora")
wn.setup(700 , 700)

class Pen1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Pen2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Pen3(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

class Pen4(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)

class Pen5(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Pen6(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        

def iniciar_lab(nivel , x , y):
    count=0
    for fila in range(len(nivel)):
        if fila == x-1 or fila == x or fila == x+1 or x == 0:
            for column in range(len(nivel[fila])):
                if column == y-1 or column == y or column == y+1 or y == 0:
                    letra_x = nivel[fila][column]
                    screen_x = -288 + (column * 24)
                    screen_y = 288 - (fila * 24)

                    if letra_x == "X":
                        pen1.goto(screen_x , screen_y)
                        pen1.stamp()

                    if letra_x == "_":
                        pen2.goto(screen_x , screen_y)
                        pen2.stamp()
                    
                    if letra_x == "-":
                        pen6.goto(screen_x , screen_y)
                        pen6.stamp()
                    
                    if letra_x == "Z":
                        pen3.goto(screen_x , screen_y)
                        pen3.stamp()

                    if letra_x == "A":
                        pen4.goto(screen_x , screen_y)
                        pen4.stamp()
                    
                    if letra_x == "B":
                        pen5.goto(screen_x , screen_y)
                        pen5.stamp()
                        count = count + 1
    if count == 0:
        return True
    else:
        return False
    
def mover_aspiradora(nivel , x , y):
    if (nivel[x-1][y] == "X" or nivel[x-1][y] == '-'):
        if (nivel[x][y+1] != 'X' and nivel[x][y+1] != '-'):
            nivel[x][y+1]='A'
            nivel[x][y]="-"
            y = y + 1
            return nivel , x , y
        else:
            if (nivel[x][y+1] == 'X' or nivel[x][y+1] == '-'):
                if(nivel[x+1][y] != 'X' and nivel[x+1][y] != '-'):
                    nivel[x+1][y]='A'
                    nivel[x][y]="-"
                    x = x + 1
                    return nivel , x , y
                else:
                    if (nivel[x+1][y] == 'X' or nivel[x+1][y] == '-'):
                        if (nivel[x][y-1] != 'X' and nivel[x][y-1] != '-'):
                            nivel[x][y-1]='A'
                            nivel[x][y]="-"
                            y = y - 1
                            return nivel , x , y
            
    else:
        if (nivel[x][y+1] == '-'):
            if(nivel[x+1][y] == 'X' or nivel[x+1][y] == '-'):
                if(nivel[x][y-1] != 'X' and nivel[x][y-1] != '-'):
                    nivel[x][y-1]='A'
                    nivel[x][y]="-"
                    y = y - 1
                    return nivel , x , y
                else:
                    if(nivel[x][y-1] == 'X' or nivel[x][y-1] == '-'):
                        if(nivel[x-1][y] != 'X' and nivel[x-1][y] != '-'):
                            nivel[x-1][y]='A'
                            nivel[x][y]="-"
                            x = x - 1
                            return nivel , x , y
            else:
                if(nivel[x+1][y] != 'X' and nivel[x+1][y] != '-'):
                    nivel[x+1][y]='A'
                    nivel[x][y]="-"
                    x = x + 1
                return nivel , x , y
            return nivel , x , y
        if (nivel[x+1][y] == '-'):
            if(nivel[x][y-1] == 'X' or nivel[x][y-1] == '-'):
                if(nivel[x-1][y] != 'X' and nivel[x-1][y] != '-'):
                    nivel[x-1][y]='A'
                    nivel[x][y]="-"
                    x = x - 1
                    return nivel , x , y
            else:
                if(nivel[x][y-1] != 'X' and nivel[x][y-1] != '-'):
                    nivel[x][y-1]='A'
                    nivel[x][y]="-"
                    y = y - 1
                    return nivel , x , y
            return nivel , x , y
        if (nivel[x][y-1] == '-'):
            if(nivel[x-1][y] != 'X' and nivel[x-1][y] != '-'):
                nivel[x-1][y]='A'
                nivel[x][y]="-"
                x = x - 1
                return nivel , x , y
            return nivel , x , y
    return nivel , x , y



pen1 = Pen1()
pen2 = Pen2()
pen3 = Pen3()
pen4 = Pen4()
pen5 = Pen5()
pen6 = Pen6()


mapa0 = [['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'X', 'A', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z']]

mapa1 = [['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', '', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'X', 'A', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'B', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', 'B','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', 'B', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', 'B', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','B', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', 'B', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','B', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'B', '_','_', 'B', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', 'B', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'B', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'B', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z']]

mapa2 = [['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'X', 'A', 'X', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','B', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', 'X', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', 'B','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', 'B','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', 'B', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','B', 'X', 'X', '_', '_','_', '_', 'B', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','B', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','B', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', 'B', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','B', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','B', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z']]

mapa3 = [['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'X', 'A', 'X', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','B', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', 'X', 'B','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', 'X', 'X','X', '_', '_', 'X', 'X','_', 'X', 'X', '_', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', '_','_', 'X', 'X', '_', '_','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', 'B','_', 'X', 'X', 'B', '_','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', 'B', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', '_','_', 'B', '_', '_', '_','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', '_','_', '_', '_', '_', '_','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', 'X', '_','_', 'X', 'X', '_', '_','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','_', '_', '_', 'X', 'B','_', 'X', 'X', '_', 'B','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'B', '_', 'X','_', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', 'X','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', 'X', 'X', 'B', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z']]

mapa = [['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'X', 'A', '_', 'X','X', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','X', '_', 'B', '_', '_','_', '_', 'X', '_', '_','X', 'X', 'X', 'X', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','X', '_', 'X', '_', '_','X', '_', 'X', '_', '_','X', '_', 'B', 'X', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','X', 'B', 'X', '_', '_','X', 'B', 'X', 'B', '_','X', '_', '_', 'X', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','X', 'X', 'X', '_', '_','X', 'X', 'X', '_', '_','X', '_', 'X', 'X', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'B', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', 'B','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', 'B', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', 'B','_', '_', '_', '_', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'],
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', 'X','X', 'X', 'X', 'X', 'X','X', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', 'B', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', '_', '_','_', '_', '_', 'B', '_','_', '_', '_', 'X', 'Z'], 
        ['Z', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'Z'], 
        ['Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z','Z', 'Z', 'Z', 'Z', 'Z']]



pasos = 0
x = 2
y = 2

limpio=iniciar_lab(mapa , 0 , 0)

while True :
    pasos = pasos + 1
    mapa , x , y = mover_aspiradora(mapa , x , y)

    limpio=iniciar_lab(mapa , x , y)
    print(pasos,"\n")
    print(x,"\n",y)
    if pasos == 500:
        break

turtle.done()