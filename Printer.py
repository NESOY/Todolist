class Printer:
    @staticmethod
    def printYelloHeader(string):
        print(color.BOLD + color.WARNING + string + color.ENDC)
    
    @staticmethod
    def printGreenHeader(string):
        print(color.BOLD + color.OKGREEN + string + color.ENDC)
    
    @staticmethod
    def printBlueHeader(string):
        print(color.BOLD + color.OKBLUE + string + color.ENDC)

    @staticmethod
    def printAllList(todoList, doingList, doneList):
        Printer.printTodoList(todoList)
        Printer.printDoingList(doingList)
        Printer.printDoneList(doneList)

    @staticmethod
    def printTodoList(todoList):
        Printer.printYelloHeader("➤ Todo List")
        Printer.printList(todoList, color.WARNING)

    @staticmethod
    def printDoingList(todoList):
        Printer.printBlueHeader("➤ Doing List")
        Printer.printDoingList2(todoList, color.OKBLUE)

    @staticmethod
    def printDoneList(todoList):
        Printer.printGreenHeader("➤ Done List")
        Printer.printList(todoList, color.OKGREEN)

    @staticmethod
    def printDoingList2(todoList, stringColor):
        if(len(todoList) > 0):
            index = 1
            for todo in todoList:
                status = todo[1]
                desc = todo[2]
                startTime = todo[3]
                usedTime = getUsingTime(startTime)
                hours, remainder = divmod(int(usedTime),60*60)
                minutes, seconds = divmod(remainder,60)
                print(stringColor + "#          " + color.ENDC + color.OKGREEN + status + ": " + color.ENDC + "[" + str(index) + "] " + stringColor + desc + color.ENDC + " " + color.BOLD + str(hours) + ":" + str(minutes) + ":" + str(seconds) + color.ENDC)
                index += 1

    @staticmethod
    def printList(todoList, stringColor):
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