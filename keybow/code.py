import board
from keybow2040 import Keybow2040

import time

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Set up keyboard integration
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Colors
engine = (0, 160, 170)
selected_engine = (255,0,255)
non_selected_engine = (0,20,20)
preset = (80, 50, 0)
action_up = (50, 200, 0)
action_down = (200, 30, 0)
settings = (0, 0, 255)
fx_settings = (0,255,0)

non_functional = (5,5,5)

# Keys
engine_keys = [0,1,2,3]
mode_keys = [4,5,6,7,8,9,10,11,12,13]
sfizz_key = 0
aeolus_key = 1
setBfree_key = 2
pd_key = 3

settings_key = 15
fx_key = 14


#Settings view specific
action_up_keys = [4,5,11]
action_down_keys = [8,9]


#SFZ presets
sfz_presets = {
    "Kawaii": [],
    "360": [],
    "Mirage": [],
    "Soviet": [],
    "Tape": [],
    "OB": []
}

key_4_preset = "sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/02. Keys/Randroid - Kawaii Dreams From Mars.sfz"

key_5_preset = "sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/04. Organs/Indie Organ - Kawaii Dreams From Mars.sfz"

key_6_preset = "sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/05. Strings/String Combo 1 - TOM 1501.sfz"

key_7_preset = "sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/04. Keys and Chords/Clarinet - MAESTRO.sfz" 

key_8_preset = "sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/03. Pads/Piano 201 - MAESTRO.sfz"

key_9_preset = "sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/05. Bass/E Bass Multi Filter - 360 From Mars.sfz" 

key_10_preset = "sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/02. Strings/Strings - 360 From Mars.sfz" 

key_11_preset = "sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/01. Keys/Artifact Piano - Mirage From Mars.sfz" 

#[0 1 2 3]
#[4 5 6 7]
#[8 9 10 11]
#[12 13 14 15]
#[Eng Eng Eng Eng]
#[Pre Pre Pre Pre]
#[Pre Pre Pre Pre]
#[Pre Pre Pre Set]

class Screen(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return ''

    def enter(self, machine):
        pass

    def exit(self, machine):
        pass

    def update(self, machine):
        return True


#Ok ok maybe this is a state machine
class ScreenMachine(object):
    def __init__(self):
        self.current_screen = None
        self.screens = {}

    def add_screen(self, screen):
        self.screens[screen.name] = screen

    def go_to_screen(self, screen_name):
        if self.current_screen:
            self.current_screen.exit(self)
        self.current_screen = self.screens[screen_name]
        self.current_screen.enter(self)

    def update(self):
        if self.current_screen:
            self.current_screen.update(self)


class HomeScreen(Screen):
    @property
    def name(self):
        return 'home'

    def enter(self, machine):
        keys[sfizz_key].set_led(*engine)
        @keybow.on_release(keys[sfizz_key])
        def release_handler(key):
            machine.go_to_screen('sfizz')

        keys[aeolus_key].set_led(*engine)
        @keybow.on_release(keys[aeolus_key])
        def release_handler(key):
            machine.go_to_screen('aeolus')

        keys[setBfree_key].set_led(*engine)
        @keybow.on_release(keys[setBfree_key])
        def release_handler(key):
            machine.go_to_screen('setBfree')
       
        keys[pd_key].set_led(*engine)
        @keybow.on_release(keys[pd_key])
        def release_handler(key):
            machine.go_to_screen('pd')

        keys[settings_key].set_led(*settings)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*fx_settings)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

        for i in mode_keys:
            keys[i].set_led(*non_functional)
            
            @keybow.on_release(keys[i])
            def release_handler(key):
                pass
        
    def exit(self, machine):
        #shut down running engines
        pass

    def update(self, machine):
        return True

class SettingsScreen(Screen):

    @property
    def name(self):
        return 'settings'

    def enter(self, machine):
        #home keys are engine keys
        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')

        for i in mode_keys:
            keys[i].set_led(*non_functional)
            @keybow.on_release(keys[i])
            def release_handler(key):
                pass
 
        keys[settings_key].set_led(*selected_engine)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*non_selected_engine)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

    def exit(self, machine):
        pass

    def update(self, machine):
        return True

class FxScreen(Screen):
    @property
    def name(self):
        return 'fx'

    def enter(self, machine):
        #home keys are engine keys
        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')

        for i in mode_keys:
            keys[i].set_led(*non_functional)
            @keybow.on_release(keys[i])
            def release_handler(key):
                pass
 
        keys[settings_key].set_led(*non_selected_engine)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*selected_engine)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

    def exit(self, machine):
        pass

    def update(self, machine):
        return True

