import matplotlib.pyplot as plt

def sign(x: int):
    if x > 0:
        return 1
    elif x == 0:
        return  0
    else:
        return -1

def det3x3(matrix3x3):
    return (matrix3x3[0][0] * matrix3x3[1][1] * matrix3x3[2][2] + 
            matrix3x3[0][1] * matrix3x3[1][2] * matrix3x3[2][0] + 
            matrix3x3[1][0] * matrix3x3[2][1] * matrix3x3[0][2] -
            matrix3x3[0][2] * matrix3x3[1][1] * matrix3x3[2][0] -
            matrix3x3[0][1] * matrix3x3[1][0] * matrix3x3[2][2] -
            matrix3x3[1][2] * matrix3x3[2][1] * matrix3x3[0][0])

def isInsideDisk(disk: list, point):
    if len(disk) == 0:
        return -1
    if len(disk) == 1:
        if disk[0] == point:
            return 0
        else:
            return 1
    if len(disk) == 2:
        d_x_d = (disk[0][0] - disk[1][0]) * (disk[0][0] - disk[1][0]) + (disk[0][1] - disk[1][1]) * (disk[0][1] - disk[1][1])
        o_x_2 = [disk[0][0] + disk[1][0], disk[0][1] + disk[1][1]]
        o_point_x_o_point = (2 * point[0] - o_x_2[0]) * (2 * point[0] - o_x_2[0]) + (2 * point[1] - o_x_2[1]) * (2 * point[1] - o_x_2[1])
        return (o_point_x_o_point - d_x_d)
    if len(disk) == 3:
        minor00 = det3x3([[disk[0][0], disk[0][1], 1],
                                        [disk[1][0], disk[1][1], 1],
                                        [disk[2][0], disk[2][1], 1]])
        
        minor01 = det3x3([[disk[0][0] * disk[0][0] + disk[0][1] * disk[0][1], disk[0][1], 1],
                                        [disk[1][0] * disk[1][0] + disk[1][1] * disk[1][1], disk[1][1], 1],
                                        [disk[2][0] * disk[2][0] + disk[2][1] * disk[2][1], disk[2][1], 1]])
        
        minor02 = det3x3([[disk[0][0] * disk[0][0] + disk[0][1] * disk[0][1], disk[0][0], 1],
                                        [disk[1][0] * disk[1][0] + disk[1][1] * disk[1][1], disk[1][0], 1],
                                        [disk[2][0] * disk[2][0] + disk[2][1] * disk[2][1], disk[2][0], 1]])
        
        minor03 = det3x3([[disk[0][0] * disk[0][0] + disk[0][1] * disk[0][1], disk[0][0], disk[0][1]],
                                        [disk[1][0] * disk[1][0] + disk[1][1] * disk[1][1], disk[1][0], disk[1][1]],
                                        [disk[2][0] * disk[2][0] + disk[2][1] * disk[2][1], disk[2][0], disk[2][1]]])
        return ((point[0] * point[0] + point[1] * point[1]) * minor00 - 
                point[0] * minor01 + 
                point[1] * minor02 - 
                minor03) * sign(minor00)
    

def drawDisk(disk: list, ax: plt.Axes, color = 'black'):
    if len(disk) == 0:
        return
    elif len(disk) == 2:
        x, y = complex(disk[0][0], disk[0][1]), complex(disk[1][0], disk[1][1])
        c = (x + y) / 2
        center = [c.real, c.imag]
        radious = abs(c-x)
        circle = plt.Circle(center, radious, fill=False, clip_on=False)
        ax.add_artist(circle)
        ax.plot(center[0], center[1], color=color, marker='o')
    elif len(disk) == 3:
        x, y, z = complex(disk[0][0], disk[0][1]), complex(disk[1][0], disk[1][1]), complex(disk[2][0], disk[2][1])
        w = z-x
        w /= y-x
        c = (x-y)*(w-abs(w)**2)/2j/w.imag-x
        center = [-c.real, -c.imag]
        radious = abs(c+x)
        circle = plt.Circle(center, radious, fill=False, clip_on=False, color=color)
        ax.add_artist(circle)
        ax.plot(center[0], center[1], color=color, marker='o')
    elif len(disk) > 3:
        return
    for point in disk:
        ax.plot(point[0], point[1], color=color, marker='x')


def isEqualDisc(disk1: list, disk2: list):
    if (len(disk1) == 0 and len(disk2) == 0):
        return True
    if (len(disk1) == 0 or len(disk2) == 0):
        return False
    for point in disk2:
        if isInsideDisk(disk1, point) != 0:
            return False
    return True
