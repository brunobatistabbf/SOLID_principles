from abc import ABC, abstractmethod
#Para resolver esse problemas podemos criar uma classe abstrata que tenha o metodo abstrato de buscar dados
#podendo abstrair esse metodo em varias classes especificas (Front-end, Back-end e API REST)

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"