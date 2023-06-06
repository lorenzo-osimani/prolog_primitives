from enum import Enum
from generatedProto import basicMessages_pb2 as basicMsg
from python_Primitives_Server import Utils

class Attribute:  
    name: str
    type = None
    
    def __init__(self,
                 name: str,
                 type):
        self.name = name
        self.type = type
        
    def typeToArgumentMsg(self) -> basicMsg.ArgumentMsg:
        if(self.type == int):
            return basicMsg.ArgumentMsg(
                constant="integer"
            )
        elif(self.type == float):
            return basicMsg.ArgumentMsg(
                constant="real"
            )
        elif(self.type == str):
            return basicMsg.ArgumentMsg(
                constant="string"
            )
        elif(self.type == bool):
            return basicMsg.ArgumentMsg(
                constant="boolean"
            )
        elif(self.type["type"] == "categorical" or self.type["type"] == "ordinal"):
            argument = Utils.fromListToArgumentMsg(self.type["values"])
            return basicMsg.ArgumentMsg(
                struct = basicMsg.StructMsg(
                    functor=self.type["type"],
                    arguments = [argument]
                )
            )
    
    def parseTypeFromArgumentMsg(type_name: basicMsg.ArgumentMsg):
        type_struct = Utils.parseArgumentMsg(type_name)
        return Attribute.parseType(type_struct)
        
    def parseType(type_struct):
        if(type_struct == "integer"):
            return int
        elif(type_struct == "real"):
            return float
        elif(type_struct == "string"):
            return str
        elif(type_struct == "boolean"):
            return bool
        elif(type(type_struct) is Utils.Struct and (type_struct.functor == "categorical" or type_struct.functor == "ordinal")):
            values = dict()
            values["type"] = type_struct.functor
            values["values"] = type_struct.arguments[0]
            return values
    

class Schema:
    name: str
    attributes: list[Attribute]
    targets: list[str]
    
    def __init__(self,
                 name: str,
                 attributes: list,
                 targets: list):
        self.name = name
        self.attributes = attributes
        self.targets = targets   

class SharedCollections(object):

    schemas: dict = dict()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SharedCollections, cls).__new__(cls)
        return cls.instance
    
    
    def addSchema(self, schema: Schema) -> str:
        id = self.idGenerator()
        self.schemas[id] = schema
        return id
    
    def getSchema(self, ref: str) -> Schema:
        return self.schemas.get(ref, None)


    def idGenerator(self) -> str:
        import random
        import string
        characters = string.ascii_lowercase# + string.digits
        id = ''.join(random.choice(characters) for i in range(10)) 
        while(id in self.schemas):
            id = ''.join(random.choice(characters) for i in range(10)) 
        return id  
   