from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArgumentMsg(_message.Message):
    __slots__ = ["constant", "struct", "var"]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    constant: str
    struct: StructMsg
    var: str
    def __init__(self, struct: _Optional[_Union[StructMsg, _Mapping]] = ..., var: _Optional[str] = ..., constant: _Optional[str] = ...) -> None: ...

class ChannelsMsg(_message.Message):
    __slots__ = ["channels"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channels: _Optional[_Iterable[str]] = ...) -> None: ...

class CustomDataMsg(_message.Message):
    __slots__ = ["durableData", "ephemeralData", "persistentData"]
    class DurableDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class EphemeralDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PersistentDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DURABLEDATA_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALDATA_FIELD_NUMBER: _ClassVar[int]
    PERSISTENTDATA_FIELD_NUMBER: _ClassVar[int]
    durableData: _containers.ScalarMap[str, str]
    ephemeralData: _containers.ScalarMap[str, str]
    persistentData: _containers.ScalarMap[str, str]
    def __init__(self, persistentData: _Optional[_Mapping[str, str]] = ..., durableData: _Optional[_Mapping[str, str]] = ..., ephemeralData: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EmptyMsg(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutionContextMsg(_message.Message):
    __slots__ = ["elapsedTime", "endTime", "maxDuration", "procedure", "remainingTime", "startTime", "substitutions"]
    class SubstitutionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ArgumentMsg
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ArgumentMsg, _Mapping]] = ...) -> None: ...
    ELAPSEDTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    MAXDURATION_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    REMAININGTIME_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    elapsedTime: int
    endTime: int
    maxDuration: int
    procedure: StructMsg
    remainingTime: int
    startTime: int
    substitutions: _containers.MessageMap[str, ArgumentMsg]
    def __init__(self, procedure: _Optional[_Union[StructMsg, _Mapping]] = ..., substitutions: _Optional[_Mapping[str, ArgumentMsg]] = ..., startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., remainingTime: _Optional[int] = ..., elapsedTime: _Optional[int] = ..., maxDuration: _Optional[int] = ...) -> None: ...

class FlagsMsg(_message.Message):
    __slots__ = ["flags"]
    class FlagsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ArgumentMsg
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ArgumentMsg, _Mapping]] = ...) -> None: ...
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.MessageMap[str, ArgumentMsg]
    def __init__(self, flags: _Optional[_Mapping[str, ArgumentMsg]] = ...) -> None: ...

class LibrariesMsg(_message.Message):
    __slots__ = ["libraries"]
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    libraries: _containers.RepeatedCompositeFieldContainer[LibraryMsg]
    def __init__(self, libraries: _Optional[_Iterable[_Union[LibraryMsg, _Mapping]]] = ...) -> None: ...

class LibraryMsg(_message.Message):
    __slots__ = ["alias", "clauses", "functionsSignatures", "operators", "primitives", "rulesSignatures"]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONSSIGNATURES_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVES_FIELD_NUMBER: _ClassVar[int]
    RULESSIGNATURES_FIELD_NUMBER: _ClassVar[int]
    alias: str
    clauses: _containers.RepeatedCompositeFieldContainer[StructMsg]
    functionsSignatures: _containers.RepeatedCompositeFieldContainer[SignatureMsg]
    operators: OperatorSetMsg
    primitives: _containers.RepeatedCompositeFieldContainer[SignatureMsg]
    rulesSignatures: _containers.RepeatedCompositeFieldContainer[SignatureMsg]
    def __init__(self, alias: _Optional[str] = ..., primitives: _Optional[_Iterable[_Union[SignatureMsg, _Mapping]]] = ..., rulesSignatures: _Optional[_Iterable[_Union[SignatureMsg, _Mapping]]] = ..., clauses: _Optional[_Iterable[_Union[StructMsg, _Mapping]]] = ..., functionsSignatures: _Optional[_Iterable[_Union[SignatureMsg, _Mapping]]] = ..., operators: _Optional[_Union[OperatorSetMsg, _Mapping]] = ...) -> None: ...

class LogicStacktraceMsg(_message.Message):
    __slots__ = ["logicStackTrace"]
    LOGICSTACKTRACE_FIELD_NUMBER: _ClassVar[int]
    logicStackTrace: _containers.RepeatedCompositeFieldContainer[StructMsg]
    def __init__(self, logicStackTrace: _Optional[_Iterable[_Union[StructMsg, _Mapping]]] = ...) -> None: ...

class OperatorMsg(_message.Message):
    __slots__ = ["functor", "priority", "specifier"]
    FUNCTOR_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SPECIFIER_FIELD_NUMBER: _ClassVar[int]
    functor: str
    priority: int
    specifier: str
    def __init__(self, functor: _Optional[str] = ..., specifier: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class OperatorSetMsg(_message.Message):
    __slots__ = ["operators"]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    operators: _containers.RepeatedCompositeFieldContainer[OperatorMsg]
    def __init__(self, operators: _Optional[_Iterable[_Union[OperatorMsg, _Mapping]]] = ...) -> None: ...

class SignatureMsg(_message.Message):
    __slots__ = ["arity", "name"]
    ARITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    arity: int
    name: str
    def __init__(self, name: _Optional[str] = ..., arity: _Optional[int] = ...) -> None: ...

class StructMsg(_message.Message):
    __slots__ = ["arguments", "functor"]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    FUNCTOR_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedCompositeFieldContainer[ArgumentMsg]
    functor: str
    def __init__(self, functor: _Optional[str] = ..., arguments: _Optional[_Iterable[_Union[ArgumentMsg, _Mapping]]] = ...) -> None: ...

class TheoryMsg(_message.Message):
    __slots__ = ["clauses"]
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    clauses: _containers.RepeatedCompositeFieldContainer[StructMsg]
    def __init__(self, clauses: _Optional[_Iterable[_Union[StructMsg, _Mapping]]] = ...) -> None: ...

class UnificatorMsg(_message.Message):
    __slots__ = ["unificator"]
    class UnificatorEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ArgumentMsg
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ArgumentMsg, _Mapping]] = ...) -> None: ...
    UNIFICATOR_FIELD_NUMBER: _ClassVar[int]
    unificator: _containers.MessageMap[str, ArgumentMsg]
    def __init__(self, unificator: _Optional[_Mapping[str, ArgumentMsg]] = ...) -> None: ...
