# Read data from input file
def checkValid(input):
    allValid = True
    errorCodes = []
    for element in input:
        element = element.split(' ')
        if element[1] == 'false':
            errorCodes.append(element[2])
    if len(errorCodes) != 0:
        allValid = False
    if allValid == True:
        return ("Yes")
    else:
        return ("No"+'\n'+' '.join(errorCodes))
import sys
if __name__ == '__main__':
    input =  []
    length = int(sys.stdin.readline().strip())
    for i in range(length):
        line = sys.stdin.readline().strip()
        input.append(line)
    sys.stdout.write(checkValid(input))
