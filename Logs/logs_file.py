import logging


def get_logs():
    """
    this method used to generate logs and also store the logs in current_log_file file
    :return: logger
    """
    logger = logging.getLogger()
    filehandler = logging.FileHandler("..\\Logs\\current_log_file.log", mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    return logger

