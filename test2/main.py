import logging
import os



#logging.basicConfig(filename='demo.log', level=logging.DEBUG)


logging.basicConfig(filename='demo.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')


if __name__ == "__main__":
    logging.warning("shit")
    logging.info("Hello, Python!")
    logging.debug("I'm a debug message!")


