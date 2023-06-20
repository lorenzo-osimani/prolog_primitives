from generatedProto import basicMessages_pb2 as basicMsg
from python_Primitives_Server import Utils
import pandas as pd
import tensorflow as tf
import datasets

class Dataset:
    targets: list
    data: datasets.Dataset
    
    def __init__(self,
                 data,
                 targets):
        self.data = data
        self.targets = targets 
   