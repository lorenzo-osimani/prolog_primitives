from python_Primitives_Server import DistributedElements
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
import tensorflow as tf
from .transformationClass import Pipeline
from ..schema.schemaClass import Attribute, Schema

class __SchemaTrasformation(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        schema_ref = request.arguments[0]
        transf_ref = request.arguments[1]
        
        if(not schema_ref.HasField('var') and transf_ref.HasField('var')):
            schema_id = Utils.parseArgumentMsg(schema_ref)
            
            id = SharedCollections().addPipeline(Pipeline(schema_id))
            yield request.replySuccess(substitutions={
                transf_ref.var: basicMsg.ArgumentMsg(constant=id)
                }, hasNext=False)
        elif(schema_ref.HasField('var') and not transf_ref.HasField('var')):
            transformation_id = Utils.parseArgumentMsg(transf_ref)
            transformation: Pipeline = SharedCollections().getPipeline(transformation_id)
            schema = SharedCollections().getSchema(transformation.originalSchemaId)
            
            inputs = transformation.computeFinalSchema()
                
            attributes = []
            for name, attr in inputs.items():
                try:
                    if(attr['shape'][1] > 1):
                        for i in range(attr['shape'][1]):
                            attributes.append(
                                Attribute(str(name)+"_"+str(i), tf.as_dtype(attr['dtype']))
                            )
                except:
                    attributes.append(
                        Attribute(name, tf.as_dtype(attr['dtype']))
                    )
            
            id = SharedCollections().addSchema(Schema(schema.name, attributes, schema.targets))
            yield request.replySuccess(substitutions = {
                schema_ref.var: basicMsg.ArgumentMsg(constant=id)
            }, hasNext=False)            
        else:
            yield request.replyFail()
            
            
schemaTrasformation = DistributedElements.DistributedPrimitiveWrapper("schema_trasformation", 2, __SchemaTrasformation())