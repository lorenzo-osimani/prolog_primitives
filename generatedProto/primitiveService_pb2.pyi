from . import basicMessages_pb2 as _basicMessages_pb2
from . import sideEffectsMessages_pb2 as _sideEffectsMessages_pb2
from . import errorsMessages_pb2 as _errorsMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorMsg(_message.Message):
    __slots__ = ["cause", "context", "haltException", "initializationIssue", "logicError", "message", "missingPredicate", "resolutionException", "timeoutException"]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HALTEXCEPTION_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATIONISSUE_FIELD_NUMBER: _ClassVar[int]
    LOGICERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MISSINGPREDICATE_FIELD_NUMBER: _ClassVar[int]
    RESOLUTIONEXCEPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTEXCEPTION_FIELD_NUMBER: _ClassVar[int]
    cause: ErrorMsg
    context: _basicMessages_pb2.ExecutionContextMsg
    haltException: _errorsMessages_pb2.HaltExceptionMsg
    initializationIssue: _errorsMessages_pb2.InitializationIssueMsg
    logicError: _errorsMessages_pb2.LogicErrorMsg
    message: str
    missingPredicate: _errorsMessages_pb2.MissingPredicateMsg
    resolutionException: _errorsMessages_pb2.ResolutionExceptionMsg
    timeoutException: _errorsMessages_pb2.TimeOutExceptionMsg
    def __init__(self, message: _Optional[str] = ..., cause: _Optional[_Union[ErrorMsg, _Mapping]] = ..., context: _Optional[_Union[_basicMessages_pb2.ExecutionContextMsg, _Mapping]] = ..., initializationIssue: _Optional[_Union[_errorsMessages_pb2.InitializationIssueMsg, _Mapping]] = ..., missingPredicate: _Optional[_Union[_errorsMessages_pb2.MissingPredicateMsg, _Mapping]] = ..., haltException: _Optional[_Union[_errorsMessages_pb2.HaltExceptionMsg, _Mapping]] = ..., logicError: _Optional[_Union[_errorsMessages_pb2.LogicErrorMsg, _Mapping]] = ..., resolutionException: _Optional[_Union[_errorsMessages_pb2.ResolutionExceptionMsg, _Mapping]] = ..., timeoutException: _Optional[_Union[_errorsMessages_pb2.TimeOutExceptionMsg, _Mapping]] = ...) -> None: ...

