import logging


logger = logging.getLogger("APP_LOG")
logger.setLevel(logging.INFO)

# Define a formatter
formatter = logging.Formatter('%(asctime)-4s %(filename)-4s %(levelname)-4s %(message)s')

# Define a console handler
console = logging.StreamHandler()
# Set the log level
console.setLevel(logging.INFO)
# Set the format
console.setFormatter(formatter)
# Add the handler to the root logger
logger.addHandler(console)

# define a file handler
file = logging.FileHandler('k8s_demo_fastapi.log')
# Set the log level
file.setLevel(logging.INFO)
# Set the format
file.setFormatter(formatter)
# Add the handler to the root logger
logger.addHandler(file)
