sleep 5

jack_connect aeolus:out.L system:playback_1 

jack_connect aeolus:out.R system:playback_2


jack_connect system:midi_capture_1 aeolus:Midi/in
