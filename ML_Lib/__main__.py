from .schema.schema import schemaPrimitive
from .schema.theoryToSchema import theoryToSchemaPrimitive
from .dataset.theoryToDataset import theoryToDatasetPrimitive
from .dataset.randomSplit import randomSplitPrimitive
from .dataset.column import columnPrimitive
from .dataset.row import rowPrimitive
from .dataset.cell import cellPrimitive
from .dataset.fold import foldPrimitive
from .dataset.theory_from_Dataset import theoryFromDatasetPrimitive
from .trasformations.schema_trasformation import schemaTrasformation
from .trasformations.normalization import normalizePrimitive
from .trasformations.one_hot_encode import one_hot_encodePrimitive
from .trasformations.drop import dropPrimitive
from .trasformations.fit import fitPrimitive
from .trasformations.transform import transformPrimitive
from .neuralNetwork.inputLayer import inputLayerPrimitive
from .neuralNetwork.denseLayer import denseLayerPrimitive
from .neuralNetwork.outputLayer import outputLayerPrimitive
from .neuralNetwork.neuralNetwork import neuralNetworkPrimitive
from .predictors.train import trainPrimitive
from .predictors.predict import predictPrimitive
from .predictors.classify import classifyPrimitive
from .predictors.score import msePrimitive
from python_Primitives_Server import PrimitiveWrapper, DistributedElements
import threading

def launchPrimitive(primitive: DistributedElements.DistributedPrimitiveWrapper, port: int):
    PrimitiveWrapper.serve(primitive, port, "customLibrary")
    
primitives = [schemaPrimitive, theoryToSchemaPrimitive,
              theoryToDatasetPrimitive, randomSplitPrimitive,
              rowPrimitive, columnPrimitive, cellPrimitive, foldPrimitive, 
              theoryFromDatasetPrimitive, schemaTrasformation,
              normalizePrimitive, one_hot_encodePrimitive, dropPrimitive,
              fitPrimitive, transformPrimitive, inputLayerPrimitive,
              denseLayerPrimitive, outputLayerPrimitive, neuralNetworkPrimitive,
              trainPrimitive, predictPrimitive, classifyPrimitive, msePrimitive]

threads: list[threading.Thread] = []
port = 8080
for primitive in primitives:
    t = threading.Thread(target=launchPrimitive, args=(primitive, port))
    t.start()
    threads.append(t)
    port += 1

for t in threads:
   t.join()

print("Done!")
