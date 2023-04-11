import json


class FileHandler:
    @staticmethod
    def open_file(loaded_file_path: str):
        try:
            with open(f"{loaded_file_path}.json", "r") as file:
                return json.load(file)
        except OSError as err:
            print(f"{err=}, {type(err)=}")

    @staticmethod
    def save_file(file_path_to_save: str, data: str, operation: str = "w") -> None:
        try:
            with open(f"{file_path_to_save}.json", operation) as file:
                json.dump(data, file)
        except OSError as err:
            print(f"{err=}, {type(err)=}")


def main():
    pass


if __name__ == "__main__":
    main()
