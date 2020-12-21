# keyboard_listener.py
# for PyQt5-keyboard-visualizer by lutet88

import keyboard
import mouse

class KeyboardListener():
    """Keyboard Listener class."""
    def __init__(self, num_keys, reset):
        """Constructor.
        Args:
            num_keys: maximum number of keyCodes storable
            reset: keyCode for counter reset
        """
        self.keyCodes = ["" for x in range(num_keys)]
        self.pressed = [False for x in range(num_keys)]
        self.counts = [0 for x in range(num_keys)]
        self.reset = reset
        print("[KeyboardListener] registered KeyboardListener at "+str(id(self)))

    def update(self):
        """Updates keyboard and mouse input."""
        for c in range(len(self.keyCodes)):
            kc = self.keyCodes[c]
            if kc is None:
                continue
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
        """Sets a keyCode for this KeyboardListener.
        Args:
            id: index of key in self.keyCodes
            code: desired keyCode
        """
        self.keyCodes[id] = code

    def getKeyCode(self, id):
        return self.keyCodes[id]

    def addCount(self, id):
        print(id)
        self.counts[id] += 1;
