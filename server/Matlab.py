import matlab.engine

class Matlab:

    engine = null
    
    def __init__(self):
        self.engine = matlab.engine.start_matlab()

    def customAdd(a,b):
        engine.customAdd(a,b)

