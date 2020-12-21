# keyboard_visualizer.py (main application script)
# for PyQt5-keyboard-visualizer by lutet88

# use actual main script (kvgui.py)
import kvgui

# create application
app = kvgui.createApplication()

# define PyQt5 window
window = kvgui.MainGUI()

# start application
app.exec_()
