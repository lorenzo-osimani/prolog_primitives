import sys
sys.path.append('../generatedProto')

import unittest
from concurrent.futures import ThreadPoolExecutor
from prolog_primitives.basic import nt, PrimitiveWrapper

class TestMyClass(unittest.TestCase):

    def test_my_method(self):
        executor = ThreadPoolExecutor()
        server = PrimitiveWrapper.serve(nt.ntPrimitive, 8080, "custom")
        import time
        time.sleep(2)
        server.stop(0)
        self.assert_(True)
        
