from .schema.schemaClass import Schema
import tensorflow as tf
from datasets import Dataset

class SharedCollections(object):

    __schemas: dict = dict()
    __dataset: dict = dict()
    __pipeline: dict = dict()
    __topology: dict = dict()
    __model: dict = dict()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SharedCollections, cls).__new__(cls)
        return cls.instance
    
    def addSchema(self, schema: Schema) -> str:
        id = self.idGenerator()
        self.__schemas[id] = schema
        return id
    
    def getSchema(self, ref: str) -> Schema:
        return self.__schemas.get(ref, None)
    
    def addDataset(self, dataset: Dataset) -> str:
        id = self.idGenerator()
        self.__dataset[id] = dataset
        return id
    
    def getDataset(self, ref: str) -> Dataset:
        return self.__dataset.get(ref, None)
    
    def addPipeline(self, pipeline) -> str:
        id = self.idGenerator()
        self.__pipeline[id] = pipeline
        return id
    
    def getPipeline(self, ref: str):
        return self.__pipeline.get(ref, None)
    
    def addTopology(self, topology) -> str:
        id = self.idGenerator()
        self.__topology[id] = topology
        return id
    
    def getTopology(self, ref: str):
        return self.__topology.get(ref, None).copy()
    
    def addModel(self, model) -> str:
        id = self.idGenerator()
        self.__model[id] = model
        return id
    
    def getModel(self, ref: str):
        return self.__model.get(ref, None)

    def idGenerator(self) -> str:
        import random
        import string
        characters = string.ascii_lowercase# + string.digits
        id = ''.join(random.choice(characters) for i in range(10)) 
        while(id in self.__schemas or id in self.__dataset):
            id = ''.join(random.choice(characters) for i in range(10)) 
        return id  
   