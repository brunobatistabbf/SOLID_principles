#Nesse exemplo podemos ver que o front end necessita apresentar os dados para o usuario
#Mas para isso depende do back-end buscar os dados no banco de dados e retornar para o front-end
#Além de vio o DIP Principle também viola outros principios caso fosse escalar a aplicação, como por exemplo implementar a chamada de dados de uma API
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"