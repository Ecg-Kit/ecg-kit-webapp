import matlab.engine
matlabEngine  = matlab.engine.start_matlab()
t = matlabEngine.customAdd(4,5)
print(t)

