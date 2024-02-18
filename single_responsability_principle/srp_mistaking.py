from pathlib import Path
from zipfile import ZipFile

#Nesse exemplo de classe fugindo do principio de responsabilidade unica,
# A classe tem mais de uma responsabilidade e mais de uma motivo para ser mudada
#No caso de gerenciar arquivos e trabalhar com arquivos zipados
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

if __name__ == '__main__':
    #Exemplo de uso
    arquivo = FileManager("/srp_correct.py")
    arquivo.read()
    arquivo.compress()
