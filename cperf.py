'''
Created on 2015-11-25

@author: chinple
'''
from tmodel.runner.perfdriver import StressScheduler

_sc = StressScheduler()
def stressScenario(startThreads=3, maxThreads=10, step=1, expTps=50):
    def __stressMiddleFun(stsHandler):      
        _sc.addScenario(stsHandler, startThreads, maxThreads, step, expTps)
    return __stressMiddleFun

def apiStatisticHandler(obj, objFun, tupleArg, jsonArg, adpInfo):
    rh = _sc.getApiRunner(objFun)
    return rh.runHandler(*tupleArg, **jsonArg)[1]

def running(*args):
    from libs.objop import StrOperation
    import sys
    
    if len(args) == 0:
        args = ("-t", sys.argv[0])
    elif len(args) == 1:
        args = ["-t", sys.argv[0]] + StrOperation.splitStr(args[0], " ", '"')
    _sc.setRunnerByArgs(True, args)
    _sc.launch()
