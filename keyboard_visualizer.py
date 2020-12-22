# keyboard_visualizer.py (main application script)
# for PyQt5-keyboard-visualizer by lutet88

# use actual main script (kvgui.py)
import kvgui

# create application
app = kvgui.createApplication()

# define PyQt5 window
config = "config2.yml"
window = kvgui.MainGUI(config)

# start application
app.exec_()
