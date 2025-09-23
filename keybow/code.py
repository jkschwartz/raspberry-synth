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
selected_engine = (205,0,255)
non_selected_engine = (0,10,10)
preset = (80, 50, 0)
pack_synth = (178,34,34)
pack_sample = (251,79,20)
preset_bass = (100,0,10)
preset_keys = (80,64,77)
preset_orch = (89,39,32)
preset_synth = (198,34,34)
preset_fx = (20,0,100)

selected_preset = (10,150,30)
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


sfz_packs = {4: ("kawaii","synth"), 5: ("s360","sample"), 6: ("mirage","sample"), 7: ("soviet","synth"), 8: ("tape","sample"), 9: ("ob","synth"), 10: ("drSample","sample"), 11: ("vinyl","sample")}
#keys to be set to non functional for sfizz screen
unused_packs = [12,13]

#SFZ presets
sfz_presets = {
    "kawaii": [
        ("sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/02. Keys/Randroid - Kawaii Dreams From Mars.sfz","keys"),
        ("sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/04. Organs/Indie Organ - Kawaii Dreams From Mars.sfz","keys"),
        ("sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/03. Pads/Analog Strings - Kawaii Dreams From Mars.sfz","orch"),
        ("sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/01. Voices/Bell Air - Kawaii Dreams From Mars.sfz","orch"),
        ("sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/03. Pads/Glass Howl - Kawaii Dreams From Mars.sfz","synth"),
        ("sfz/kawaii_dreams_from_mars/Kawaii Dreams From Mars/SFZ/Kawaii Dreams From Mars/02. Keys/Jazz Harp - Kawaii Dreams From Mars.sfz","keys")

        ],
    "s360": [
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/05. Bass/E Bass Multi Filter - 360 From Mars.sfz","bass"),
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/02. Strings/Strings - 360 From Mars.sfz","orch"),
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/02. Strings/Strings Filter - 360 From Mars.sfz","orch"),
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/04. Brass & Woodwind/French Horn Filter - 360 From Mars.sfz","orch"),
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/06. Perc/Vibes - 360 From Mars.sfz","orch"),
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/04. Brass & Woodwind/English Horn - 360 From Mars.sfz","orch"),
        ("sfz/360_from_mars/360 From Mars/SFZ/360 From Mars/03. Keys/E Piano Tremolo - 360 From Mars.sfz","keys")
        ],
    "mirage": [
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/01. Keys/Artifact Piano - Mirage From Mars.sfz","keys"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/02. Orchestral/String Quartet - Mirage From Mars.sfz","orch"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/06. Vox/Dark Vox - Mirage From Mars.sfz","orch"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/05. Synth/Electric Strings - Mirage From Mars.sfz","synth"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/01. Keys/Wurli - Mirage From Mars.sfz","keys"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/03. Bass/Fuzz Bass - Mirage From Mars.sfz","bass"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/03. Bass/Upright Bass - Mirage From Mars.sfz","bass"),
        ("sfz/mirage_from_mars/Mirage From Mars/Presets/SFZ/Mirage From Mars/01. Keys/Dark Piano - Mirage From Mars.sfz","keys")

        ],
    "soviet": [
        ("sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/05. Strings/String Combo 1 - TOM 1501.sfz","orch"),
        ("sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/04. Keys and Chords/Clarinet - MAESTRO.sfz","orch"),
        ("sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/03. Pads/Piano 201 - MAESTRO.sfz","keys"),
        ("sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/02. Leads/Broken Brass - ALTAIR 231.sfz","synth"),
        ("sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/06. Basic Waveforms/Sawtooth - FORMANTA POLIVOKS.sfz","synth"),
        ("sfz/soviet_synths_from_mars/Soviet Synths From Mars/SFZ/Soviet Synths From Mars/03. Pads/Drunkpad - AELITA.sfz","synth")
        

        ],
    "tape": [
        ("sfz/tape_fragments_from_mars/Tape Fragments From Mars/Presets/SFZ/Tape Fragments From Mars/02. Leads/Glass Theremin - Tape Fragments From Mars.sfz","fx"),
        ("sfz/tape_fragments_from_mars/Tape Fragments From Mars/Presets/SFZ/Tape Fragments From Mars/02. Leads/Tape Flute - Tape Fragments From Mars.sfz","orch"),
        ("sfz/tape_fragments_from_mars/Tape Fragments From Mars/Presets/SFZ/Tape Fragments From Mars/05. FX/Awaiting Raptor - Tape Fragments From Mars.sfz","fx"),
        ("sfz/tape_fragments_from_mars/Tape Fragments From Mars/Presets/SFZ/Tape Fragments From Mars/04. Bass/Otari Bass - Tape Fragments From Mars.sfz","bass")
        ],
    "ob": [
        ("sfz/ob_from_mars/OB From Mars/SFZ/OB From Mars/Organs/King Jimmy - OB From Mars.sfz","keys"),
        ("sfz/ob_from_mars/OB From Mars/SFZ/OB From Mars/Strings/Halen Strings - OB From Mars.sfz","orch"),
        ("sfz/ob_from_mars/OB From Mars/SFZ/OB From Mars/Keys/AM Funk - OB From Mars.sfz","keys"),
        ("sfz/ob_from_mars/OB From Mars/SFZ/OB From Mars/Bass/Medium Muff - OB From Mars.sfz","bass"),
        ("sfz/ob_from_mars/OB From Mars/SFZ/OB From Mars/Brass & Woodwinds/Hard Trumpet - OB From Mars.sfz", "orch")
        ],
    "drSample": [
        ("sfz/dr_sample_from_mars/SFZ/Dr Sample From Mars/03. Keys/02. Upright Piano - Dr Sample From Mars.sfz","keys"),
        ("sfz/dr_sample_from_mars/SFZ/Dr Sample From Mars/04. Pads/04. Mellovox - Dr Sample From Mars.sfz","orch"),
        ("sfz/dr_sample_from_mars/SFZ/Dr Sample From Mars/04. Pads/02. Prophet Chorus - Dr Sample From Mars.sfz","synth"),
        ("sfz/dr_sample_from_mars/SFZ/Dr Sample From Mars/02. Bass/06. Warm Bass - Dr Sample From Mars.sfz","bass"),
        ("sfz/dr_sample_from_mars/SFZ/Dr Sample From Mars/02. Bass/02. E Bass - Dr Sample From Mars.sfz","bass"),
        ("sfz/dr_sample_from_mars/SFZ/Dr Sample From Mars/03. Keys/01. 80s Piano - Dr Sample From Mars.sfz","keys")
        ],
    "vinyl": [
        ("sfz/vinyl_synths_from_mars/Vinyl Synths From Mars/Presets/SFZ/Vinyl Synths From Mars/01. Bass/MS20 Fuzz Mod - Vinyl Synths From Mars.sfz","bass"),
        ("sfz/vinyl_synths_from_mars/Vinyl Synths From Mars/Presets/SFZ/Vinyl Synths From Mars/02. Keys & Pads/Sub37 Sine Chorus - Vinyl Synths From Mars.sfz","synth"),
        ("sfz/vinyl_synths_from_mars/Vinyl Synths From Mars/Presets/SFZ/Vinyl Synths From Mars/03. Leads/Jupiter4 Saw Delay - Vinyl Synths From Mars.sfz","synth"),
        ("sfz/vinyl_synths_from_mars/Vinyl Synths From Mars/Presets/SFZ/Vinyl Synths From Mars/03. Leads/Polaris Snake Organ - Vinyl Synths From Mars.sfz","keys")
            ]
}

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
        self.running_engine = None
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
        #check if already running sfizz
        if machine.running_engine != self.name:
            machine.running_engine = self.name
            #start up a terminal
            keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
            time.sleep(1)
            layout.write('~/raspberry-synth/scripts/sfz_script.sh')
            time.sleep(.5)
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
        
        for pack_id, value in sfz_packs.items():
            if value[1] == "synth":
                keys[pack_id].set_led(*pack_synth)
            elif value[1] == "sample":
                keys[pack_id].set_led(*pack_sample)
            else:
                keys[pack_id].set_led(*preset)

            engine_nav_helper(pack_id,value[0])
        for i in unused_packs:
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

