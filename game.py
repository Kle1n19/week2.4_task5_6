class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
    
    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return self.description
    
    def set_character(self, new_character):
        self.character = new_character
        
    def get_character(self):
        return self.character
    
    def set_item(self, new_item):
        self.item = new_item
        
    def get_item(self):
        return self.item
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    
    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print("The " + room.name + " is " + direction + " of here.")




class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        self.defeated = 0

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, item):
        if item == self.weakness:
            print("You fend " + self.name + " off with the " + item)
            self.defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def get_defeated(self):
        return self.defeated


class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def describe(self):
        print("You see a " + self.description)
