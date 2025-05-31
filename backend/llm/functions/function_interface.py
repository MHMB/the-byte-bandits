from abc import abstractmethod, ABC
from typing import Tuple, Dict, Type, Optional

from models.stream_response import StreamResponse

class Function(ABC):

    @classmethod
    @abstractmethod
    async def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        pass

    @classmethod
    @abstractmethod
    def get_name(cls):
        pass

    @classmethod
    @abstractmethod
    def get_props(cls) -> Dict:
        pass
