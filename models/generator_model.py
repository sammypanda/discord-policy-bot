import os
from dotenv import load_dotenv

load_dotenv() # import dotenv values

class GeneratorModel:
    def log(self, level: int, message: str):
        if int(os.getenv('DEBUG_LEVEL')) >= int(level):
            print(message)
        