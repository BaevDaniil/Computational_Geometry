import utils
import matplotlib.pyplot as plt
import time

def miniDisk(points: list):
    if (len(points) <= 2):
        return points
    disk = [points[0], points[1]]
    for i in range(2, len(points)):
        if utils.isInsideDisk(disk, points[i]) <= 0:
            continue
        else:
            disk = MiniDiskWithPoint(points[:i], points[i])
    return disk

def MiniDiskWithPoint(points: list, q: list):
    disk = [points[0], q]

    for j in range(1, len(points)):
        if utils.isInsideDisk(disk, points[j]) <= 0:
            continue
        else:
            disk = MiniDiskWith2Points(points[:j], points[j], q)
    return disk

def MiniDiskWith2Points(points: list, q1: list, q2: list):
    disk = [q1, q2]

    for k in range(0, len(points)):
        if utils.isInsideDisk(disk, points[k]) <= 0:
            continue
        else:
            disk = [q1, q2, points[k]]
    return disk