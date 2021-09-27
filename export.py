from classes.stickers import Stickers
import os
from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = os.getenv('SESSION_NAME_1')
API_ID = os.getenv('API_ID_1')
API_HASH = os.getenv('API_HASH_1')

stickers = Stickers(SESSION_NAME, API_ID, API_HASH)
stickers.export_installed_to_file()

