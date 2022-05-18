#The function for that our player can't go through the decor.
def collision(decor_x, decor_y, player_x, player_y):
    decor_bottom = decor_y+100
    decor_top = decor_y -50
    decor_left = decor_x -100
    decor_right = decor_x + 100
    print(decor_bottom, decor_top, decor_left, decor_right)
    if decor_left < player_x < decor_right:
        if decor_bottom > player_y > decor_top:
            return True
    # In the another collision cases
    return False

def go(Px, Py, Dx, Dy):
    return collision(Px, Py,Dx,Dy)