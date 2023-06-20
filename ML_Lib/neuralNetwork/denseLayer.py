from python_Primitives_Server import DistributedElements
from generatedProto import primitiveService_pb2 as primitiveMsg
from generatedProto import basicMessages_pb2 as basicMsg
from generatedProto import errorsMessages_pb2 as errorMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
import tensorflow as tf

class __DenseLayer(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        topology_in_ref = request.arguments[0]
        size = request.arguments[1]
        activation = request.arguments[2]
        topology_out_ref = request.arguments[3]
        
        if(not topology_in_ref.HasField('var') and not size.HasField('var') and
           not activation.HasField('var') and topology_out_ref.HasField('var')):
            topology: list = SharedCollections().getTopology(Utils.parseArgumentMsg(topology_in_ref))

            dense = tf.keras.layers.Dense(
                units=int(Utils.parseArgumentMsg(size)),
                activation=Utils.parseArgumentMsg(activation),
                name="dense_"+str(len(topology)))
            topology.append(dense)
            
            id = SharedCollections().addTopology(topology)
            yield request.replySuccess(substitutions={
                topology_out_ref.var: basicMsg.ArgumentMsg(constant=id)
                }, hasNext=False)
        else:
            yield request.replyFail()
            
            
denseLayerPrimitive = DistributedElements.DistributedPrimitiveWrapper("dense_layer", 4, __DenseLayer())