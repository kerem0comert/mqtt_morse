from morse_audio_decoder.morse import MorseCode
from subprocess import call
from pyMorseTranslator import translator


def morse_to_plaintext(morse_msg: str) -> str:
    return translator.Decoder().decode(morse_msg).plaintext

def msg_to_wav(msg: str, curr_time: str) -> int:
    return call(f'echo "{msg}" |python generator/play.py -f 750 --wpm 10  -o messages/{curr_time}.wav', shell=True)

def wav_to_msg(wav_path: str) -> str:
    return MorseCode.from_wavfile(wav_path).decode()
