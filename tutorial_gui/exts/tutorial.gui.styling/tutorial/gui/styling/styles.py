import omni.ui as ui
from omni.ui import color as cl

class StyleSheet():

    # Colors
    background = cl("#1A1A2E")
    foreground = cl("#2A2A4E")
    text = cl("#FFFFFF")
    muted_pink = cl("#FF8A80")
    deep_rose = cl("#C2185B")
    lavender = cl("#B39DDB")
    grape = cl("#5E35B1")


    # Styles
    my_window = {
        "Window": {
            "background_color": background,
            "border_radius": 5
        }
    }

    custom_rectangle = {
        "Rectangle": {
            "background_color": foreground,
            "border_radius": 5
        }
    }

    my_label = {
        "Label": {
            "color": text,
            "font_size": 24
        }
    }

    add_button = {
        "Button": {
            "background_color": muted_pink,
            "border_width": 3,
            "border_radius": 7,
            "border_color": deep_rose
        },
        "Button.Label": {
            "color": text,
            "font_size": 24
        }
    }

    reset_button = {
        "Button": {
            "background_color": lavender,
            "border_radius": 7,
            "border_width": 3,
            "border_color": grape
        },
        "Button.Label": {
            "color": text,
            "font_size": 24
        }
    }