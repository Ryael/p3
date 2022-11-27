"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the logic dictating everything concerning the player.
"""


from world import path_at


class Player:
    """
    The core class for the player character within the world.
    """
    def __init__(self):
        """
        Creates an instance of the player character and assigns x,y coordinates
        to them to represent their position within the world.
        """
        self.x_pos = 2
        self.y_pos = 0
        self.moved = True

    def move(self, dx_pos, dy_pos):
        """
        The move method is called using named parameteres, these parameteres
        are from math and represent changes in x and y values. This method
        accepts a change in the x and/or y directions. It moves the player
        if the path exists, and doesn't if the path doesn't exist. It also
        checks if the path is either blocked or locked.
        """
        path = valid_move(self, dx_pos, dy_pos)

        if path is not None:
            if path.block or path.lock:
                print(path.desc)
            else:
                self.x_pos += dx_pos
                self.y_pos += dy_pos
                self.moved = True
                return

        self.moved = False
        print("""
        You find yourself unable to move in that direction.
        """)

    def move_north(self):
        """
        This method shows the amount of the change in the
        y-direction (negative).
        """
        self.move(dx_pos=0, dy_pos=-1)

    def move_south(self):
        """
        This method shows the amount of the change in the
        y-direction (positive).
        """
        self.move(dx_pos=0, dy_pos=1)

    def move_west(self):
        """
        This method shows the amount of the change in the
        x-direction (negative).
        """
        self.move(dx_pos=-1, dy_pos=0)

    def move_east(self):
        """
        This method shows the amount of the change in the
        x-direction (positive).
        """
        self.move(dx_pos=1, dy_pos=0)


def valid_move(player, x_pos, y_pos):
    """
    Checks if the path being moved into exists.
    """
    x_dest = player.x_pos + x_pos
    y_dest = player.y_pos + y_pos
    path = path_at(player.x_pos, player.y_pos, x_dest, y_dest)

    if path is not None:
        return path

    return None
