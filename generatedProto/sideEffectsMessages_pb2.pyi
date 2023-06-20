from . import basicMessages_pb2 as _basicMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlterChannelsMsg(_message.Message):
    __slots__ = ["close", "modify", "write"]
    class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class CloseChannels(_message.Message):
        __slots__ = ["channelType", "channels"]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        CHANNELTYPE_FIELD_NUMBER: _ClassVar[int]
        channelType: AlterChannelsMsg.ChannelType
        channels: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, channels: _Optional[_Iterable[str]] = ..., channelType: _Optional[_Union[AlterChannelsMsg.ChannelType, str]] = ...) -> None: ...
    class ModifyChannels(_message.Message):
        __slots__ = ["channelType", "channels", "opType"]
        class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class ChannelsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        CHANNELTYPE_FIELD_NUMBER: _ClassVar[int]
        OPEN: AlterChannelsMsg.ModifyChannels.OpType
        OPTYPE_FIELD_NUMBER: _ClassVar[int]
        RESET: AlterChannelsMsg.ModifyChannels.OpType
        channelType: AlterChannelsMsg.ChannelType
        channels: _containers.ScalarMap[str, str]
        opType: AlterChannelsMsg.ModifyChannels.OpType
        def __init__(self, channels: _Optional[_Mapping[str, str]] = ..., opType: _Optional[_Union[AlterChannelsMsg.ModifyChannels.OpType, str]] = ..., channelType: _Optional[_Union[AlterChannelsMsg.ChannelType, str]] = ...) -> None: ...
    class WriteOnOutputs(_message.Message):
        __slots__ = ["channels"]
        class ChannelsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: AlterChannelsMsg.WriteOnOutputs.ContentMsg
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AlterChannelsMsg.WriteOnOutputs.ContentMsg, _Mapping]] = ...) -> None: ...
        class ContentMsg(_message.Message):
            __slots__ = ["messages"]
            MESSAGES_FIELD_NUMBER: _ClassVar[int]
            messages: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, messages: _Optional[_Iterable[str]] = ...) -> None: ...
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        channels: _containers.MessageMap[str, AlterChannelsMsg.WriteOnOutputs.ContentMsg]
        def __init__(self, channels: _Optional[_Mapping[str, AlterChannelsMsg.WriteOnOutputs.ContentMsg]] = ...) -> None: ...
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    INPUT: AlterChannelsMsg.ChannelType
    MODIFY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT: AlterChannelsMsg.ChannelType
    WRITE_FIELD_NUMBER: _ClassVar[int]
    close: AlterChannelsMsg.CloseChannels
    modify: AlterChannelsMsg.ModifyChannels
    write: WriteOnOutputChannelMsg
    def __init__(self, modify: _Optional[_Union[AlterChannelsMsg.ModifyChannels, _Mapping]] = ..., close: _Optional[_Union[AlterChannelsMsg.CloseChannels, _Mapping]] = ..., write: _Optional[_Union[WriteOnOutputChannelMsg, _Mapping]] = ...) -> None: ...

