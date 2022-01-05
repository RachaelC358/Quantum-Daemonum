# Program by Rachael Carpenter
#
# Quantum Daemonum 
# A simple game where you play as as a wicked spirit in a battle with
# Van Helsing who is played by a quantum computer. Van Helsing will
# attempt to guess your true name in an attempt to gain power over and
# and defeat you. You can attempt to thwart him with spiritual attacks
# that can either weaken his ability to guess or hide your name entirely.
#


from configparser import RawConfigParser
import random
import qiskit
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit.providers.aer import QasmSimulator
import time
import operator
import math
import ast
import numpy as np

                                                                                
#
def runGame(program):
    shots = 100
    # execute program on quantum simulator
    job = qiskit.execute(program, qiskit.Aer.get_backend('qasm_simulator'), shots=shots)
    result = job.result().get_counts()
    return result


#def battleStatus(points):



# utility function called by quantumGuess
def quantumProcessing(quessProcess, qreg, hiddenName):
    # Convert hiddenName in binary from list to array
    secretName = list(hiddenName)
    
    secretName.reverse()
    indexList = []

    for i in range(len(secretName)):
        if (secretName[i] == '0'):
            indexList.append(i)
    
    # Find all bits in the array with a value of 0
    #indexList = np.where(secretName == 0)
    #print(len(indexList))
    #print(indexList)

    # Invert the 0s
    for i in range(len(indexList)):
        # find bits with a value of 0
        anIndex = indexList[i]
        
        # Invert qubit
        quessProcess.x(qreg[anIndex])
        

    

def quantumGuess(hiddenName):
    # 4-bit Grover's search to identify target index of 4 bits from list of all combinations of 4 bits
    # create 2 qubits for input
    qreg = QuantumRegister(4)
    # these 2 registers take output
    creg = ClassicalRegister(4)
    guessProcess = QuantumCircuit(qreg, creg)

    
    # place qubits into superposition, representing all possible outcomes(starting position)
    guessProcess.h(qreg)

   
    # Run quantumProcessing on key, inverting bits with value of zero
    quantumProcessing(guessProcess, qreg, hiddenName) # um never runs???
    

    
    #Grover's Algorithm
    guessProcess.cp(np.pi / 4, qreg[0], qreg[3])
    guessProcess.cx(qreg[0], qreg[1])
    guessProcess.cp(-np.pi / 4, qreg[1], qreg[3])
    guessProcess.cx(qreg[0], qreg[1])
    guessProcess.cp(np.pi / 4, qreg[1], qreg[3])
    guessProcess.cx(qreg[1], qreg[2])
    guessProcess.cp(-np.pi / 4, qreg[2], qreg[3])
    guessProcess.cx(qreg[0], qreg[2])
    guessProcess.cp(np.pi / 4, qreg[2], qreg[3])
    guessProcess.cx(qreg[1], qreg[2])
    guessProcess.cp(-np.pi / 4, qreg[2], qreg[3])
    guessProcess.cx(qreg[0], qreg[2])
    guessProcess.cp(np.pi / 4, qreg[2], qreg[3])
   

    #Reverse the earlier inversions by guessProcessing
    quantumProcessing(guessProcess, qreg, hiddenName)

    #Amplification
    guessProcess.h(qreg)
    guessProcess.x(qreg)

    
 
    #apply grover's algorithm again for amplification
    guessProcess.cp(np.pi / 4, qreg[0], qreg[3])
    guessProcess.cx(qreg[0], qreg[1])
    guessProcess.cp(-np.pi / 4, qreg[1], qreg[3])
    guessProcess.cx(qreg[0], qreg[1])
    guessProcess.cp(np.pi / 4, qreg[1], qreg[3])
    guessProcess.cx(qreg[1], qreg[2])
    guessProcess.cp(-np.pi / 4, qreg[2], qreg[3])
    guessProcess.cx(qreg[0], qreg[2])
    guessProcess.cp(np.pi / 4, qreg[2], qreg[3])
    guessProcess.cx(qreg[1], qreg[2])
    guessProcess.cp(-np.pi / 4, qreg[2], qreg[3])
    guessProcess.cx(qreg[0], qreg[2])
    guessProcess.cp(np.pi / 4, qreg[2], qreg[3])

    
    # Reverse amplification
    guessProcess.x(qreg)
    guessProcess.h(qreg)

    # Measure results
    guessProcess.barrier(qreg)
    guessProcess.measure(qreg, creg)

   

    #check for error, if result matches one of the given names
    results = runGame(guessProcess)
    foundName = max(results.items(), key=operator.itemgetter(1))[0]

    # convert binary result to character array
    resultArray = list(foundName)

    # convert character array in integers
    resultArrayInt = [int(i) for i in resultArray]
    

    stringy = ''.join([str(item) for item in resultArrayInt])
    
    myIndex = int(stringy, 2)
    #convert result to index in name array
    return myIndex

    

