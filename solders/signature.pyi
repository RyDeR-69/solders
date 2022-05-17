from typing import ClassVar, Sequence, Union, List

class Signature:
    LENGTH: ClassVar[int]
    def __init__(self, signature_slice: bytes) -> None: ...
    @staticmethod
    def new_unique() -> "Signature": ...
    @staticmethod
    def default() -> "Signature": ...
    @staticmethod
    def from_string(s: str) -> "Signature": ...
    def verify(self, pubkey_bytes: Union[bytes, Sequence[int]], message_bytes: bytes) -> bool: ...
    def to_bytes_array(self) -> List[int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "Signature", op: int) -> bool: ...
    def __hash__(self) -> int: ...