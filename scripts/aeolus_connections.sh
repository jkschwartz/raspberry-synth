sleep 5

#aeolus connections

jack_connect aeolus:out.L system:playback_1 

jack_connect aeolus:out.R system:playback_2

jack_connect system:midi_capture_1 aeolus:Midi/in


#setBfree connections



#sfizz connections

jack_connect system:midi_capture_1 sfizz:input

jack_connect system:midi_capture_2 sfizz:input