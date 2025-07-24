from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RandomNumberRequest(_message.Message):
    __slots__ = ("min", "max", "seed", "count", "unique", "output_duration")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    seed: int
    count: int
    unique: bool
    output_duration: bool
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ..., seed: _Optional[int] = ..., count: _Optional[int] = ..., unique: bool = ..., output_duration: bool = ...) -> None: ...

class RandomNumberResponse(_message.Message):
    __slots__ = ("numbers", "output_duration", "seed_used")
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    SEED_USED_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    output_duration: str
    seed_used: int
    def __init__(self, numbers: _Optional[_Iterable[int]] = ..., output_duration: _Optional[str] = ..., seed_used: _Optional[int] = ...) -> None: ...
