import os
import uuid
import env
import water_logger

from env import ROOT_DIR
from water_logger import getLogger

LOG_PATH = os.path.join(ROOT_DIR, 'logs/app.log')

def get_first_line(file_path):
    with open(file_path, "rb") as file:
        try:
            file.seek(-2, 2)

            while file.read(1) != b'\n':
                file.seek(-2,1)
        except(OSError):
            file.seek(0)

        return file.readline().decode()


def test_answer():
    unique_string = str(uuid.uuid4())
    
    logger = getLogger('test')
    logger.debug(unique_string)
    
    last_line = get_first_line(LOG_PATH)

    test_string = 'test - DEBUG - ' + str(unique_string) 
    assert last_line.find(test_string) > 0
