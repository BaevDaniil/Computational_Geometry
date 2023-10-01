from polygon import polygon
import matplotlib.pyplot as plt
import config
import os
import ast

def main():
    print ([1.0, -0.0] == [1.0, 0.0])
    conf = config.config()
    conf.readConfig("config.txt")
    if not os.path.isdir(conf.resultFolder):
        os.mkdir(conf.resultFolder)
    
    for test in conf.tests:
        polygons = []
        with open(test[1], 'r') as testFile:
            for line in testFile:
                polygons.append(polygon(ast.literal_eval(line)))
            if len(polygons) != 2:
                print("Error in file: " + test[1] + "\nIn file expected two polygons in list format")
            else:
                intersection = polygons[0].intersecting(polygons[1])
                if conf.draw:
                    fig, ax = plt.subplots()
                    polygons[0].draw(ax, 'b')
                    polygons[1].draw(ax, 'r')
                    intersection.draw(ax, 'g')
                    fig.savefig(conf.resultFolder + '/' + test[0])
                resFile = open(conf.resultFolder + '/' + test[0] + '.txt', 'w')                  
                resFile.write(str(intersection.vertexes))
                resFile.close()

if __name__== "__main__":
    main()