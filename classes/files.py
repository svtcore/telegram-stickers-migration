class Files():

    loaded_array = []

    #Write array to file with short name of stickers
    def export_file(self, data):
        try:
            with open('stickers.txt', 'w') as f:
                for i in range(0, len(data)):
                    f.write(data[i]+"\n")
                f.close()
        except NameError:
            print(NameError)

    #Load short names from file and convert to array
    def import_file(self):
        try:
            with open('stickers.txt') as f:
                self.loaded_array = f.readlines()
            self.__trim_values()
        except NameError:
            print(NameError)
            
    #Trim \n from elements in array
    def __trim_values(self):
        try:
            for i in range(0, len(self.loaded_array)):
               self.loaded_array[i] = self.loaded_array[i].strip()
        except NameError:
            print(NameError)
