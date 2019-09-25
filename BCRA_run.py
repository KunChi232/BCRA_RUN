import sys
import rpy2
from rpy2.robjects.packages import importr, data
from rpy2.robjects import DataFrame
LIBRARY_PATH = 'C:/iir/R/win-library/3.6'
PACKAGE_NAME = 'BCRA'
use_exmaple = True

def initBCRAObject():
    bcra = importr(PACKAGE_NAME, lib_loc = LIBRARY_PATH)
    return bcra

def getExmpleData(bcra):
    example = data(bcra).fetch('exampledata')
    example = example['exampledata']
    return example

def getArgument():
    ID = sys.argv[1]
    T1 = sys.argv[2] #填表人，目前年齡
    T2 = sys.argv[3] #切片時的年齡
    N_Biop = sys.argv[4] #乳房切片次數，unk=99
    HypPlas = sys.argv[5] #若為atypical為1,no=0,unk=99
    AgeMen = sys.argv[6] #初經年齡, unk=99
    Age1st = sys.argv[7] #第一次懷孕年齡, 未產=98 , unk=99
    N_Rels = sys.argv[8] #一等親得乳癌數量。父母兄弟姊妹
    Race = sys.argv[9] # 1=白人, 11=華人
    
    return ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race

def createDataFrame():
    ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race = getArgument()
    d = {"ID" : int(ID), "T1" : float(T1), "T2" : float(T2),
        "N_Biop" : int(N_Biop), "HypPlas" : int(HypPlas), "AgeMen" : int(AgeMen),
        "Age1st" : int(Age1st), "N_Rels" : int(N_Rels), "Race" : int(Race)}
    dataFrame = DataFrame(d)
    return dataFrame

def main():
    bcra = initBCRAObject()
    userData = DataFrame({})
    if(use_exmaple):
        userData = getExmpleData(bcra)
    else:
        userData = createDataFrame()
    print([bcra.absolute_risk(userData, Raw_Ind = 1), bcra.relative_risk(userData, Raw_Ind = 1)])

if __name__ == '__main__':
    main()