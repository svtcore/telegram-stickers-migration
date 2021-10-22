# Telegram Stickers Migration

Helps quickly migrate (import or export) sticker sets from one account to another account 
## Installation
```pip install -r requirements.txt```
## Setup

### 1. Edit .env file

Description for fileds

**```SESSION_NAME```** - could be any random name, recommend **IMPORT** or **EXPORT**

**```API_ID```** - credential of application, which was create on the my.telegram.org

**```API_HASH```** - credential of application, which was create on the my.telegram.org

### 2. Choose mode and run file

For **EXPORT AND IMPORT** run

**```python bot.py```** - as result script export stickers list to file and import them to second account

For only **EXPORT** run

**```python export.py```** - as result you will be get file **stickers.txt** with list of sticker sets short name

For only **IMPORT** run

**```python import.py```** - as result script will be add sticker sets from file **stickers.txt** to selected account

### 3. After run script you should authorize on the account(s) and migration will be start

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPL-3.0](https://github.com/svtcore/telegram-referral-bot/blob/main/LICENSE)

## Involved libraries
* [Pyrogram](https://github.com/pyrogram/pyrogram)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
