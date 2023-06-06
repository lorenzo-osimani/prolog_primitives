from python_Primitives_Server import DistributedElements
from generatedProto import primitiveService_pb2 as primitiveMsg
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from python_Primitives_Server import Utils
from . import Collections

class __TheoryToSchemaPrimitive(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        arg0 = request.arguments[0]
        if(arg0.HasField("var")):
            schema_name = str(Utils.parseArgumentMsg(
                next(request.inspectKb(
                    primitiveMsg.InspectKbMsg.STATIC,
                    [(primitiveMsg.InspectKbMsg.STARTS_WITH, "schema_name")])
                ).arguments[0].struct.arguments[0]
            ))
                        
            attributes = list()
            for i in request.inspectKb(
                primitiveMsg.InspectKbMsg.STATIC,
                [(primitiveMsg.InspectKbMsg.STARTS_WITH, "attribute")]):    
                if(i == None and len(attributes) == 0 ):
                    yield request.replyFail()
                elif(i != None):
                    fact = i.arguments[0].struct
                    index = int(Utils.parseArgumentMsg(fact.arguments[0]))
                    name = str(Utils.parseArgumentMsg(fact.arguments[1]))
                    type = Collections.Attribute.parseTypeFromArgumentMsg(fact.arguments[2])
                    attributes.insert(index, Collections.Attribute(name, type))
                 
            targets = list()     
            targetFact = next(request.inspectKb(
                primitiveMsg.InspectKbMsg.STATIC,
                [(primitiveMsg.InspectKbMsg.STARTS_WITH, "schema_target")]))
            if(targetFact == None):
                yield request.replyFail()
            else:
                targets = Utils.parseArgumentMsgList(targetFact.arguments[0].struct.arguments[0])
            substitutions = {
                arg0.var: basicMsg.ArgumentMsg(constant=Collections
                                               .SharedCollections()
                                               .addSchema(Collections.Schema(schema_name, attributes, targets))) 
                }
            yield request.replySuccess(substitutions, hasNext=False)
        else:
            request.replyFail()
            
            
theoryToSchemaPrimitive = DistributedElements.DistributedPrimitiveWrapper("theoryToSchema", 1, __TheoryToSchemaPrimitive())