import math


def script(QGO, QG1, CD1ang, CD1n, CD2n, gap, Dlength):
    # QG0 QG1 CD1ang
    CD1len = CD1ang / 180.0 * math.pi
    CD2len = (45.0 - CD1ang * 2.0) / 180.0 * math.pi
    return ''''HUST SC Gantry DownStream'
0
15. 11.0 /MEV/ .001 ;
15. 6. /%/ 1.0   ;
15. 1. /mm/ 0.1   ;

1. 3.5 7.5 3.5 7.5 0.0 0.0 729.134 /BEAM/ ;

13 3;
13 6;

3. 0.01 /CP/;
3. 1.0 ;
5. 0.27 {vQGO} 30. /QG0/ ;
3. 0.30 ;
5. 0.27 {vQG1} 30. /QG1/ ;
3. {vDlength} ;

16. 5. 30;
16. 7. 0.0;
20. -180.0 ;
2. 0 /A1/ ;
4. {vCD1len} -24.32128299585206 {vCD1n} /CD1/ ;
2. 0 /B1/ ;
20. 180.0 ;
3. {vgap};
20. -180.0 ;
2. 0 /A1/ ;
4. {vCD2len} -24.32128299585206 {vCD2n} /CD1/ ;
2. 0 /B1/ ;
20. 180.0 ;
3. {vgap};
20. -180.0 ;
2. 0 /A1/ ;
4. {vCD1len} -24.32128299585206 {vCD1n} /CD3/ ;
2. 0 /B1/ ;
20. 180.0 ;

3. 0.8 ;

13 4;

SENTINEL

SENTINEL
SENTINEL'''.format(vQGO=QGO, vQG1=QG1, vCD1len=CD1len, vCD2len=CD2len, vgap=gap, vCD1n=CD1n, vCD2n=CD2n , vDlength = Dlength)

# print(script(2.,3.,15.0,0.3))
