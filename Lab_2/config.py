import re

class config:
    def __init__(self) -> None:
        self.resultFolder = ""
        self.testFolder = ""
        self.tests = []
        self.draw = False

    def readConfig(self, name: str):
        with open(name, 'r') as conf:
            for line in conf:
                if (re.fullmatch(r'\s*(#.*)?\s*', line)):
                    continue
                check = re.fullmatch(r'\s*result:\s*(.*)\s*$', line)
                if check != None:
                    self.resultFolder = check.group(1)
                    continue
                check = re.fullmatch(r'\s*test:\s*(.*)\s*$', line)
                if check != None:
                    self.testFolder = check.group(1)
                    continue
                check = re.fullmatch(r'\s*(\w[\w\d]*):\s*(.*\.txt)\s*$', line)
                if check != None:
                    self.tests.append([check.group(1), check.group(2)])
                    continue
                check = re.fullmatch(r'\s*draw:\s*((True)|(False))\s*', line)
                if check != None:
                    self.draw = check.group(1) == "True"
                    continue
                print("Unexpexted string: ", line)