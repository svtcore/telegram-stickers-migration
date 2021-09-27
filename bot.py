from classes.stickers import Stickers
import os
from dotenv import load_dotenv

load_dotenv()

SESSION_NAME_1 = os.getenv('SESSION_NAME_1')
API_ID_1 = os.getenv('API_ID_1')
API_HASH_1 = os.getenv('API_HASH_1')

SESSION_NAME_2 = os.getenv('SESSION_NAME_2')
API_ID_2 = os.getenv('API_ID_2')
API_HASH_2 = os.getenv('API_HASH_2')

stickers = Stickers(SESSION_NAME_1, API_ID_1, API_HASH_1)
stickers.export_installed_to_file()

stickers = Stickers(SESSION_NAME_2, API_ID_2, API_HASH_2)
stickers.import_from_file()
