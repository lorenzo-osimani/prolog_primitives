from python_Primitives_Server import DistributedElements
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
from sklearn.model_selection import KFold
import numpy as np

class __FoldPrimitive(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        dataset_ref = request.arguments[0]
        k = request.arguments[1]
        train_ref = request.arguments[2]
        val_ref = request.arguments[3]
        if(not dataset_ref.HasField("var") and not k.HasField("var") and 
           train_ref.HasField("var") and val_ref.HasField("var")):
            
            dataset = SharedCollections().getDataset(str(Utils.parseArgumentMsg(dataset_ref)))
            k = int(Utils.parseArgumentMsg(k))
            for kfold, (train, test) in enumerate(KFold(n_splits=k, 
                                shuffle=True).split(dataset)):
                train_ds = dataset[train]   
                val_ds = dataset[test]
                
                train_id = SharedCollections().addDataset(train_ds)
                val_id = SharedCollections().addDataset(val_ds)
            
                yield request.replySuccess(substitutions={
                    train_ref.var: basicMsg.ArgumentMsg(constant=train_id),
                    val_ref.var: basicMsg.ArgumentMsg(constant=val_id)
                    }, hasNext= kfold + 1 < k)
        else:
            yield request.replyFail()
            
foldPrimitive = DistributedElements.DistributedPrimitiveWrapper("fold", 4, __FoldPrimitive())