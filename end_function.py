#The function that end the game when the object is touched

def touch(decor_x, decor_y, player_x, player_y):
    decor_bottom = decor_y+100
    decor_top = decor_y -50
    decor_left = decor_x -50
    decor_right = decor_x + 100
    if decor_left < player_x < decor_right:
        if decor_bottom > player_y > decor_top:
            return True
    # In all the another cases where it is not touched
    return False

def go(Px, Py, Dx, Dy):
    return touch(Px, Py,Dx,Dy)