class GeneratorMsg(_message.Message):
    __slots__ = ["request", "response"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    request: SubRequestMsg
    response: ResponseMsg
    def __init__(self, response: _Optional[_Union[ResponseMsg, _Mapping]] = ..., request: _Optional[_Union[SubRequestMsg, _Mapping]] = ...) -> None: ...

class GenericGetMsg(_message.Message):
    __slots__ = ["element"]
    class Element(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CUSTOM_DATA_STORE: GenericGetMsg.Element
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    FLAGS: GenericGetMsg.Element
    INPUT_CHANNELS: GenericGetMsg.Element
    LIBRARIES: GenericGetMsg.Element
    LOGIC_STACKTRACE: GenericGetMsg.Element
    OPERATORS: GenericGetMsg.Element
    OUTPUT_CHANNELS: GenericGetMsg.Element
    UNIFICATOR: GenericGetMsg.Element
    element: GenericGetMsg.Element
    def __init__(self, element: _Optional[_Union[GenericGetMsg.Element, str]] = ...) -> None: ...

class GenericGetResponse(_message.Message):
    __slots__ = ["channels", "customDataStore", "flags", "libraries", "logicStackTrace", "operators", "unificator"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMDATASTORE_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    LOGICSTACKTRACE_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    UNIFICATOR_FIELD_NUMBER: _ClassVar[int]
    channels: _basicMessages_pb2.ChannelsMsg
    customDataStore: _basicMessages_pb2.CustomDataMsg
    flags: _basicMessages_pb2.FlagsMsg
    libraries: _basicMessages_pb2.LibrariesMsg
    logicStackTrace: _basicMessages_pb2.LogicStacktraceMsg
    operators: _basicMessages_pb2.OperatorSetMsg
    unificator: _basicMessages_pb2.UnificatorMsg
    def __init__(self, logicStackTrace: _Optional[_Union[_basicMessages_pb2.LogicStacktraceMsg, _Mapping]] = ..., customDataStore: _Optional[_Union[_basicMessages_pb2.CustomDataMsg, _Mapping]] = ..., unificator: _Optional[_Union[_basicMessages_pb2.UnificatorMsg, _Mapping]] = ..., libraries: _Optional[_Union[_basicMessages_pb2.LibrariesMsg, _Mapping]] = ..., flags: _Optional[_Union[_basicMessages_pb2.FlagsMsg, _Mapping]] = ..., operators: _Optional[_Union[_basicMessages_pb2.OperatorSetMsg, _Mapping]] = ..., channels: _Optional[_Union[_basicMessages_pb2.ChannelsMsg, _Mapping]] = ...) -> None: ...

class InspectKbMsg(_message.Message):
    __slots__ = ["filters", "kbType", "maxClauses"]
    class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class KbType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class FilterMsg(_message.Message):
        __slots__ = ["argument", "type"]
        ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        argument: str
        type: InspectKbMsg.FilterType
        def __init__(self, type: _Optional[_Union[InspectKbMsg.FilterType, str]] = ..., argument: _Optional[str] = ...) -> None: ...
    BOTH: InspectKbMsg.KbType
    CONTAINS_FUNCTOR: InspectKbMsg.FilterType
    CONTAINS_TERM: InspectKbMsg.FilterType
    DYNAMIC: InspectKbMsg.KbType
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    KBTYPE_FIELD_NUMBER: _ClassVar[int]
    MAXCLAUSES_FIELD_NUMBER: _ClassVar[int]
    STARTS_WITH: InspectKbMsg.FilterType
    STATIC: InspectKbMsg.KbType
    filters: _containers.RepeatedCompositeFieldContainer[InspectKbMsg.FilterMsg]
    kbType: InspectKbMsg.KbType
    maxClauses: int
    def __init__(self, kbType: _Optional[_Union[InspectKbMsg.KbType, str]] = ..., maxClauses: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[InspectKbMsg.FilterMsg, _Mapping]]] = ...) -> None: ...

class LineMsg(_message.Message):
    __slots__ = ["channelName", "content", "failed"]
    CHANNELNAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    channelName: str
    content: str
    failed: bool
    def __init__(self, channelName: _Optional[str] = ..., failed: bool = ..., content: _Optional[str] = ...) -> None: ...

class ReadLineMsg(_message.Message):
    __slots__ = ["channelName"]
    CHANNELNAME_FIELD_NUMBER: _ClassVar[int]
    channelName: str
    def __init__(self, channelName: _Optional[str] = ...) -> None: ...

class RequestMsg(_message.Message):
    __slots__ = ["arguments", "context", "max_duration", "signature", "start_time"]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedCompositeFieldContainer[_basicMessages_pb2.ArgumentMsg]
    context: _basicMessages_pb2.ExecutionContextMsg
    max_duration: int
    signature: _basicMessages_pb2.SignatureMsg
    start_time: int
    def __init__(self, signature: _Optional[_Union[_basicMessages_pb2.SignatureMsg, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]]] = ..., context: _Optional[_Union[_basicMessages_pb2.ExecutionContextMsg, _Mapping]] = ..., start_time: _Optional[int] = ..., max_duration: _Optional[int] = ...) -> None: ...

class ResponseMsg(_message.Message):
    __slots__ = ["sideEffects", "solution"]
    SIDEEFFECTS_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    sideEffects: _containers.RepeatedCompositeFieldContainer[_sideEffectsMessages_pb2.SideEffectMsg]
    solution: SolutionMsg
    def __init__(self, solution: _Optional[_Union[SolutionMsg, _Mapping]] = ..., sideEffects: _Optional[_Iterable[_Union[_sideEffectsMessages_pb2.SideEffectMsg, _Mapping]]] = ...) -> None: ...

