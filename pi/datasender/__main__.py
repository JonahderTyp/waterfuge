import argparse

from configobj import ConfigObj

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send data to a server")
    parser.add_argument("--config", type=str,
                        help="Path to the config file", default="config.cfg")
    parser.add_argument("--server-port", type=int,
                        help="Port to listen for the server ip", default=8080)
    parser.add_argument("-test", action="store_true",
                        help="Test the connection to the server")
    args = vars(parser.parse_args())
    print(args)
    config = ConfigObj(args['config'])
    try:
        if args['test']:
            from .test import test
            test(config)
        else:
            from .main import main
            main(config)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
