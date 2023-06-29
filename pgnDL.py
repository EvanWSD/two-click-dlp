import shlex
import subprocess
import pyperclip as pc

# ------- CHANGE PATH --------
path = "G:\YT\Content"

def download(pPath, pAudioOnly):
    # configure command string based on a/v
    cmdString = "yt-dlp "
    if pAudioOnly:
        cmdString += "-x --audio-format mp3 "
    else:
        cmdString += '-f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best '
    cmdString += pc.paste()
    # execute yt-dlp command
    subprocess.Popen(shlex.split(cmdString), cwd=pPath).wait()