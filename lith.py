# (c) 2022 geschmit

"""
from pydub import AudioSegment
from pydub.playback import play
"""
from datetime import datetime

from loguru import logger
import cv2

cv2.bootstrap()

logger.add("logs/" + str(datetime.now()) + ".log")
logger.log("INFO","HELLO- Monolith ver. 1.0")
logger.log("INFO","(c) 2022 geschmit")
logger.log("INFO","System boot...")


