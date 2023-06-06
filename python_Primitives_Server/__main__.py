from ML_Lib.schema import schemaPrimitive
from ML_Lib.theoryToSchema import theoryToSchemaPrimitive
from ML_Lib.filterKbPrimitive import filterKBPrimitive
from . import PrimitiveWrapper, DistributedElements
import threading

def launchPrimitive(primitive: DistributedElements.DistributedPrimitiveWrapper, port: int):
    PrimitiveWrapper.serve(primitive, port, "customLibrary")


t1 = threading.Thread(target=launchPrimitive, args=(schemaPrimitive, 8081))
t2 = threading.Thread(target=launchPrimitive, args=(theoryToSchemaPrimitive, 8082))
t3 = threading.Thread(target=launchPrimitive, args=(filterKBPrimitive, 8083))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("Done!")