class SolutionMsg(_message.Message):
    __slots__ = ["error", "hasNext", "query", "substitutions", "type"]
    class SolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class SubstitutionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _basicMessages_pb2.ArgumentMsg
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_basicMessages_pb2.ArgumentMsg, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAIL: SolutionMsg.SolutionType
    HALT: SolutionMsg.SolutionType
    HASNEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS: SolutionMsg.SolutionType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    error: ErrorMsg
    hasNext: bool
    query: _basicMessages_pb2.StructMsg
    substitutions: _containers.MessageMap[str, _basicMessages_pb2.ArgumentMsg]
    type: SolutionMsg.SolutionType
    def __init__(self, type: _Optional[_Union[SolutionMsg.SolutionType, str]] = ..., query: _Optional[_Union[_basicMessages_pb2.StructMsg, _Mapping]] = ..., substitutions: _Optional[_Mapping[str, _basicMessages_pb2.ArgumentMsg]] = ..., error: _Optional[_Union[ErrorMsg, _Mapping]] = ..., hasNext: bool = ...) -> None: ...

class SolverMsg(_message.Message):
    __slots__ = ["next", "request", "response"]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    next: _basicMessages_pb2.EmptyMsg
    request: RequestMsg
    response: SubResponseMsg
    def __init__(self, request: _Optional[_Union[RequestMsg, _Mapping]] = ..., next: _Optional[_Union[_basicMessages_pb2.EmptyMsg, _Mapping]] = ..., response: _Optional[_Union[SubResponseMsg, _Mapping]] = ...) -> None: ...

class SubRequestMsg(_message.Message):
    __slots__ = ["genericGet", "id", "inspectKb", "readLine", "subSolve"]
    GENERICGET_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INSPECTKB_FIELD_NUMBER: _ClassVar[int]
    READLINE_FIELD_NUMBER: _ClassVar[int]
    SUBSOLVE_FIELD_NUMBER: _ClassVar[int]
    genericGet: GenericGetMsg
    id: str
    inspectKb: InspectKbMsg
    readLine: ReadLineMsg
    subSolve: SubSolveRequest
    def __init__(self, id: _Optional[str] = ..., subSolve: _Optional[_Union[SubSolveRequest, _Mapping]] = ..., readLine: _Optional[_Union[ReadLineMsg, _Mapping]] = ..., inspectKb: _Optional[_Union[InspectKbMsg, _Mapping]] = ..., genericGet: _Optional[_Union[GenericGetMsg, _Mapping]] = ...) -> None: ...

class SubResponseMsg(_message.Message):
    __slots__ = ["clause", "genericGet", "id", "line", "solution"]
    CLAUSE_FIELD_NUMBER: _ClassVar[int]
    GENERICGET_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    clause: _basicMessages_pb2.StructMsg
    genericGet: GenericGetResponse
    id: str
    line: LineMsg
    solution: ResponseMsg
    def __init__(self, id: _Optional[str] = ..., solution: _Optional[_Union[ResponseMsg, _Mapping]] = ..., line: _Optional[_Union[LineMsg, _Mapping]] = ..., clause: _Optional[_Union[_basicMessages_pb2.StructMsg, _Mapping]] = ..., genericGet: _Optional[_Union[GenericGetResponse, _Mapping]] = ...) -> None: ...

class SubSolveRequest(_message.Message):
    __slots__ = ["lazy", "limit", "query", "timeout"]
    LAZY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    lazy: bool
    limit: int
    query: _basicMessages_pb2.StructMsg
    timeout: int
    def __init__(self, query: _Optional[_Union[_basicMessages_pb2.StructMsg, _Mapping]] = ..., timeout: _Optional[int] = ..., lazy: bool = ..., limit: _Optional[int] = ...) -> None: ...
