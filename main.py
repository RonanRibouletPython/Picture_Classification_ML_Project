# Import the log handler
from CNN_Classification_Task import logger

# Debugging tests for module imports
from CNN_Classification_Task.utils.common import *

test = ["test"]
create_directories(test)

logger.info("Customed logger")