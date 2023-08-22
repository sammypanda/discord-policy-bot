# imports
from models.manager_model import ManagerModel
from controllers.manager_controller import ManagerController

_console_manager = ManagerModel() # instantiate a private manager_model just for console/server admin
_bot = _console_manager.get_bot() # private variable for the ongoing bot instance

# Setup 
manager = ManagerController(_bot) # instantiate the manager commands
_console_manager.run_bot(_bot) # instantiate the bot