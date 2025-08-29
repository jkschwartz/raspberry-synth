
if [ "$#" -ne 1 ]; then
    echo "Missing sfx file location ./start_sfz.sh <file>"
    exit 1
fi

sfizz_jack --jack_autoconnect --preload_size 16384 "$1" &

sleep 2

jack_connect system:midi_capture_2 sfizz:in &> /dev/null

fg
