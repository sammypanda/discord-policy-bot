from models.generator_model import GeneratorModel

class GeneratorController:
    def log(self, level: int, message: str):
        GeneratorModel().log(level, message)