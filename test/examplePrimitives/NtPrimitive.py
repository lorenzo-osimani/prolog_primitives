import logging
from python_Primitives_Server import serve
from python_Primitives_Server import DistributedElements

import python_Primitives_Server.generatedProto.basicMessages_pb2 as basicMsg
from typing import Generator

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
    
if __name__ == '__main__':
    logging.basicConfig()
    serve(NtPrimitive(), "nt", 1, 8081, "customLibrary")
    
        