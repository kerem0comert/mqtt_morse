from morse_audio_decoder.morse import MorseCode
from subprocess import call


def msg_to_wav(msg: str) -> int:
    return call(f'echo "{msg}" |python generator/play.py -f 750 --wpm 10  -o {msg}.wav', shell=True)

def wav_to_msg(wav_path: str) -> str:
    return MorseCode.from_wavfile(wav_path).decode()
