class ProcessWithFile:
    def __init__(self, file_name, file_mode, encoding='utf-8'):
        self.file_name = file_name
        self.file_mode = file_mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.file_mode, self.encoding)
        print(f'Файл {self.file_name} открыт')
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f'Файл {self.file_name} закрыт')


with ProcessWithFile('Values.txt', 'r') as file:
    content = file.read()
    print()

