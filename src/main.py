from adapters.inbound.web_framework.fastapi.main import create_app
from applications.create_new_user import CreateNewUserUseCase

create_new_user_use_case = CreateNewUserUseCase()
app = create_app(create_new_user_use_case=create_new_user_use_case)
