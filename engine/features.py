import tempfile

# Force temp dir to a writable folder
tempfile.tempdir = r"C:\Users\Pooja\Desktop\temp_audio"


import eel
from pydub import AudioSegment
from pydub.playback import play

@eel.expose
# Playing assistant sound function
def playAssistantSound():
    music_dir = "www/assets/audio/start_sound.mp3"
    sound = AudioSegment.from_file(music_dir, format="mp3")
    play(sound)
