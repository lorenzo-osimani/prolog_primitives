from python_Primitives_Server import DistributedElements
from generatedProto import primitiveService_pb2 as primitiveMsg
from generatedProto import basicMessages_pb2 as basicMsg
from generatedProto import errorsMessages_pb2 as errorMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
import tensorflow as tf
from .transformationClass import Transformation
from ..schema.schemaClass import Schema, Attribute, parseAttributeFromStruct
from .transformationClass import OneHotEncoder, Pipeline
from datasets import Dataset

class __Fit(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        transf_in_ref = request.arguments[0]
        dataset_ref = request.arguments[1]
        transf_out_ref = request.arguments[2]
        
        if(not transf_in_ref.HasField('var') and not dataset_ref.HasField('var') and transf_out_ref.HasField('var')):
            transf: Pipeline = SharedCollections().getPipeline(Utils.parseArgumentMsg(transf_in_ref))
            dataset: Dataset = SharedCollections().getDataset(Utils.parseArgumentMsg(dataset_ref))
            
            id = SharedCollections().addPipeline(transf.adapt(dataset))
            yield request.replySuccess(substitutions={
                transf_out_ref.var: basicMsg.ArgumentMsg(constant=id)
                }, hasNext=False)
        else:
            yield request.replyFail()
            
            
fitPrimitive = DistributedElements.DistributedPrimitiveWrapper("fit", 3, __Fit())