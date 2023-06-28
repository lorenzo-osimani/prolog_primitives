import sys
sys.path.append('../generatedProto')

import unittest
from prolog_primitives.basic.PrimitiveWrapper import serve
from prolog_primitives.basic import DistributedElements
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator

class TestMyClass(unittest.TestCase):
    # test methods' names should begin with `test_`
    def test_my_method(self):
        serve(NtPrimitive(), "nt", 1, 8081, "customLibrary")
        
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
