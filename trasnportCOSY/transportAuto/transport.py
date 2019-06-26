import scriptT
import fileSkipLine
import os
import math


def trans(**kwargs):
    # return [sList,xList,yList,r16List]

    # beamlime parameter
    QGO = kwargs['QGO']
    QG1 = kwargs['QG1']
    CD1ang = kwargs['CD1ang']
    CD1n = kwargs['CD1n']
    CD2n = kwargs['CD2n']
    gap = kwargs['gap']
    Dlength = kwargs['Dlength']

    # arrays hold envelope parameter
    sList = []  # distance
    xList = []  # envelope along X
    yList = []  # envelope along Y
    r16List = []  # transport matrix R16
    typeList = []  # component type such as QUAD BEND DRIFT

    # write FOR001 file
    # def script(QGO,QG1,CD1ang,CD1n,CD2n,gap):
    FOR001 = open('./FOR001.DAT', 'w')
    FOR001.write(scriptT.script(QGO, QG1, CD1ang, CD1n, CD2n, gap,Dlength))
    FOR001.flush()
    FOR001.close()

    # run transport
    os.system('transwin85.exe')

    # read FOR002 and extract envelope parameter to the arrays declared above
    FOR002 = open('./FOR002.DAT', 'r')
    line = FOR002.readline()
    while line != '':
        if line.startswith(' *QUAD*') or line.startswith(' *BEND*') or line.startswith(' *DRIFT*'):
            # type
            if line.startswith(' *QUAD*'):
                typeList.append('QUAD')
            elif line.startswith(' *BEND*'):
                typeList.append('BEND')
            elif line.startswith(' *DRIFT*'):
                typeList.append('DRIFT')

            # print(line)
            next01line = FOR002.readline()
            sList.append(float(list(filter(None, next01line.split(' ')))[0]))
            xList.append(float(list(filter(None, next01line.split(' ')))[3]))
            fileSkipLine.skip(FOR002, 1)
            next03line = FOR002.readline()
            yList.append(-1.0 * float(list(filter(None, next03line.split(' ')))[1]))
            fileSkipLine.skip(FOR002, 4)
            next08line = FOR002.readline()
            r16List.append(10.0 * math.fabs(float(list(filter(None, next08line.split(' ')))[5])))

        line = FOR002.readline()
    FOR002.close()

    # print([sList, xList, yList, r16List])

    return [sList, xList, yList, r16List, typeList]

# test
# print(trans(QGO=-4.3737,QG1=5.398396,CD1ang=15.0,CD1n=5.9,CD2n=-22.9,gap=0.3))
