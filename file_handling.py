import os
import tkinter.filedialog


class FileHandler:
    def open_file(self, loaded_file_path):
        try:
            with open(loaded_file_path, 'r') as file:
                return file.read()
        except OSError as err:
            print(f'{err=}, {type(err)=}')

    def write_file(self, file_path_to_save, data):
        if os.path.exists(file_path_to_save):
            operation = 'a'
        else:
            operation = 'w'

        try:
            with open(file_path_to_save, operation) as file:
                file.write(data)
        except OSError as err:
            print(f'{err=}, {type(err)=}')


class FileManager:
    def __init__(self):
        self.handler = FileHandler()

    def load_file(self):
        path_file = tkinter.filedialog.askopenfilename(
            title='Select file to load',
            filetypes=[('text file', '.txt')],
            initialdir=os.getcwd())
        self.handler.open_file(path_file)

    def save_file(self, data=''):
        path_file = tkinter.filedialog.asksaveasfilename(
            title='Save file as *.txt',
            defaultextension='.txt',
            initialdir=os.getcwd())
        self.handler.write_file(path_file, data)


def main():
    f = FileManager()
    # f.load_file()
    data = 'zupa'
    f.save_file(data)


if __name__ == '__main__':
    main()
