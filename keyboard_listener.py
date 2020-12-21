import keyboard
import mouse

class KeyboardListener():
    def __init__(self, num_keys, reset):
        self.keyCodes = ["" for x in range(num_keys)]
        self.pressed = [False for x in range(num_keys)]
        self.counts = [0 for x in range(num_keys)]
        self.reset = reset

    def update(self):
       #mouse._MouseListener.process()
        #print(self.keyCodes, self.pressed)
        for c in range(len(self.keyCodes)):
            kc = self.keyCodes[c]
            if "mouse_" in kc:
                newstate = mouse.is_pressed(kc.replace("mouse_", ""))
            else:
                newstate = keyboard.is_pressed(kc)
            if self.pressed[c] != newstate and newstate is True:
                self.counts[c] += 1
            self.pressed[c] = newstate
            if keyboard.is_pressed(self.reset):
                self.counts = [0 for x in range(len(self.keyCodes))]

    def getStates(self):
        return self.pressed

    def setKeyCode(self, id, code):
        self.keyCodes[id] = code

    def getKeyCode(self, id):
        return self.keyCodes[id]

    def addCount(self, id):
        print(id)
        self.counts[id] += 1;
