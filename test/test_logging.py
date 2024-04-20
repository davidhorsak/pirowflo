import os
import uuid
import env
import water_logger

from env import ROOT_DIR
from water_logger import getLogger


def get_list_line(file_path):
    with open(file_path, "rb") as file:
        try:
            file.seek(-2, 2)

            while file.read(1) != b'\n':
                file.seek(-2,1)
        except(OSERROR):
            file.seek(0)

        return file.readline().decode()


def test_answer():
    unique_string = str(uuid.uuid4())
    
    logger = getLogger('test')
    logger.debug(unique_string)

    log_path = os.path.join(ROOT_DIR, 'logs/app.log')
    last_line = get_list_line(log_path)

    test_string = 'test - DEBUG - ' + str(unique_string) 
    
    assert last_line.find(test_string) > 0