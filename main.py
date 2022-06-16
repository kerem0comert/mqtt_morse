from morse_converter import msg_to_wav, wav_to_msg
import publish
import subscribe

def main():
    subscribe.run()
    
if __name__ == '__main__':
    main()