import datetime

from string import Template

class Printer:
    def printYelloHeader(self, string):
        print(color.BOLD + color.WARNING + string + color.ENDC)
    
    def printGreenHeader(self, string):
        print(color.BOLD + color.OKGREEN + string + color.ENDC)

    def printBlueHeader(self, string):
        print(color.BOLD + color.OKBLUE + string + color.ENDC)

    def printTodoList(self, todoList):
        self.printYelloHeader("➤ Todo List")
        self.printList(todoList, color.WARNING)

    def printDoingList(self, todoList):
        self.printBlueHeader("➤ Doing List")
        self.printDoingWithTime(todoList, color.OKBLUE)

    def printDoneList(self, todoList):
        self.printGreenHeader("➤ Done List")
        self.printList(todoList, color.OKGREEN)

    def printDoingWithTime(self, todoList, stringColor):
        if(len(todoList) > 0):
            index = 1
            for todo in todoList:
                status = todo[1]
                desc = todo[2]
                startTime = todo[3]
                start = datetime.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
                now = datetime.datetime.now()
                usedTime = now - start
                time = self.strfdelta(usedTime,'%H:%M:%S')
                print(stringColor + "#          " + color.ENDC + color.OKGREEN + status + ": " + color.ENDC + "[" + str(index) + "] " + stringColor + desc + color.ENDC + " " + color.BOLD + time + color.ENDC)
                index += 1

    def printList(self, todoList, stringColor):
        if(len(todoList) > 0):
            index = 1
            for todo in todoList:
                status = todo[1]
                desc = todo[2]
                print(stringColor + "#          " + color.ENDC + color.OKGREEN + status + ": " + color.ENDC + "[" + str(index) + "] " + stringColor + desc + color.ENDC)
                index += 1
    
    def strfdelta(self, tdelta, fmt):
        d = {"D": tdelta.days}
        hours, rem = divmod(tdelta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        d["H"] = '{:02d}'.format(hours)
        d["M"] = '{:02d}'.format(minutes)
        d["S"] = '{:02d}'.format(seconds)
        t = DeltaTemplate(fmt)
        return t.substitute(**d)

# Color
class color:
    WHITE = '\033[37m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class DeltaTemplate(Template):
    delimiter = "%"