def action(read):
    read = read.lower(0);

    #switcher = {
    # thwart
    #'t':
    # 
    #'':
    #
    #'':

    return switcher.get(read[0], -1)
    


def getDemonName(index):
    demonNames = {
        1:'Dusios',
        2:'Belial',
        3:'Belphegor', 
        4:'Andromalius',
        5:'Astaroth',
        6:'Beleth',
        7:'Drekevac',
        8:'Demiurge',
        9:'Forneus',
        10:'Gomory',
        11:'Haures',
        12:'Pithius',
        13:'Mammon',
        14:'Marchosias',
        15:'Moloch',
        16:'Naphula'
    }
    return demonNames.get(index)


def response(read):
    read = str(read)
    read = read.lower()
    switcher = {
        'y': 1,
        'n': 0,
        'q': 0
    }

    return switcher.get(read[0], -1)


def main():
    #print welcome message
    print("   __                 ___                __        ___        __")
    print("  /  \ |  |  /\  |\ |  |  |  |  |\/|    |  \  /\  |__   |\/| /  \ |\ | |  |  |\/|")
    print("  \__X \__/ /~~\ | \|  |  \__/  |  |    |__/ /~~\ |___  |  | \__/ | \| \__/  |  |")
    print("           ~ A DARK GAME PLAYED AGAINST A SIMULATED QUANTUM COMPUTER ~")
    print("")
    print("")
    print(" The year is 1887.")
    print("")
    print(" You are a wicked spirit, evil personified, who is being hunted by Van Helsing, the")
    print(" infamous slayer of unholy beasts. He will try to destroy you by guessing your true")
    print(" name. You must stop him at any cost. A battle of magic and wits begins!")
    print("")
    print(" Use keyboard commands to attempt to thwart Van Helsing, who makes guesses using")
    print(" Grover's search algorithm, which runs on a quantum simulator.")
    print("")
    print(" Van Helsing has you cornered in the caverns below Corvin Castle in Romania. He")
    print(" performs the rites of excorcism while you have your powers of psychic blasting, ")
    print("")
    print("")

    quitGame = False

    #Begin main loop of game
    while not quitGame:
        # pick the true name for this game from name array
        playerName = random.randint(1, 16)
        playerName = playerName - 1
        trueName = getDemonName(playerName)
        print(" Your true name is ... " + str(trueName))
        # convert player name index int to binary
        secretBinary = format(playerName,"04b")

        gameOver = False
        evil = 100
        turns = 0
        loopControl = 1
        VHResult = ""
        
        print(" +:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+") 
        print("")
        roundStr = str(loopControl)
        evilStr = str(evil)
        print(" Round: ", roundStr.rjust(5))
        print(" Evil : ", evilStr.rjust(5))
        # get player input
        print("")
        text = ''
        #while not text.lower() in ['u','d','q','up','down','quit']:
        # parse input

        #process input

        #process on quantum simulator, VH will guess now
        while not gameOver:
            #let the computer guess
            VHResult = quantumGuess(secretBinary)

            #convert index of name into the correct range
            #nameIndex = VHResult -

            print(" Van Helsing Guesses: " + getDemonName(VHResult))
        

            #check player progress
            if  (VHResult != "" and str(getDemonName(VHResult)) == str(trueName)):
                print(" GAME OVER")
                gameOver = True
            continue

        loopControl = loopControl + 1
        read = ''
        while not read.lower() in ['y','n','q','yes','no','quit']:
                #Read input from user
                read = input("\n +:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+\n" + 
                              "\n [yes, no, quit]: ").lower()
        print(read)
        actionCode = -1
        actionCode = response(read)
        print("actionCode: ",actionCode)
        if actionCode == 0:
            quitGame =  True
        elif actionCode == 1:
            gameOver = False
            continue
        else:
            print(" What?")
        

        
if __name__ == "__main__":
    main()
    
    
