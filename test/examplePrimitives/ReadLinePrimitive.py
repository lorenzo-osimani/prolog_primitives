import logging
import sys
sys.path.append('./generatedProto')

import prolog_primitives.generatedProto.basicMessages_pb2 as basicMsg
from prolog_primitives.basic import PrimitiveWrapper
from prolog_primitives.basic import  DistributedElements, Utils
from typing import Generator

class ReadPrimitive(DistributedElements.DistribuitedPrimitive):

    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        channelName = request.arguments[0].struct.functor
        while(True):
            char = request.readLine(channelName)
            if(char != ""):
                substitutions = {}
                substitutions[request.arguments[1].var] = Utils.buildConstantArgumentMsg(char)
                yield request.replySuccess(substitutions = substitutions)
            else:
                yield request.replyFail()
    
if __name__ == '__main__':
    logging.basicConfig()
    PrimitiveWrapper.serve(ReadPrimitive(), "readLine", 2, 8082, "customLibrary")
    
        