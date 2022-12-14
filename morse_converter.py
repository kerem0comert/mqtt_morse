from morse_audio_decoder.morse import MorseCode
from subprocess import call
from pyMorseTranslator import translator


def morse_to_plaintext(morse_msg: str) -> str:
    return translator.Decoder().decode(morse_msg).plaintext

def msg_to_wav(msg: str, curr_time: str, wpm: int, tone_frequency: int) -> int:
    return call(f'echo "{msg}" |python generator/play.py -f {tone_frequency} --wpm {wpm} --message {msg} -o messages/{curr_time}.wav' 
                , shell=True)

def wav_to_msg(wav_path: str) -> str:
    return MorseCode.from_wavfile(wav_path).decode()
