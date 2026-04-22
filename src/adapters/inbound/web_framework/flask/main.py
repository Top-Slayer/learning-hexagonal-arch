from flask import Flask, jsonify, request

from applications.create_new_user import CreateNewUserUseCase
from ports.web_framework_port import WebFrameworkPort


class FlaskAdapter(WebFrameworkPort):
    def __init__(self, create_new_user_use_case: CreateNewUserUseCase) -> None:
        self.create_new_user_use_case = create_new_user_use_case

    def create_app(self) -> Flask:
        app = Flask(__name__)

        @app.get("/status")
        def status() -> tuple:
            return jsonify(self.status()), 200

        @app.post("/users")
        def create_user() -> tuple:
            payload = request.get_json(force=True) or {}
            result = self.create_new_user_use_case.execute(
                name=payload["name"],
                age=payload["age"],
            )
            return jsonify(result), 201

        return app

    def status(self) -> dict:
        return {"status": True}


def create_app(
    create_new_user_use_case: CreateNewUserUseCase,
    port: WebFrameworkPort | None = None,
) -> Flask:
    web_framework = port or FlaskAdapter(create_new_user_use_case)
    return web_framework.create_app()
