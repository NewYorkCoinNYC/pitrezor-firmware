# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoAddressParametersType import CardanoAddressParametersType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoGetAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 307

    def __init__(
        self,
        show_display: bool = None,
        protocol_magic: int = None,
        network_id: int = None,
        address_parameters: CardanoAddressParametersType = None,
    ) -> None:
        self.show_display = show_display
        self.protocol_magic = protocol_magic
        self.network_id = network_id
        self.address_parameters = address_parameters

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('show_display', p.BoolType, 0),
            3: ('protocol_magic', p.UVarintType, 0),
            4: ('network_id', p.UVarintType, 0),
            5: ('address_parameters', CardanoAddressParametersType, 0),
        }