#https://medium.com/skiller-whale/late-binding-variables-its-a-trap-c17af980164f
def engine_nav_helper(key_id,new_screen):
    @keybow.on_release(keys[key_id])
    def release_handler(key):
        machine.go_to_screen(new_screen)

class SfizzTypeScreen(Screen):
    def __init__(self):
        self.selected_sfz = -1

    @property 
    def name(self):
        pass

    def enter(self, machine):

        print(self.name)
        for i in engine_keys:
            keys[i].set_led(*non_selected_engine)
            @keybow.on_release(keys[i])
            def release_handler(key):
                machine.go_to_screen('home')
        
        keys[sfizz_key].set_led(*selected_engine)
        @keybow.on_release(keys[sfizz_key])
        def release_handler(key):
            machine.go_to_screen('sfizz')

        for i in mode_keys:
            
            if i-4 < len(sfz_presets[self.name]):
                preset = sfz_presets[self.name][i-4]
                if preset[1] == "bass":
                    keys[i].set_led(*preset_bass)
                elif preset[1] == "keys":
                    keys[i].set_led(*preset_keys)
                elif preset[1] == "orch":
                    keys[i].set_led(*preset_orch)
                elif preset[1] == "synth":
                    keys[i].set_led(*preset_synth)
                elif preset[1] == "fx":
                    keys[i].set_led(*preset_fx)
                else:
                    keys[i].set_led(*preset)
                self.sfizz_load_helper(i,preset[0])
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
        if selected_sfz > 0 and selected_sfz < 16:
            print(self.name)
            print("something selected")
            print(selected_sfz)
            #not totally functionaly, TODO fix me
            #keys[selected_sfz].set_led(*selected_preset)
 

    def sfizz_load_helper(self,key_id,preset_path):
        @keybow.on_release(keys[key_id])
        def release_handler(key):
            selected_sfz = key_id
            load_sfz_from_sfizz(preset_path)


class KawaiiScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'kawaii'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass


class S360Screen(SfizzTypeScreen):
    @property
    def name(self):
        return 's360'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass

class MirageScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'mirage'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass


class SovietScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'soviet'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass

class TapeScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'tape'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass

class ObScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'ob'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass


class DrSampleScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'drSample'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass

class VinylScreen(SfizzTypeScreen):
    @property
    def name(self):
        return 'vinyl'

    def enter(self, machine):
        SfizzTypeScreen.enter(self, machine)
    
    def exit(self, machine):
        pass

    def update(self,machine):
        pass



class AeolusScreen(Screen):
    @property
    def name(self):
        return 'aeolus'

    def enter(self, machine):
        #start aeolus
        if machine.running_engine != self.name:
            machine.running_engine = self.name
            #start up a terminal
            keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)

            time.sleep(1)
            layout.write('~/raspberry-synth/scripts/aeolus_script.sh')
            time.sleep(.5)
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
        if machine.running_engine != self.name:
            machine.running_engine = self.name
            #start up a terminal
            keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
            time.sleep(1)
            layout.write('~/raspberry-synth/scripts/setBfree_script.sh')
            time.sleep(.5)
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
machine.add_screen(KawaiiScreen())
machine.add_screen(S360Screen())
machine.add_screen(MirageScreen())
machine.add_screen(SovietScreen())
machine.add_screen(TapeScreen())
machine.add_screen(ObScreen())
machine.add_screen(DrSampleScreen())
machine.add_screen(VinylScreen())

#default view
machine.go_to_screen('home')
while True:
    # Always remember to call keybow.update() on every iteration of your loop!
    keybow.update()
    machine.update()
    for key in keys:
        if key.pressed:
            #get current value and flash then return to current value
            current_rgb = key.rgb
            key.set_led(50,50,50)
            time.sleep(.2)
            key.set_led(current_rgb[0],current_rgb[1],current_rgb[2])
