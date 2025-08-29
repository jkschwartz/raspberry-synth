aeolus &

sleep 2 

jack_connect aeolus:out.L system:playback_1 &> /dev/null

jack_connect aeolus:out.R system:playback_2 &> /dev/null


jack_connect system:midi_capture_1 aeolus:Midi/in &> /dev/null

