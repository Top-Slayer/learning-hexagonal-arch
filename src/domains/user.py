class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def change_name(self, name: str) -> bool:
        if not name:
            return False
        else:
            self.name = name
            return True
