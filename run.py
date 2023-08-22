# imports
from models.manager_model import ManagerModel
from controllers.manager_controller import ManagerController

_console = ManagerModel() # instantiate a private manager_model just for console/server admin
_bot = _console.get_bot() # private variable for "managing" the ongoing bot instance

# Setup 
manager = ManagerController(_bot) # instantiate the manager commands
_console.run_bot(_bot) # instantiate the bot