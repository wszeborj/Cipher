from dataclasses import dataclass, asdict


@dataclass
class Text:
    text: str
    status: bool | str
    rot_type: int

    def __post_init__(self):
        """
        pass
        """
        if self.status:
            self.status = 'encrypted'
        else:
            self.status = 'decrypted'


class Buffer:
    def __init__(self):
        self.__data = []

    @property
    def data(self):
        return self.__data

    def add(self, text: Text):
        self.__data.append(text)

    def show_all(self):
        for t in self.__data:
            print(t)
