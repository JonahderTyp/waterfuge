import argparse
from configobj import ConfigObj
from RPi.GPIO import cleanup, setwarnings
from datasender.testData import test
from datasender.run import run

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
        if args['test']:
            test(config.get("serverurl"))
        else:
            run(config.get("serverurl"))
    finally:
        print("\ncleaning up...\n")
        cleanup()
