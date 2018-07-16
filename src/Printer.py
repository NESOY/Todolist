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
        self.printDoingList2(todoList, color.OKBLUE)

    def printDoneList(self, todoList):
        self.printGreenHeader("➤ Done List")
        self.printList(todoList, color.OKGREEN)

    def printDoingList2(self, todoList, stringColor):
        if(len(todoList) > 0):
            index = 1
            for todo in todoList:
                status = todo[1]
                desc = todo[2]
                startTime = todo[3]
                usedTime = Printer.getUsingTime(startTime)
                hours, remainder = divmod(int(usedTime),60*60)
                minutes, seconds = divmod(remainder,60)
                print(stringColor + "#          " + color.ENDC + color.OKGREEN + status + ": " + color.ENDC + "[" + str(index) + "] " + stringColor + desc + color.ENDC + " " + color.BOLD + str(hours) + ":" + str(minutes) + ":" + str(seconds) + color.ENDC)
                index += 1

    def printList(self, todoList, stringColor):
        if(len(todoList) > 0):
            index = 1
            for todo in todoList:
                status = todo[1]
                desc = todo[2]
                print(stringColor + "#          " + color.ENDC + color.OKGREEN + status + ": " + color.ENDC + "[" + str(index) + "] " + stringColor + desc + color.ENDC)
                index += 1

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