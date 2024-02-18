# file_manager_srp.py

from pathlib import Path
from zipfile import ZipFile

#Versão corrigida do código
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


if __name__ == '__main__':
    #Exemplo de uso
    arquivoZipar = ZipFileManager("/srp_mistaking.py")
    arquivoZipar.decompress()

    arquivoLeitura = FileManager("/srp_mistaking.py")
    arquivoLeitura.read()
    arquivoLeitura.write()

    arquivoZipar.compress()
