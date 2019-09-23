import sys

LIBRARY_PATH = 'C:\Users\iir\iir\R\win-library'
PACKAGE_NAME = 'BCRA'

def main():
    ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race = getArgument()

def getArgument():
    ID = sys.argv[1]
    T1 = sys.argv[2] #age, key_name = age
    T2 = sys.argv[3] #乳房攝影時年齡, 
    N_Biop = sys.argv[4] #乳房切片次數 key_name = times
    HypPlas = sys.argv[5] #key_name = type, 若為atypical為1,no=0,unk=99
    AgeMen = sys.argv[6] #初經年齡, key_name = mena_age
    Age1st = sys.argv[7] #第一次懷孕年齡, key_name = firstp_age
    N_Rels = sys.argv[8] #一等親得乳癌數量。父母兄弟姊妹
    Race = sys.argv[9] # 1=白人, 11=華人。key_name = racial
    
    return ID, T1, T2, N_Biop, HypPlas, AgeMen, Age1st, N_Rels, Race

if __name__ == '__main__':
    main()