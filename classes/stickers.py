from pyrogram.raw import functions
from pyrogram.raw import types
import random
from classes.auth import Auth
from classes.files import Files

class Stickers(Auth, Files):

    __sticker_list = []

    '''
        Authenticate with credential data and get all installed stickers
        Save each into array and send to write file function
    '''
    def export_installed_to_file(self):
        try:
            self.authenticate()
            self.start()
            stickers = self.app.send(
                functions.messages.GetAllStickers(
                        hash=random.randint(100000,999999),
                    )
                )
            for i in (range(0, len(stickers['sets']))):
                self.__sticker_list.append(stickers['sets'][i]['short_name'])
            self.export_file(self.__sticker_list)
            self.stop()
            print("Stickers have been successful exported to file stickers.txt")
        except NameError:
            NameError

    '''
        Authenticate with credential data and load array with stickers data
        And install each to new account
    '''
    def import_from_file(self):
        try:
            self.authenticate()
            self.start()
            self.import_file()
            for i in range(0, len(self.loaded_array)):
                try:
                    self.app.send(
                        functions.messages.InstallStickerSet(
                                stickerset=types.InputStickerSetShortName(short_name=self.loaded_array[i]),
                                archived=0
                            )
                        )
                except:
                    print("Error install sticker "+ self.loaded_array[i])
                    continue
                print(self.loaded_array[i] + " has been installed")
            self.stop()
        except NameError:
            print(NameError)