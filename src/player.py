# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name} is currently in the {self.current_room}"

    def move(self, direction):
        if self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
        else:
            print('Nothing over here')