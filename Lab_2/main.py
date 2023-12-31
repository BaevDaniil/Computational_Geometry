import utils
import matplotlib.pyplot as plt
import config
import os
import ast

import random
import minimalDisc

def main():
    conf = config.config()
    conf.readConfig("config.txt")
    if not os.path.isdir(conf.resultFolder):
        os.mkdir(conf.resultFolder)
    
    resFile = open(conf.resultFolder + '/result.txt', 'w')

    unswer = []

    for test in conf.tests:
        points = []
        disc = []
        with open(conf.testFolder + '/' + test[1], 'r') as testFile:
            line = testFile.readline()
            points = ast.literal_eval(line)
            line = testFile.readline()
            disc = ast.literal_eval(line)
            unswer.append(minimalDisc.CheckDisc(points, disc))

            if conf.draw:
                trueDisc = minimalDisc.miniDisk(points)
                fig, ax = plt.subplots()
                for [x, y] in points:
                    param = utils.isInsideDisk(disc, [x, y])
                    if (param == 0):
                        ax.plot(x, y, 'b+')
                        plt.text(x, y, '({0}, {1})'.format(x, y))
                    elif (param < 0):
                        ax.plot(x, y, 'g+')
                        plt.text(x, y, '({0}, {1})'.format(x, y))
                    else:
                        ax.plot(x, y, 'r+')
                        plt.text(x, y, '({0}, {1})'.format(x, y))
                    utils.drawDisk(disc, ax)
                    utils.drawDisk(trueDisc, ax)
                fig.savefig(conf.resultFolder + '/' + test[0])
    resFile.write(str(unswer))
    resFile.close()
    fig, ax = plt.subplots()

if __name__== "__main__":
    main()