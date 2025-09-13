import board
from keybow2040 import Keybow2040
#from enum import Enum

class States(Enum):
    HOME = 1
    SFIZZ = 2
    AEOLUS = 3
    SETBFREE = 4
    PD = 5

# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Colors
rgb = (0, 255, 255)
engine = (0, 255, 255)
selected_engine(200,240,240)
non_selected_engine(0,40,40)
preset = (0, 255, 0)
settings = (0, 0, 255)
non_functional = (15,15,15)
engine_keys = [3,7,11,15]
setting_keys = [8,12]

# Keys
sfizz_key = 3
aeolus_key = 7
setBfree_key = 11
pd_key = 15

#current_view = States.HOME

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
        elif i in engine_key:
            keys[i].set_led(*non_selected_engine)
        else:
            keys[i].set_led(*preset)

#default view
home_view(keys)

while True:
    # Always remember to call keybow.update() on every iteration of your loop!
    keybow.update()

