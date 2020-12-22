# pyQt5-keypress-visualizer
simple keypress visualizer made with pyQt5

designed for me to practice pyQt5 skills



## how to use
1. install dependencies:
 `keyboard` `mouse` `pyQt5` `pyyaml`
2. configure `config/config.yml` (check the one I included for example) or use `config/fpsconfig.yml`
3. run `python3 keyboard_visualizer.py`
4. fix any errors if necessary since this probably won't work lol

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
```

## known limitations
- kinda laggy if you have tilesize too big
- does not crash properly if you enter invalid keycodes
- for whatever reason closing it doesn't always work...???
    - apparently even more so if you have more keys