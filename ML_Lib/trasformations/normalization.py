from python_Primitives_Server import DistributedElements
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
from .transformationClass import Normalization, Pipeline

class __Normalize(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        transf_in_ref = request.arguments[0]
        attributes = request.arguments[1]
        transf_out_ref = request.arguments[2]
        
        if(not transf_in_ref.HasField('var') and not attributes.HasField('var') and transf_out_ref.HasField('var')):
            transf_in_id = Utils.parseArgumentMsg(transf_in_ref)
            transf: Pipeline = SharedCollections().getPipeline(transf_in_id)
            listOfAttr = Utils.parseArgumentMsgList(attributes)
            if(listOfAttr != []):
                attributes = listOfAttr
            else:
                attributes = [Utils.parseArgumentMsg(attributes)]
                
            id = SharedCollections().addPipeline(transf.append(dict.fromkeys(attributes, [Normalization()])))
            yield request.replySuccess(substitutions={
                transf_out_ref.var: basicMsg.ArgumentMsg(constant=id)
                }, hasNext=False)
        else:
            yield request.replyFail()
            
            
normalizePrimitive = DistributedElements.DistributedPrimitiveWrapper("normalize", 3, __Normalize())