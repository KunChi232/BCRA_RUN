import sys
import rpy2
from rpy2.robjects.packages import importr, data
from rpy2.robjects import DataFrame
PACKAGE_NAME = 'BCRA'
use_exmaple = False

def initBCRAObject():
    bcra = importr(PACKAGE_NAME)
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

def createDataFrame(ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race):
    d = {"ID" : int(ID), "T1" : float(T1), "T2" : float(T2),
        "N_Biop" : int(N_Biop), "HypPlas" : int(HypPlas), "AgeMen" : int(AgeMen),
        "Age1st" : int(Age1st), "N_Rels" : int(N_Rels), "Race" : int(Race)}
    dataFrame = DataFrame(d)
    return dataFrame

def calculate(dataFrame):
    bcra = initBCRAObject()
    a_risk = bcra.absolute_risk(dataFrame, Raw_Ind = 1)
    r_risk = bcra.relative_risk(dataFrame, Raw_Ind = 1)
    return a_risk, r_risk

def main():
    bcra = initBCRAObject()
    userData = DataFrame({})
    if(use_exmaple):
        userData = getExmpleData(bcra)
        a_risk = bcra.absolute_risk(userData.rx(5, True), Raw_Ind = 1)
        r_risk = bcra.relative_risk(userData.rx(5, True), Raw_Ind = 1)
        print(a_risk[0], r_risk[0][0], r_risk[1][0], r_risk[2][0])

    else:
        ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race = getArgument()
        userData = createDataFrame(ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race)
        a_risk = bcra.absolute_risk(userData, Raw_Ind = 1)
        r_risk = bcra.relative_risk(userData, Raw_Ind = 1)
        print(a_risk[0], r_risk[0][0], r_risk[1][0], r_risk[2][0])


if __name__ == '__main__':
    main()