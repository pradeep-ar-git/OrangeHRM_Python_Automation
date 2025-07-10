# Not working, Need to check the loggers

import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + "\\logs\\automation.log"
        logging.basicConfig(
            filename=path,
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d-%M-%Y %H-%M-%S %p'
        )
        return logging.getLogger()
