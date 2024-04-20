import pathlib

ROOT_DIR = None

def setup():
    global ROOT_DIR
    ROOT_DIR = str(pathlib.Path(__file__).parent.parent.absolute())

setup()