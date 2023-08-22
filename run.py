# imports
from models.manager_model import ManagerModel
from controllers.manager_controller import ManagerController

_console = ManagerController() # instantiate a private controller just for console/server admin

# Setup 
manager = _console.commands() # instantiate the manager commands (client-side manager)
_console.run_bot() # instantiate the bot after registering handlers