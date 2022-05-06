from typing import List, Union, Optional, ClassVar, Sequence

def is_on_curve(_bytes: bytes) -> bool: ...

class Pubkey:
    LENGTH: ClassVar[int]
    def __init__(self, pubkey_bytes: bytes) -> None: ...
    @staticmethod
    def new_unique() -> "Pubkey": ...
    @staticmethod
    def default() -> "Pubkey": ...
    @staticmethod
    def from_string(s: str) -> "Pubkey": ...
    @staticmethod
    def create_with_seed(
        from_public_key: "Pubkey", seed: str, program_id: "Pubkey"
    ) -> "Pubkey": ...
    @staticmethod
    def create_program_address(seeds: Sequence[bytes]) -> "Pubkey": ...
    @staticmethod
    def find_program_address(
        seeds: Sequence[bytes], program_id: "Pubkey"
    ) -> "Pubkey": ...
    def is_on_curve(self) -> bool: ...
    def string(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def __richcmp__(self, other: "Pubkey", op: int) -> bool: ...
    def __hash__(self) -> int: ...

class Keypair:
    def __init__(self) -> None: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "Keypair": ...
    @staticmethod
    def from_seed(seed: bytes) -> "Keypair": ...
    @staticmethod
    def from_base58_string(s: str) -> "Keypair": ...
    @staticmethod
    def from_seed_phrase_and_passphrase(
        seed_phrase: str, passphrase: str
    ) -> "Keypair": ...
    def secret(self) -> bytes: ...
    def pubkey(self) -> Pubkey: ...
    def sign_message(self, message: bytes) -> Signature: ...
    def to_bytes_array(self) -> List[int]: ...
    def to_base58_string(self) -> str: ...
    def __str__(self) -> str: ...
    def __bytes__(self) -> str: ...
    def __richcmp__(self, other: "Keypair", op: int) -> bool: ...
    def __hash__(self) -> int: ...

class Signature:
    def __init__(self, signature_slice: bytes) -> None: ...
    @staticmethod
    def new_unique() -> "Signature": ...
    @staticmethod
    def default() -> "Signature": ...
    @staticmethod
    def from_string(s: str) -> "Signature": ...
    def verify(self, pubkey_bytes: bytes, message_bytes: bytes) -> bool: ...
    def to_bytes_array(self) -> List[int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def to_string(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "Signature", op: int) -> bool: ...
    def __hash__(self) -> int: ...

class AccountMeta:
    def __init__(self, pubkey: Pubkey, is_signer: bool, is_writable: bool) -> None: ...
    @property
    def pubkey(self) -> Pubkey: ...
    @property
    def is_signer(self) -> bool: ...
    @property
    def is_writable(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "AccountMeta", op: int) -> bool: ...

class Instruction:
    def __init__(
        self, program_id: Pubkey, data: bytes, accounts: Sequence[AccountMeta]
    ) -> None: ...
    @property
    def program_id(self) -> Pubkey: ...
    @property
    def data(self) -> bytes: ...
    @property
    def accounts(self) -> List[AccountMeta]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "Instruction", op: int) -> bool: ...

class CompiledInstruction:
    def __init__(self, program_id_index: int, data: bytes, accounts: bytes) -> None: ...
    def program_id(self, program_ids: Sequence[Pubkey]) -> Pubkey: ...
    def program_id_index(self) -> int: ...
    def accounts(self) -> bytes: ...
    @property
    def data(self) -> bytes: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "CompiledInstruction", op: int) -> bool: ...

class Hash:
    def __init__(self, hash_bytes: Union[bytes, Sequence[int]]) -> None: ...
    def to_string(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def from_string(s: str) -> "Hash": ...
    @staticmethod
    def new_unique() -> "Hash": ...
    @staticmethod
    def default() -> "Hash": ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def __richcmp__(self, other: "Hash", op: int) -> bool: ...
    @staticmethod
    def hash(val: bytes) -> "Hash": ...
    def __hash__(self) -> int: ...

def decode_length(raw_bytes: bytes) -> tuple[int, int]: ...
def encode_length(value: int) -> List[int]: ...

class MessageHeader:
    LENGTH: ClassVar[int]
    def __init__(
        self,
        num_required_signatures: int,
        num_readonly_signed_accounts: int,
        num_readonly_unsigned_accounts: int,
    ) -> None: ...
    @staticmethod
    def default() -> "MessageHeader": ...
    @property
    def num_required_signatures(self) -> int: ...
    @property
    def num_readonly_signed_accounts(self) -> int: ...
    @property
    def num_readonly_unsigned_accounts(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class Message:
    def __init__(
        self, instructions: Sequence[Instruction], payer: Optional[Pubkey]
    ) -> None: ...
    @property
    def header(self) -> MessageHeader: ...
    @property
    def account_keys(self) -> List[Pubkey]: ...
    @property
    def recent_blockhash(self) -> Hash: ...
    @property
    def instructions(self) -> List[CompiledInstruction]: ...
    @staticmethod
    def new_with_blockhash(
        instructions: Sequence[Instruction], payer: Optional[Pubkey], blockhash: Hash
    ) -> "Message": ...
    @staticmethod
    def new_with_compiled_instructions(
        num_required_signatures: int,
        num_readonly_signed_accounts: int,
        num_readonly_unsigned_accounts: int,
        account_keys: Sequence[Pubkey],
        recent_blockhash: Hash,
        instructions: Sequence[CompiledInstruction],
    ) -> "Message": ...
    def hash(self) -> Hash: ...
    @staticmethod
    def hash_raw_message(message_bytes: bytes) -> Hash: ...
    def compile_instruction(self, ix: Instruction) -> CompiledInstruction: ...
    def serialize(self) -> bytes: ...
    def program_id(self, instruction_index: int) -> Optional[Pubkey]: ...
    def program_index(self, instruction_index: int) -> Optional[int]: ...
    def program_ids(self) -> List[Pubkey]: ...
    def is_key_passed_to_program(self, key_index: int) -> bool: ...
    def is_key_called_as_program(self, key_index: int) -> bool: ...
    def is_non_loader_key(self, key_index: int) -> bool: ...
    def program_position(self, index: int) -> Optional[int]: ...
    def maybe_executable(self, i: int) -> bool: ...
    def is_writable(self, i: int) -> bool: ...
    def is_signer(self, i: int) -> bool: ...
    def signer_keys(self) -> List[Pubkey]: ...
    def has_duplicates(self) -> bool: ...
    @staticmethod
    def default() -> "Message": ...
    @staticmethod
    def deserialize() -> "Message": ...
    def __richcmp__(self, other: "Message", op: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
