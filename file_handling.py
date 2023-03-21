import os


class FileHandler:
    @staticmethod
    def open_file(loaded_file_path: str):
        try:
            with open(loaded_file_path, 'r') as file:
                return file.read()
        except OSError as err:
            print(f'{err=}, {type(err)=}')

    @staticmethod
    def save_file(file_path_to_save: str, data: str):
        if os.path.exists(file_path_to_save):
            operation = 'a'
        else:
            operation = 'w'

        try:
            with open(file_path_to_save, operation) as file:
                file.write(data)
        except OSError as err:
            print(f'{err=}, {type(err)=}')


def main():
    pass


if __name__ == '__main__':
    main()
