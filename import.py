from classes.stickers import Stickers
import os
from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = os.getenv('SESSION_NAME_2')
API_ID = os.getenv('API_ID_2')
API_HASH = os.getenv('API_HASH_2')

stickers = Stickers(SESSION_NAME, API_ID, API_HASH)
stickers.import_from_file()

