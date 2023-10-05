import utils
import config
import os

import random
import minimalDisc

def generateTest(numOfTest: int, maxNumOfPoint: int, space:list, dirForTest, config):
    unswerFile = open("unswer.txt", 'w')
    unswer = []

    configFile = open(config, 'a')

    for i in range(numOfTest):
        numOfPoint = random.randint(0, maxNumOfPoint)
        points = [[random.randint(space[0][0], space[0][1]), random.randint(space[1][0], space[1][1])] for i in range(numOfPoint)]
        isPositiveTest = True
        if random.randint(-1000, 1000) > 500:
            isPositiveTest = True
        else:
            isPositiveTest = False
        unswer.append(isPositiveTest)
        disc = []
        trueDisk = minimalDisc.miniDisk(points)

        if isPositiveTest:
            configFile.write('#positive test\n')
            disc = trueDisk
        else:
            param = random.randint(-1000, 1000)
            if param < 0:
                configFile.write('#new random point\n')
                while True:
                    disc = [[random.randint(space[0][0], space[0][1]), random.randint(space[1][0], space[1][1])] for i in range(random.randint(0, 3))]
                    if not utils.isEqualDisc(disc, trueDisk): break
            else:
                configFile.write('#random points from set\n')
                while True:
                    disc = [points[random.randint(0, len(points))] for i in range(random.randint(0, 3))]
                    if not utils.isEqualDisc(disc, trueDisk): break
        file = open(dirForTest + '/test_' + str(i) + '.txt', 'w')
        file.write(str(points) + '\n')        
        file.write(str(disc) + '\n')
        file.close()

        configFile.write('test_' + str(i) + ': ' + 'test_' + str(i) + '.txt\n')
    unswerFile.write(str(unswer))
    unswerFile.close()
    configFile.close()



if __name__== "__main__":
    numOfTest = 20
    spase = [[-100, 100], [-100, 100]]
    maxNumOfPoint = 50

    conf = config.config()
    conf.readConfig("config.txt")
    if not os.path.isdir(conf.resultFolder):
        os.mkdir(conf.resultFolder)

    if len(conf.tests) != 0:
        print("In config.txt is old tests!")
        exit()

    generateTest(numOfTest, maxNumOfPoint, spase, conf.testFolder, "config.txt")