class AlterCustomDataMsg(_message.Message):
    __slots__ = ["data", "type"]
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    SET_DURABLE: AlterCustomDataMsg.OpType
    SET_EPHEMERAL: AlterCustomDataMsg.OpType
    SET_PERSISTENT: AlterCustomDataMsg.OpType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    data: _containers.ScalarMap[str, str]
    type: AlterCustomDataMsg.OpType
    def __init__(self, type: _Optional[_Union[AlterCustomDataMsg.OpType, str]] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AlterFlagsMsg(_message.Message):
    __slots__ = ["flags", "operationType"]
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class FlagsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _basicMessages_pb2.ArgumentMsg
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...
    CLEAR: AlterFlagsMsg.OpType
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    RESET: AlterFlagsMsg.OpType
    SET: AlterFlagsMsg.OpType
    flags: _containers.MessageMap[str, _basicMessages_pb2.ArgumentMsg]
    operationType: AlterFlagsMsg.OpType
    def __init__(self, operationType: _Optional[_Union[AlterFlagsMsg.OpType, str]] = ..., flags: _Optional[_Mapping[str, _basicMessages_pb2.ArgumentMsg]] = ...) -> None: ...

class AlterOperatorsMsg(_message.Message):
    __slots__ = ["operationType", "operators"]
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    OPERATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    REMOVE: AlterOperatorsMsg.OpType
    RESET: AlterOperatorsMsg.OpType
    SET: AlterOperatorsMsg.OpType
    operationType: AlterOperatorsMsg.OpType
    operators: _containers.RepeatedCompositeFieldContainer[_basicMessages_pb2.OperatorMsg]
    def __init__(self, operationType: _Optional[_Union[AlterOperatorsMsg.OpType, str]] = ..., operators: _Optional[_Iterable[_Union[_basicMessages_pb2.OperatorMsg, _Mapping]]] = ...) -> None: ...

class AlterRuntimeMsg(_message.Message):
    __slots__ = ["libraries", "operationType"]
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    LOAD: AlterRuntimeMsg.OpType
    OPERATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    RESET: AlterRuntimeMsg.OpType
    UNLOAD: AlterRuntimeMsg.OpType
    UPDATE: AlterRuntimeMsg.OpType
    libraries: _containers.RepeatedScalarFieldContainer[str]
    operationType: AlterRuntimeMsg.OpType
    def __init__(self, operationType: _Optional[_Union[AlterRuntimeMsg.OpType, str]] = ..., libraries: _Optional[_Iterable[str]] = ...) -> None: ...

class SetClausesOfKBMsg(_message.Message):
    __slots__ = ["clauses", "kbType", "onTop", "operationType"]
    class KbType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADD: SetClausesOfKBMsg.OpType
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC: SetClausesOfKBMsg.KbType
    KBTYPE_FIELD_NUMBER: _ClassVar[int]
    ONTOP_FIELD_NUMBER: _ClassVar[int]
    OPERATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    REMOVE: SetClausesOfKBMsg.OpType
    RESET: SetClausesOfKBMsg.OpType
    STATIC: SetClausesOfKBMsg.KbType
    clauses: _containers.RepeatedCompositeFieldContainer[_basicMessages_pb2.StructMsg]
    kbType: SetClausesOfKBMsg.KbType
    onTop: bool
    operationType: SetClausesOfKBMsg.OpType
    def __init__(self, kbType: _Optional[_Union[SetClausesOfKBMsg.KbType, str]] = ..., operationType: _Optional[_Union[SetClausesOfKBMsg.OpType, str]] = ..., onTop: bool = ..., clauses: _Optional[_Iterable[_Union[_basicMessages_pb2.StructMsg, _Mapping]]] = ...) -> None: ...

class SideEffectMsg(_message.Message):
    __slots__ = ["channels", "clauses", "customData", "flags", "operators", "runtime"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMDATA_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    channels: AlterChannelsMsg
    clauses: SetClausesOfKBMsg
    customData: AlterCustomDataMsg
    flags: AlterFlagsMsg
    operators: AlterOperatorsMsg
    runtime: AlterRuntimeMsg
    def __init__(self, clauses: _Optional[_Union[SetClausesOfKBMsg, _Mapping]] = ..., flags: _Optional[_Union[AlterFlagsMsg, _Mapping]] = ..., runtime: _Optional[_Union[AlterRuntimeMsg, _Mapping]] = ..., operators: _Optional[_Union[AlterOperatorsMsg, _Mapping]] = ..., channels: _Optional[_Union[AlterChannelsMsg, _Mapping]] = ..., customData: _Optional[_Union[AlterCustomDataMsg, _Mapping]] = ...) -> None: ...

class UpdateFromSessionMsg(_message.Message):
    __slots__ = ["type"]
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DYNAMIC_KB: UpdateFromSessionMsg.UpdateType
    FLAGS: UpdateFromSessionMsg.UpdateType
    INPUT_CHANNELS: UpdateFromSessionMsg.UpdateType
    OPERATORS: UpdateFromSessionMsg.UpdateType
    OUTPUT_CHANNELS: UpdateFromSessionMsg.UpdateType
    STATIC_KB: UpdateFromSessionMsg.UpdateType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: UpdateFromSessionMsg.UpdateType
    def __init__(self, type: _Optional[_Union[UpdateFromSessionMsg.UpdateType, str]] = ...) -> None: ...

class WriteOnOutputChannelMsg(_message.Message):
    __slots__ = ["messages"]
    class Messages(_message.Message):
        __slots__ = ["message"]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, message: _Optional[_Iterable[str]] = ...) -> None: ...
    class MessagesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: WriteOnOutputChannelMsg.Messages
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[WriteOnOutputChannelMsg.Messages, _Mapping]] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.MessageMap[str, WriteOnOutputChannelMsg.Messages]
    def __init__(self, messages: _Optional[_Mapping[str, WriteOnOutputChannelMsg.Messages]] = ...) -> None: ...
