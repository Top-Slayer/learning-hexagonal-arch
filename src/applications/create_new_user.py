from domains.user import User


class CreateNewUserUseCase:
    def execute(self, name: str, age: int) -> dict:
        user = User(name=name, age=age)
        return {
            "status": True,
            "user": {
                "name": user.name,
                "age": user.age,
            },
        }
