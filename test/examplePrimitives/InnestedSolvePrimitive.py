import logging
from python_Primitives_Server import serve
from python_Primitives_Server import DistributedElements
from typing import Generator

class InnestedPrimitive(DistributedElements.DistributedPrimitive):

    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        arg0 = request.arguments[0]
        for solution in request.subSolve(arg0.struct):
            if(solution.type == solution.SUCCESS):
                yield request.replySuccess(solution.substitutions, hasNext=solution.hasNext)
            elif(solution.type == solution.FAIL):
                yield request.replyFail()
            else:
                yield request.replyError(solution.error)
    
if __name__ == '__main__':
    logging.basicConfig()
    serve(InnestedPrimitive(), "solve", 1, 8080, "customLibrary")
    
        