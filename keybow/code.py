import board
from keybow2040 import Keybow2040

# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Colors
rgb = (0, 255, 255)
engine = (0, 150, 150)
selected_engine = (200,50,255)
non_selected_engine = (0,40,40)
preset = (70, 50, 0)
settings = (0, 0, 255)
non_functional = (5,5,5)
engine_keys = [3,7,11,15]
setting_keys = [12]

# Keys
sfizz_key = 3
aeolus_key = 7
setBfree_key = 11
pd_key = 15

#current_view = States.HOME

class Engine:
    def __init__(self):
        self.draw_view = home_view

def home_view(keys):
    for i in range(16):
        if i in engine_keys:
            keys[i].set_led(*engine)
        elif i in setting_keys:
            keys[i].set_led(*settings)
        else:
            keys[i].set_led(*non_functional)

def aeolus_view(keys):
    for i in range(16):
        if i == aeolus_key:
            keys[i].set_led(*selected_engine)
        elif i in setting_keys:
            keys[i].set_led(*settings)
        elif i in engine_keys:
            keys[i].set_led(*non_selected_engine)
        else:
            keys[i].set_led(*preset)


def setBfree_view(keys):
    for i in range(16):
        if i == setBfree_key:
            keys[i].set_led(*selected_engine)
        elif i in setting_keys:
            keys[i].set_led(*settings)
        elif i in engine_keys:
            keys[i].set_led(*non_selected_engine)
        else:
            keys[i].set_led(*preset)

#default view
current_engine = aeolus_view
current_engine(keys)
while True:
    # Always remember to call keybow.update() on every iteration of your loop!
    keybow.update()
    current_engine(keys)
    for key in keys:
        if key.pressed:
            if key.get_number() == aeolus_key:
                current_engine = aeolus_view
            elif key.get_number() == setBfree_key:
                current_engine = setBfree_view
            elif key.get_number() in engine_keys:
                current_engine = home_view
            key.set_led(99,99,94)
