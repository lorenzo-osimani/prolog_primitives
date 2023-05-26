import basicMessages_pb2 as _basicMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainErrorMsg(_message.Message):
    __slots__ = ["culprit", "expectedDomain"]
    CULPRIT_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDDOMAIN_FIELD_NUMBER: _ClassVar[int]
    culprit: _basicMessages_pb2.ArgumentMsg
    expectedDomain: str
    def __init__(self, expectedDomain: _Optional[str] = ..., culprit: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...

class EvaluationErrorMsg(_message.Message):
    __slots__ = ["errorType"]
    ERRORTYPE_FIELD_NUMBER: _ClassVar[int]
    errorType: str
    def __init__(self, errorType: _Optional[str] = ...) -> None: ...

class ExistenceErrorMsg(_message.Message):
    __slots__ = ["culprit", "expectedObject"]
    CULPRIT_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDOBJECT_FIELD_NUMBER: _ClassVar[int]
    culprit: _basicMessages_pb2.ArgumentMsg
    expectedObject: str
    def __init__(self, expectedObject: _Optional[str] = ..., culprit: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...

class HaltExceptionMsg(_message.Message):
    __slots__ = ["exitStatus"]
    EXITSTATUS_FIELD_NUMBER: _ClassVar[int]
    exitStatus: int
    def __init__(self, exitStatus: _Optional[int] = ...) -> None: ...

class InitializationIssueMsg(_message.Message):
    __slots__ = ["goal"]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    goal: _basicMessages_pb2.StructMsg
    def __init__(self, goal: _Optional[_Union[_basicMessages_pb2.StructMsg, _Mapping]] = ...) -> None: ...

class InstantiationErrorMsg(_message.Message):
    __slots__ = ["culprit"]
    CULPRIT_FIELD_NUMBER: _ClassVar[int]
    culprit: _basicMessages_pb2.ArgumentMsg
    def __init__(self, culprit: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...

class LogicErrorMsg(_message.Message):
    __slots__ = ["domainError", "evaluationError", "existenceError", "extraData", "instantiationError", "messageError", "permissionError", "representationError", "syntaxError", "systemError", "type", "typeError"]
    DOMAINERROR_FIELD_NUMBER: _ClassVar[int]
    EVALUATIONERROR_FIELD_NUMBER: _ClassVar[int]
    EXISTENCEERROR_FIELD_NUMBER: _ClassVar[int]
    EXTRADATA_FIELD_NUMBER: _ClassVar[int]
    INSTANTIATIONERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGEERROR_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONERROR_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIONERROR_FIELD_NUMBER: _ClassVar[int]
    SYNTAXERROR_FIELD_NUMBER: _ClassVar[int]
    SYSTEMERROR_FIELD_NUMBER: _ClassVar[int]
    TYPEERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    domainError: DomainErrorMsg
    evaluationError: EvaluationErrorMsg
    existenceError: ExistenceErrorMsg
    extraData: _basicMessages_pb2.ArgumentMsg
    instantiationError: InstantiationErrorMsg
    messageError: MessageErrorMsg
    permissionError: PermissionErrorMsg
    representationError: RepresentationErrorMsg
    syntaxError: SyntaxErrorMsg
    systemError: SystemErrorMsg
    type: _basicMessages_pb2.StructMsg
    typeError: TypeErrorMsg
    def __init__(self, type: _Optional[_Union[_basicMessages_pb2.StructMsg, _Mapping]] = ..., extraData: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ..., domainError: _Optional[_Union[DomainErrorMsg, _Mapping]] = ..., evaluationError: _Optional[_Union[EvaluationErrorMsg, _Mapping]] = ..., existenceError: _Optional[_Union[ExistenceErrorMsg, _Mapping]] = ..., instantiationError: _Optional[_Union[InstantiationErrorMsg, _Mapping]] = ..., messageError: _Optional[_Union[MessageErrorMsg, _Mapping]] = ..., permissionError: _Optional[_Union[PermissionErrorMsg, _Mapping]] = ..., representationError: _Optional[_Union[RepresentationErrorMsg, _Mapping]] = ..., syntaxError: _Optional[_Union[SyntaxErrorMsg, _Mapping]] = ..., systemError: _Optional[_Union[SystemErrorMsg, _Mapping]] = ..., typeError: _Optional[_Union[TypeErrorMsg, _Mapping]] = ...) -> None: ...

class MessageErrorMsg(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MissingPredicateMsg(_message.Message):
    __slots__ = ["signature"]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signature: _basicMessages_pb2.SignatureMsg
    def __init__(self, signature: _Optional[_Union[_basicMessages_pb2.SignatureMsg, _Mapping]] = ...) -> None: ...

class PermissionErrorMsg(_message.Message):
    __slots__ = ["culprit", "operation", "permission"]
    CULPRIT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    culprit: _basicMessages_pb2.ArgumentMsg
    operation: str
    permission: str
    def __init__(self, operation: _Optional[str] = ..., permission: _Optional[str] = ..., culprit: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...

class RepresentationErrorMsg(_message.Message):
    __slots__ = ["limit"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: str
    def __init__(self, limit: _Optional[str] = ...) -> None: ...

class ResolutionExceptionMsg(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SyntaxErrorMsg(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SystemErrorMsg(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TimeOutExceptionMsg(_message.Message):
    __slots__ = ["exceededDuration"]
    EXCEEDEDDURATION_FIELD_NUMBER: _ClassVar[int]
    exceededDuration: int
    def __init__(self, exceededDuration: _Optional[int] = ...) -> None: ...

class TypeErrorMsg(_message.Message):
    __slots__ = ["culprit", "expectedType"]
    CULPRIT_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDTYPE_FIELD_NUMBER: _ClassVar[int]
    culprit: _basicMessages_pb2.ArgumentMsg
    expectedType: str
    def __init__(self, expectedType: _Optional[str] = ..., culprit: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...
