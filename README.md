# pyQt5-keypress-visualizer
simple keypress visualizer made with pyQt

originally designed for me to practice pyQt5 skills
now I use it occasionally for recordings

## dependencies
```bash
pip install keyboard mouse PySide6 pyyaml
```

## how to use
1. configure `config/config.yml` 
2. run `python3 keyboard_visualizer.py`

### config.yml
```
"tilesize" - size of a single key tile
"windowheight", "windowwidth" - width and height of the window, in tilesizes
"font" - link to .ttf of text fonts
"fontsize" - font size in px
"fontcolor" - either use "#2e66ff" or "rgb(28,3,199)"
"backgroundcolor" - see fontcolor
"displaymode" - "none", "count", "name", or "both"
"resetkey" - keycode for reset (ie "ctrl+alt+esc")
"pollingratehz" - polling rate in hz
"keyimage" - link to image of single key
"keyimage_dark" - link to image of single key, but the darkened one when clicked
"keys" - array of keys
    "enabled" - true or false
    "keyCode" - keycode (or mouse_[keycode])
    "name" - name shown
    "x" - x pos in tilesizes
    "y" - y pos in tilesizes
"cps-enable" - enable CPS feature
"cps-x" - x pos for CPS tile
"cps-y" - y pos for CPS tile
```

## known limitations
- kinda laggy if you have tilesize too big
- does not crash properly if you enter invalid keycodes
