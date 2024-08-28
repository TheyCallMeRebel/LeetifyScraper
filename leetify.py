import json
import traceback
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='errors.log', encoding='utf-8',level=logging.ERROR)


class leetify:
    def __init__(self, response):
        self.response = response
        s
    def grabPlayer(response):
        playerResponse = json.loads(response.text)
        try:
            PlayerAim = playerResponse['recentGameRatings']['aim']
            PlayerUtil = playerResponse['recentGameRatings']['utility']
            errorcreate = playerResponse['aim']
        except KeyError as e:
            logger.error(traceback.format_exception(e))
            return "KeyError"
