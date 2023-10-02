def findSegmentIntersecting(p1, p2, q1, q2):
        '''
          x - p1[0]       y - p1[1] 
        ------------- = -------------
        p2[0] - p1[0]   p2[1] - p1[1]

          x - q1[0]       y - q1[1] 
        ------------- = -------------
        q2[0] - q1[0]   q2[1] - q1[1]
        '''
        det = (p2[1] - p1[1]) * (-q2[0] + q1[0]) - (q2[1] - q1[1]) * (-p2[0] + p1[0])
        cp = p1[0] * (p2[1] - p1[1]) - p1[1] * (p2[0] - p1[0])
        cq = q1[0] * (q2[1] - q1[1]) - q1[1] * (q2[0] - q1[0])
        detX = cp * (-q2[0] + q1[0]) - cq * (-p2[0] + p1[0])
        detY = (p2[1] - p1[1]) * cq - (q2[1] - q1[1]) * cp
        return [detX / det, detY / det] 

def doubleSabc(a, b, c):
        return (a[0] * b[1] + b[0] * c[1] + a[1] * c[0]) - (b[1] * c[0] + a[1] * b[0] + a[0] * c[1])

def isSegmentIntersecting(p1, p2, q1, q2) -> bool:
    return (doubleSabc(p1, p2, q1) * doubleSabc(p1, p2, q2) <= 0) and (doubleSabc(q1, q2, p1) * doubleSabc(q1, q2, p2) <= 0)