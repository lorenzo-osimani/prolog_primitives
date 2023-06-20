from python_Primitives_Server import DistributedElements
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from python_Primitives_Server import Utils
from ..Collections import SharedCollections
from datasets import Dataset

class __RandomSplitPrimitive(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        dataset_ref = request.arguments[0]
        ratio = request.arguments[1]
        train_ref = request.arguments[2]
        val_ref = request.arguments[3]
        if(not dataset_ref.HasField("var") and not ratio.HasField("var") and 
           train_ref.HasField("var") and val_ref.HasField("var")):
            
            
            dataset: Dataset = SharedCollections().getDataset(str(Utils.parseArgumentMsg(dataset_ref)))
            ratio = float(Utils.parseArgumentMsg(ratio))
            train_size = int(ratio * len(list(dataset)))
        
            shuffled = dataset.shuffle()
            train_ds = shuffled[:train_size]
            val_ds = dataset[train_size:]
            
            train_id = SharedCollections().addDataset(train_ds)
            val_id = SharedCollections().addDataset(val_ds)
            
            yield request.replySuccess(substitutions={
                train_ref.var: basicMsg.ArgumentMsg(constant=train_id),
                val_ref.var: basicMsg.ArgumentMsg(constant=val_id)
                }, hasNext=False)
        else:
            yield request.replyFail()
            
randomSplitPrimitive = DistributedElements.DistributedPrimitiveWrapper("random_split", 4, __RandomSplitPrimitive())