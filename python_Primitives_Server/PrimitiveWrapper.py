import grpc

from generatedProto import primitiveService_pb2_grpc as Server
from generatedProto import primitiveService_pb2 as primitivesMsg
from generatedProto import basicMessages_pb2 as basicMsg
from . import DistributedElements
from . import Session
from queue import Queue
from concurrent import futures
from . import DBManager

class GenericPrimitive(Server.GenericPrimitiveService):
    primitive: DistributedElements.DistributedPrimitive
    functor: str = ""
    arity: int = 0
    executor: futures.Executor
    
    def __init__(self, primitive: DistributedElements.DistributedPrimitive, functor: str, arity: int, executor):  
        self.primitive = primitive
        self.functor = functor
        self.arity = arity
        self.executor = executor
        

    def getSignature(self, request, context):
        signature = (self.functor, self.arity)
        return basicMsg.SignatureMsg(name=signature[0], arity=signature[1])

    def callPrimitive(self, request_iterator, context):
        queue = Queue[primitivesMsg.GeneratorMsg]()
        def messageHandling():
            session: Session.ServerSession = None
            for value in request_iterator:
                msg: primitivesMsg.SolverMsg = value
                if(session == None and msg.request.IsInitialized()):
                    session = Session.ServerSession(
                        primitive = self.primitive,
                        request = msg.request,
                        queue = queue)
                else:
                    self.executor.submit(session.handleMessage, msg)
        
        self.executor.submit(messageHandling)
            
        while True:
            msg: primitivesMsg.GeneratorMsg = queue.get()
            yield msg               

def serve(primitive: DistributedElements.DistributedPrimitiveWrapper, port: int = 8080, libraryName: str = ""):
    try:
        executor = futures.ThreadPoolExecutor()
        service = GenericPrimitive(primitive.primitive, primitive.functor, primitive.arity, executor)
        server = grpc.server(executor)
        Server.add_GenericPrimitiveServiceServicer_to_server(service, server)
        server.add_insecure_port('[::]:' + str(port))
        server.start()
        DBManager.addPrimitive(service.functor, service.arity, libraryName, "localhost", port)
        print("Server started, listening on " + str(port))
        server.wait_for_termination()
    except (Exception, KeyboardInterrupt, SystemExit) as inst:
        print(inst.with_traceback)
        DBManager.deletePrimitive(service.functor, service.arity, service.libraryName)
        

        
        

