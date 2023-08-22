from models.manager_model import ManagerModel

class ManagerController:
    def __init__(self):
        if not hasattr(self, '_instance'):
            self._instance = self
            self.manager_model = ManagerModel()

    def run_bot(self):
        self.manager_model.run_bot()

    def commands(self):
        self.manager_model.commands()