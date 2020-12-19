import keyboard

class KeyboardListener():
    def __init__(self, num_keys):
        self.keyCodes = ["" for x in range(num_keys)]
        self.pressed = [False for x in range(num_keys)]
        self.counts = [0 for x in range(num_keys)]

    def update(self):
        for c in range(len(self.keyCodes)):
            newstate = keyboard.is_pressed(self.keyCodes[c])
            if self.pressed[c] != newstate and newstate is True:
                self.counts[c] += 1
            self.pressed[c] = newstate

    def getStates(self):
        return self.pressed

    def setKeyCode(self, id, code):
        self.keyCodes[id] = code

    def getKeyCode(self, id):
        return self.keyCodes[id]
