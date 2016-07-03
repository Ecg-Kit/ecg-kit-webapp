# import matlab.engine
#
# matlabEngine  = matlab.engine.start_matlab()
#
# # t = matlabEngine.customAdd(4,5)
#
# matlabEngine.ECGwrapper('recording_name',
#                                   '/Users/admin/Documents/MATLAB/ecg-kit/recordings/example_recording',
#                                   'ECGtaskHandle',
#                                   'QRS_detection')
#
# # print((ECGwrapper)wrapper)
#
# matlabEngine.Run()
#
# print(t)

import matlab.engine

eng = matlab.engine.start_matlab()

pythonHandler = eng.PythonHandler()

runResult = eng.run(pythonHandler)

cacheResults = eng.ecgKitWrapper.cKnownFormats

print(cacheResults)


# tr = eng.Triangle(5.0,3.0)
# a = eng.area(tr)

