# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} is currently in the {self.current_room}"

    def move(self, direction):
        if direction not in ['n', 's', 'e', 'w']:
            print('Incorrect movement direction. Requires: n, s, e, w')
        elif self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
        else:
            print('Nothing over here')

    def get(self, item):
        items_names = [i.name for i in self.current_room.items]
        if item in items_names:
            idx = items_names.index(item)
            # SETS INSTANCE OF ITEM IN current_room.items
            item = self.current_room.items[idx]
            # ADDS TO PLAYER INVENTORY
            self.inventory.append(item)
            # REMOVES FROM CURRENT ROOM
            self.current_room.items.remove(item)
            # PRINTS "PICKED UP" MESSAGE
            item.on_take()
        else:
            print(f"{item} not available to pick up")

    def drop(self, item):
        inventory_names = [i.name for i in self.inventory]
        if item in inventory_names:
            idx = inventory_names.index(item)
            item = self.inventory[idx]
            self.inventory.remove(item)
            self.current_room.items.append(item)
            item.on_drop()
        else:
            print(f"{item} not in inventory")

    def get_inventory(self):
        print("Inventory:")
        for i in self.inventory:
            print(f"{i.name} - {i.description}")
