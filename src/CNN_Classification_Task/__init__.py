import os
import sys
import logging

# Custom logging creation

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Creation of the logging folder and file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    
    level= logging.INFO,
    format= logging_str,
    # 
    handlers=[
        # Handle the log files
        logging.FileHandler(log_filepath),
        # Print the log in the terminal
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("CNNClassifierLogger")