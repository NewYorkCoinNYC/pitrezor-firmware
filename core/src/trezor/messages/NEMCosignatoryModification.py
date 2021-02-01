# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEMModificationType = Literal[1, 2]
    except ImportError:
        pass


class NEMCosignatoryModification(p.MessageType):

    def __init__(
        self,
        type: EnumTypeNEMModificationType = None,
        public_key: bytes = None,
    ) -> None:
        self.type = type
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("NEMModificationType", (1, 2)), 0),
            2: ('public_key', p.BytesType, 0),
        }
