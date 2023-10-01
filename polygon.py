import matplotlib.pyplot as plt
import utils

class polygon:
    def __init__(self, vertexes: list) -> None:
        self.vertexes = vertexes

    def draw(self, ax: plt.axes, color: str) -> None:
        coord = self.vertexes.copy()
        if (len(coord) == 0):
            return
        coord.append(coord[0]) 
        xs, ys = zip(*coord)
        ax.plot(xs, ys, color)
        ax.plot(xs, ys, color + 'o')
    
    def isInsite(self, p) -> bool:
        for i, vertex in enumerate(self.vertexes):
            if (utils.doubleSabc(vertex, self.vertexes[i - 1], p) > 0):
                return False
        return True

    def intersecting(self, poly: type['polygon']) -> type['polygon']:
        i = 0
        j = 0
        iteration = 0
        p2 = self.vertexes[i]
        p1 = self.vertexes[i - 1]
        q2 = poly.vertexes[j]
        q1 = poly.vertexes[j - 1]
        result = polygon([])
        inside = ""
        while iteration < 2 * (len(self.vertexes) + len(poly.vertexes)):
            if (utils.isSegmentIntersecting(p1, p2, q1, q2) and (q2[0]-q1[0]) * (p2[1]-p1[1]) - (p2[0]-p1[0]) * (q2[1]-q1[1]) != 0):
                newVertex = utils.findSegmentIntersecting(p1, p2, q1, q2)
                if (len(result.vertexes) != 0 and newVertex == result.vertexes[0] and result.vertexes[-1] != result.vertexes[0]):
                    return result
                if (len(result.vertexes) == 0 or newVertex != result.vertexes[-1]):
                    result.vertexes.append(newVertex)
                if (utils.doubleSabc(q1, q2, p2) >= 0):
                    inside = "p"
                else:
                    inside = "q"
            if ((q2[0]-q1[0]) * (p2[1]-p1[1]) - (p2[0]-p1[0]) * (q2[1]-q1[1]) >= 0):
                if (utils.doubleSabc(q1, q2, p2) >= 0):
                    #advance q
                    j += 1
                    if (j == len(poly.vertexes)):
                        j = 0
                    if inside == "q":
                        if (len(result.vertexes) == 0 or result.vertexes[-1] != q2):
                            result.vertexes.append(q2)
                else:
                    #advance p
                    i += 1
                    if (i == len(self.vertexes)):
                        i = 0                  
                    if inside == "p":
                        if (len(result.vertexes) == 0 or result.vertexes[-1] != p2):
                            result.vertexes.append(p2)
            else:
                if (utils.doubleSabc(p1, p2, q2) >= 0):
                    #advance p
                    i += 1
                    if (i == len(self.vertexes)):
                        i = 0
                    if inside == "p":
                        if (len(result.vertexes) == 0 or result.vertexes[-1] != p2):
                            result.vertexes.append(p2)                
                else:
                    #advance q
                    j += 1
                    if (j == len(poly.vertexes)):
                        j = 0
                    if inside == "q":
                        if (len(result.vertexes) == 0 or result.vertexes[-1] != q2):
                            result.vertexes.append(q2)
            p2 = self.vertexes[i]
            p1 = self.vertexes[i - 1]
            q2 = poly.vertexes[j]
            q1 = poly.vertexes[j - 1]
            iteration += 1
        if (self.isInsite(q2)):
            return poly
        if (poly.isInsite(p2)):
            return self
        return polygon([])
        
