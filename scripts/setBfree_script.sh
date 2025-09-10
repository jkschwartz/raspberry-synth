setBfreeUI -j setBfreeJack &

sleep 2 

jack_connect system:midi_capture_2 setBfreeJack:control &> /dev/null

