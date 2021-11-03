# kvgui.py (main GUI script and controller, for now)
# for PyQt5-keyboard-visualizer by lutet88

import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtGui import QPixmap, QFont, QFontDatabase
import config_parser
import keyboard_listener

version = "0.0.3a"


def createApplication():
    return QApplication(sys.argv)


def switchModes(mode):
    # gets numeric value else default 0
    return {"none":0, "count":1, "name":2, "both":3}.get(mode.lower(), 0)


class MainGUI(QMainWindow):
    # initialize GUI
    def __init__(self, config, app, *args, **kwargs):
        print("[KVGUI] Initializing... (version v{version})".format(version=version))
        super(MainGUI, self).__init__(*args, **kwargs)
        print("[KVGUI] QMainWindow initialized.")
        self.app = app
        self.initVars(config)
        self.initGUI()
        self.createFonts()
        self.initKeyboard()
        if cps_enable:
            self.initCPS()
        print("[KVGUI] GUI init complete. Application Launching...")
        self.initTimer()

    def initVars(self, config):
        global tilesize, width, height, num_keys, keys, keyimage, keyimage_dark, keyimage_maps, \
            font, fontsize, fontcolor, backgroundcolor, displaymode, resetkey, pollingrate, cps_enable, \
            cps_x, cps_y
        v = config_parser.loadConfig(config)
        tilesize, width, height = v["tilesize"], v["windowwidth"], v["windowheight"]
        num_keys = width * height
        keys, keyimage, keyimage_dark = v["keys"], v["keyimage"], v["keyimage_dark"]
        keyimage_maps = [QPixmap(keyimage).scaled(tilesize, tilesize), QPixmap(keyimage_dark).scaled(tilesize, tilesize)]
        font, fontsize, fontcolor = v["font"], v["fontsize"], v["fontcolor"]
        backgroundcolor = v["backgroundcolor"]
        displaymode = switchModes(v["displaymode"])
        resetkey = v["resetkey"]
        pollingrate = 1000 / v["pollingratehz"]
        cps_enable = v["cps-enable"]
        cps_x = v["cps-x"]
        cps_y = v["cps-y"]

    def initGUI(self):
        self.setWindowTitle("keyboard visualizer v{version}".format(version=version))
        self.setDimensions(tilesize * width, tilesize * height)
        self.setBGColor(backgroundcolor)

    def initKeyboard(self):
        self.keylabels = [None for i in range(len(keys))]
        self.textlabels = [None for i in range(len(keys))]
        self.kl = keyboard_listener.KeyboardListener(len(keys), resetkey)
        self.addKeys()

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(pollingrate)
        print("[KVGUI] Refresh timer started with interval "+str(pollingrate)+"ms")

    def createFonts(self):
        text_font = QFontDatabase.addApplicationFont(font)
        self.text_font = QFont(QFontDatabase.applicationFontFamilies(text_font)[0], fontsize)

    def initCPS(self):
        cps = QLabel(self)
        cps.setGeometry(0, 0, tilesize, tilesize)
        cps.move(tilesize * cps_x, tilesize * cps_y)
        cps.setAlignment(Qt.AlignCenter)
        cps.setText("0")
        cps.setFont(self.text_font)
        cps.setStyleSheet("background-color: rgba(0,0,0,0); color : "+fontcolor+";")
        self.cps = cps
        print("[KVGUI] CPS system initialized")

    def update(self):
        self.timer.stop()
        self.kl.update()
        self.updateKeys()
        if cps_enable:
            self.updateCPS()
        self.show()
        self.timer.start(pollingrate)

    def setBGColor(self, color):
        self.setStyleSheet("background-color: " + color + ";")

    def setDimensions(self, width, height):
        self.setGeometry(100, 100, width, height)

    def addKeys(self):
        for id in range(len(keys)):
            self.addKey(id, keys[id])

    def addKey(self, id, key):
        if key["enabled"]:
            # enable keycode
            self.kl.setKeyCode(id, str(key["keyCode"]))

            # image element (background)
            q = QLabel(self)
            q.setGeometry(0, 0, tilesize, tilesize)
            q.move(tilesize * key["x"], tilesize * key["y"])
            q.setPixmap(QPixmap(keyimage).scaled(tilesize, tilesize))

            # text element
            t = QLabel(self)
            t.setGeometry(0, 0, tilesize, tilesize)
            t.move(tilesize * key["x"], tilesize * key["y"])
            t.setAlignment(Qt.AlignCenter)
            t.setText("")
            t.setFont(self.text_font)
            t.setStyleSheet("background-color: rgba(0,0,0,0); color : "+fontcolor+";")

            # add to instance
            self.keylabels[id] = q
            self.textlabels[id] = t
        else:
            self.kl.setKeyCode(id, None)

    def updateKeys(self):
        for id in range(len(keys)):
            self.updateKey(id, keys[id])

    def updateKey(self, id, key):
        if key["enabled"]:
            q = self.keylabels[id]
            q.setPixmap(keyimage_maps[1 if self.kl.pressed[id] else 0])
            text = str(key["name"]) if displaymode & 0b10 else ""
            text += "\n" if displaymode == 0b11 else ""
            text += str(self.kl.counts[id]) if displaymode & 0b01 else ""
            self.textlabels[id].setText(text)

    def updateCPS(self):
        self.cps.setText(f"{self.kl.updateCPS()}")

    def closeEvent(self, event):
        print("[KVGUI] Stopping...")
        self.kl.stopListening()
        event.accept()
        self.close()
        self.app.quit()
        exit()


if __name__ == "__main__":
    # test MainGUI
    app = createApplication()
    m = MainGUI("config/config.yml")
    app.exec()
