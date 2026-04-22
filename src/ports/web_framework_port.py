from abc import ABC, abstractmethod
from typing import Any

class WebFrameworkPort(ABC):
    @abstractmethod
    def create_user(self, payload: Any) -> dict:
        raise NotImplementedError

    @abstractmethod
    def status(self) -> dict:
        raise NotImplementedError
