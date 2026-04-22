from fastapi import FastAPI

from applications.create_new_user import CreateNewUserUseCase
from ports.web_framework_port import WebFrameworkPort

from adapters.inbound.web_framework.fastapi.dtos import CreateUserRequest


class FastAPIAdapter(WebFrameworkPort):
    def __init__(self, create_new_user_use_case: CreateNewUserUseCase) -> None:
        self.create_new_user_use_case = create_new_user_use_case

    def create_app(self) -> FastAPI:
        app = FastAPI()
        app.get("/status")(self.status)
        app.post("/users")(self.create_user)

        return app

    def create_user(self, payload: CreateUserRequest) -> dict:
        return self.create_new_user_use_case.execute(
            name=payload.name,
            age=payload.age,
        )

    def status(self) -> dict:
        return {"status": True}

def create_app(
    create_new_user_use_case: CreateNewUserUseCase,
) -> FastAPI:
    return FastAPIAdapter(create_new_user_use_case).create_app()
