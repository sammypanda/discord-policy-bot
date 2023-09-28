import os
import logging
from dotenv import load_dotenv

load_dotenv() # import dotenv values

class GeneratorModel:
    def __init__(self):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    def log(self, level: int, message: str):
        if int(os.getenv('DEBUG_LEVEL')) >= int(level):
            print(message)
            logging.info(message) # before committing, investigate if this actually is worthwhile
        