class SfizzScreen(Screen):
    @property
    def name(self):
        return 'sfizz'

    def enter(self, machine):
        
        #start up a terminal
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)

        time.sleep(1)
        layout.write('~/raspberry-synth/scripts/sfz_script.sh')
        time.sleep(1)
        keyboard.send(Keycode.ENTER)

        #home keys are engine keys
        

        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')
        
        keys[sfizz_key].set_led(*selected_engine)
        @keybow.on_release(keys[sfizz_key])
        def release_handler(key):
            pass
        

        for i in mode_keys:
            if i == 4:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_4_preset)
            elif i == 5:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_5_preset)
            elif i == 6:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_6_preset)
            elif i == 7:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_7_preset)
            elif i == 8:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_8_preset)
            elif i == 9:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_9_preset)
            elif i == 10:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_10_preset)
            elif i == 11:
                keys[i].set_led(*preset)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    load_sfz_from_sfizz(key_11_preset)
            else: 
                keys[i].set_led(*non_functional)
                @keybow.on_release(keys[i])
                def release_handler(key):
                    pass
 
        keys[settings_key].set_led(*settings)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*fx_settings)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

    def exit(self, machine):
        pass

    def update(self, machine):
        return True

class AeolusScreen(Screen):
    @property
    def name(self):
        return 'aeolus'

    def enter(self, machine):
        #start aeolus
        
        #start up a terminal
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)

        time.sleep(1)
        layout.write('~/raspberry-synth/scripts/aeolus_script.sh')
        time.sleep(1)
        keyboard.send(Keycode.ENTER)

        #home keys are engine keys
        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')
        
        keys[aeolus_key].set_led(*selected_engine)
        @keybow.on_release(keys[aeolus_key])
        def release_handler(key):
            pass
        

        for i in mode_keys:
            keys[i].set_led(*non_functional)
            @keybow.on_release(keys[i])
            def release_handler(key):
                pass
 
        keys[settings_key].set_led(*settings)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*fx_settings)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

    def exit(self, machine):
        pass

    def update(self, machine):
        return True


class SetBfreeScreen(Screen):
    @property
    def name(self):
        return 'setBfree'

    def enter(self, machine):
        #start up a terminal
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)

        time.sleep(1)
        layout.write('~/raspberry-synth/scripts/setBfree_script.sh')
        time.sleep(1)
        keyboard.send(Keycode.ENTER)
        
        #home keys are engine keys
        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')
        
        keys[setBfree_key].set_led(*selected_engine)
        @keybow.on_release(keys[setBfree_key])
        def release_handler(key):
            pass

        for i in mode_keys:
            keys[i].set_led(*non_functional)
            @keybow.on_release(keys[i])
            def release_handler(key):
                pass
 
        keys[settings_key].set_led(*settings)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*fx_settings)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

    def exit(self, machine):
        pass

    def update(self, machine):
        return True


class PdScreen(Screen):
    @property
    def name(self):
        return 'pd'

    def enter(self, machine):
        #home keys are engine keys
        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')
        
        keys[pd_key].set_led(*selected_engine)
        @keybow.on_release(keys[pd_key])
        def release_handler(key):
            pass

        for i in mode_keys:
            keys[i].set_led(*non_functional)
            @keybow.on_release(keys[i])
            def release_handler(key):
                pass
 
        keys[settings_key].set_led(*settings)
        @keybow.on_release(keys[settings_key])
        def release_handler(key):
            machine.go_to_screen('settings')

        keys[fx_key].set_led(*fx_settings)
        @keybow.on_release(keys[fx_key])
        def release_handler(key):
            machine.go_to_screen('fx')

    def exit(self, machine):
        pass

    def update(self, machine):
        return True

#Helper functions
def load_sfz_from_sfizz(path):
    layout.write('load_instrument "' + path + '"')
    time.sleep(.5)
    keyboard.send(Keycode.ENTER)

machine = ScreenMachine()
machine.add_screen(HomeScreen())
machine.add_screen(SettingsScreen())
machine.add_screen(FxScreen())
machine.add_screen(SfizzScreen())
machine.add_screen(AeolusScreen())
machine.add_screen(SetBfreeScreen())
machine.add_screen(PdScreen())

#default view
machine.go_to_screen('home')
while True:
    # Always remember to call keybow.update() on every iteration of your loop!
    keybow.update()
    machine.update()
    for key in keys:
        if key.pressed:
            #get current value and flash then return to current value
            key.set_led(99,20,20)
