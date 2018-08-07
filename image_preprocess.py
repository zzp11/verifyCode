
from PIL import Image

import logger as main_logger
import logging
logger = logging.getLevelName('verifycode.preprocess')

class ImagePreprocess():

    @classmethod
    def preprocess(cls, image_path):
        with open(image_path, 'rb') as f:
            pass

