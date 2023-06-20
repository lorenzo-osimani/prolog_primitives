from python_Primitives_Server import DistributedElements
from generatedProto import primitiveService_pb2 as primitiveMsg
from generatedProto import basicMessages_pb2 as basicMsg
from generatedProto import errorsMessages_pb2 as errorMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
import tensorflow as tf
from datasets import Dataset

class __Train(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        predictor_in_ref = request.arguments[0]
        dataset_ref = request.arguments[1]
        params = request.arguments[2]
        predictor_out_ref = request.arguments[3]
        
        if(not predictor_in_ref.HasField('var') and dataset_ref.HasField('var') and
           not params.HasField('var') and predictor_out_ref.HasField('var')):
            model: tf.keras.Model = SharedCollections().getModel(Utils.parseArgumentMsg(predictor_in_ref))
            params = Utils.parseArgumentMsg(params)
            
            print(params)
            
            model.compile()

            '''
            train_dataset = tf.data.Dataset.from_tensor_slices(
                (
                    {"feature1": dataset['feature1'], "feature2": dataset['feature2']},
                    {"target": dataset['target']},
                )
            )
            train_dataset = train_dataset.batch(5)
            model.fit(train_dataset, epochs=5)
            '''
            id = SharedCollections().addModel(model)
            yield request.replySuccess(substitutions={
                predictor_out_ref.var: basicMsg.ArgumentMsg(constant=id)
                }, hasNext=False)
        else:
            yield request.replyFail()
             
trainPrimitive = DistributedElements.DistributedPrimitiveWrapper("train", 2, __Train())