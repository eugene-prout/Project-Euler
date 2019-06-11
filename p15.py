moves = 0

def route(x,y):
    global moves
    print(x,y)
    if (x == 1) ^ (y == 1):
        moves += 1
        return True

    moveLeft = False
    moveUp = False

    if x > 0:
        moveLeft = True
    if y > 0:
        moveUp = True

    if moveLeft:
        
        route(x-1, y) 

    if moveUp:
        route(x, y-1)

route(21,21)
print(moves)
