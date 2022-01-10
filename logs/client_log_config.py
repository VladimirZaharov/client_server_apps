import logging


logger = logging.getLogger('messenger.client')
formatter = logging.Formatter("%(asctime)s   %(levelname)-10s %(module)-10s %(message)s ")

server_file_handler = logging.FileHandler("messenger.client.log", encoding='utf-8')
server_file_handler.setLevel(logging.DEBUG)
server_file_handler.setFormatter(formatter)
logger.addHandler(server_file_handler)
logger.setLevel(logging.DEBUG)
