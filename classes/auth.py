from pyrogram import Client

class Auth:

    app = None
    session_name = None
    api_id = None
    api_hash = None 

    #Set data for working
    def __init__(self, session_name, api_id, api_hash) -> None:
        self.session_name = session_name
        self.api_id = api_id
        self.api_hash = api_hash

    #Setup to exist session or create new using credential data
    def authenticate(self):
        try:
            self.app = Client(session_name="./sessions/" + self.session_name, api_id=self.api_id, api_hash=self.api_hash)
        except NameError:
            print(NameError)

    #Start created session
    def start(self):
        try:
            self.app.start()
        except NameError:
            print(NameError)

    #Stop created session
    def stop(self):
        try:
            self.app.stop()
        except NameError:
            print(NameError)

