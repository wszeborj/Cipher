import json


class FileHandler:
    @staticmethod
    def open_file(loaded_file_path: str):
        try:
            with open(f"{loaded_file_path}", "r") as file:
                return json.load(file)
        except OSError as err:
            print(f"{err=}, {type(err)=}")

    @staticmethod
    def save_file(
        file_path_to_save: str, data: list[dict], operation: str = "w"
    ) -> None:
        try:
            if operation == "a":
                with open(f"{file_path_to_save}", "r") as json_file:
                    loaded_data = json.load(json_file)
                    data.extend(loaded_data)

            with open(f"{file_path_to_save}", "w") as json_file:
                json.dump(data, json_file)
        except OSError as err:
            print(f"{err=}, {type(err)=}")


def main():
    pass


if __name__ == "__main__":
    main()
