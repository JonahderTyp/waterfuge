import argparse
from time import sleep

from configobj import ConfigObj
from RPi.GPIO import cleanup, setwarnings

from datasender.run import run
from datasender.testData import test

if __name__ == "__main__":
    print("Hello from Datasender")
    parser = argparse.ArgumentParser(description="Send data to a server")
    parser.add_argument("--config", type=str,
                        help="Path to the config file", default="config.cfg")
    parser.add_argument("--server-port", type=int,
                        help="Port to listen for the server ip", default=8080)
    parser.add_argument("-test", action="store_true",
                        help="Test the connection to the server")
    args = vars(parser.parse_args())
    config = ConfigObj("config.cfg")

    setwarnings(True)
    try:
        while True:
            try:
                if args['test']:
                    test(config.get("serverurl"))
                else:
                    run(config.get("serverurl"))
            except KeyboardInterrupt:
                print("\nKeyboard interrupt detected")
                raise KeyboardInterrupt
            except Exception as e:
                print(f"\n\n\nError: {e}\n")
                print("Retrying in 5 seconds...\n\n\n")
                sleep(5)
    finally:
        print("\ncleaning up...\n")
        cleanup()
