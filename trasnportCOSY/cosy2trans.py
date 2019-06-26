
print('--------COSY2TRANS-----------')


def CD(ang,r,G):
    pi = 3.1415926535#pi
    BR = 2.43212829958520#magnetic rigidity
    halfGap = 0.03

    length = ang/180.0*pi
    n = G*r/(BR/r)#G*R1/(2.432128299585206/R1)
    print('4. '+str(length)+' '+str(ang)+' '+str(n))


CD(8.2,1.0,0.0)
CD(45.0-8.2*2.0,1.0,0.0)
CD(25.11560031339517,1.0,0.0)
CD(8.453416623568060,1.0,0.0)
CD(10.0,1.0,-40.0)

