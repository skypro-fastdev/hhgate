import asyncio
import logging
import sys

from src.classes.HHArtifactsClient import HHArtifactsClient
from src.classes.HHResumeClient import HHResumeClient
from src.config import HH_ACCESS_TOKEN

if __name__ == '__main__':
    hh_res_client = HHResumeClient(access_token=HH_ACCESS_TOKEN)
    hh_art_client = HHArtifactsClient(access_token=HH_ACCESS_TOKEN)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(hh_art_client.load_photo())
