
from . import DistributedElements
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from . import PrimitiveWrapper

# this is the main module of your app
# it is only required if your project must be runnable
# this is the script to be executed whenever some users writes `python -m python-Primitives-Server` on the command line, eg.
class NtPrimitive(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        arg0 = request.arguments[0]
        if(arg0.HasField("var")):
            n = 0
            while(True):
                substitutions = {}
                substitutions[arg0.var] = basicMsg.ArgumentMsg(constant=str(n))
                yield request.replySuccess(substitutions = substitutions)
                n += 1
        elif(arg0.HasField("constant") and int(arg0.constant)):
            yield request.replySuccess(hasNext = False)
        else:
            yield request.replyFail()
            
PrimitiveWrapper.serve(NtPrimitive(), "nt", 1, 8081, "customLibrary")