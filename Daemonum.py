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
from qiskit import IBMQ
import time
import operator
import math
import ast

                                                                                

def runGame():
    # execute program on quantum simulator
    start = time.time();
    job = qiskit.execute(program, qiskit.Aer.get_backend('qasm-simulator'), shots=shots)
    result = job.result().get_counts()
    stop = time.time();

#def battleStatus(points):

    
def guessingGame():
    print("Van Helsing attempts to guess your name.")
    # quantum computer generates VH's guess
    qComputerResult = quantumGuess(secretName)
    #if 
    #else
    command = input

# utility function called by quantumGuess
def quantumProcessing(quessProgram, qreg, hiddenName):
    # Convert hiddenName in binary from list to array
    hiddenName = np.asarray(hiddenName)

    # Find all bits in the array with a value of 0
    indexList = np.where(secret == 0)[0]

    # Invert the 0s
    for i in range(len(indexList)):
        #
        anIndex = int(len(secret) - 1 - indexList[i])
        
        # Invert qubit
        quessProgram.x(qr[anIndex])
    

def guantumGuess():    
    # 4-bit Grover's search
    # create 2 qubits
    qreg = QuantumRegister(4)
    # these 2 registers take output
    creg = ClassicalRegister(4)

    # place qubits into superposition, representing all possible outcomes
    guessProcess.h(qreg)

    # Run quantumProcessing on key, inverting bits
    quantumProcessing(guessProcess, qreg, hiddenName)

    #Grover's Algorithm
    guessProcess.cul(np.pi / 4, qr[0], qr[3])
    guessProcess.cx(qr[0], qr[1])
    guessProcess.cul(-np.pi / 4, qr[1], qr[3])
    guessProcess.cx(qr[0], qr[1])
    guessProcess.cul(np.pi / 4, qr[1], qr[3])
    guessProcess.cx(qr[1], qr[2])
    guessProcess.cul(-np.pi / 4, qr[2], qr[3])
    guessProcess.cx(qr[0], qr[2])
    guessProcess.cul(np.pi / 4, qr[2], qr[3])
    guessProcess.cx(qr[1], qr[2])
    guessProcess.cul(-np.pi / 4, qr[2], qr[3])
    guessProcess.cx(qr[0], qr[2])
    guessProcess.cul(np.pi / 4, qr[2], qr[3])

    #Reverse the earlier inversions
    quantumProcessing(guessProcess, qr, hiddenName)

    #Amplification
    guessProcess.h(qr)
    guessProcess.x(qr)

    #apply grover's algorithm again
    guessProcess.cul(np.pi / 4, qr[0], qr[3])
    guessProcess.cx(qr[0], qr[1])
    guessProcess.cul(-np.pi / 4, qr[1], qr[3])
    guessProcess.cx(qr[0], qr[1])
    guessProcess.cul(np.pi / 4, qr[1], qr[3])
    guessProcess.cx(qr[1], qr[2])
    guessProcess.cul(-np.pi / 4, qr[2], qr[3])
    guessProcess.cx(qr[0], qr[2])
    guessProcess.cul(np.pi / 4, qr[2], qr[3])
    guessProcess.cx(qr[1], qr[2])
    guessProcess.cul(-np.pi / 4, qr[2], qr[3])
    guessProcess.cx(qr[0], qr[2])
    guessProcess.cul(np.pi / 4, qr[2], qr[3])

    # Reverse amplification
    guessProcess.x(qr)
    guessProcess.h(qr)

    # Measure results
    guessProcess.barrier(qr)
    guessProcess.measure(qr, cr)

    #check for error, if result matches one of the given names
    result = run(guessProcess, device)
    print(result)
    foundName = max(result.items(), key=operator.itemgetter(1))[0]

    # convert binary result to character array
    resultArray = list(foundName)

    # convert character array in integers
    resultArrayInt = [int(i) for i in arrResult]

    #convert result to index in name array
    return bitsToInt(resultArrayInt)

    

def action(option):
    option = option.lower(0);

    #switcher = {
    # thwart
    #'t':
    # 
    #'':
    #
    #'':
    


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
    print(" infamous slayer of unholy beasts. He will try to destroy you by guessing your true name.")
    print(" You must stop him at any cost. A battle of magic and wits begins!")
    print("")
    print(" Use keyboard commands to attempt to thwart Van Helsing, who makes guesses using")
    print(" Grover's search algorithm, which runs on a quantum simulator.")
    print("")
    print(" Van Helsing has you cornered in the caverns below Corvin Castle in Romania. He")
    print(" performs the rites of excorcism while you have your powers of psychic blasting, ")
    print(" ")
    print("")

    # pick the true name for this game from name array
    playerName = random.randint(1, 16)
    print(" index: " + str(playerName))
    trueName = getDemonName(playerName)
    print(" Your true name is ... " + str(trueName))

    #run.isInit = False
    gameOver = False
    evil = 100
    turns = 0
    loopControl = 1

    #Begin main loop of game
    while not gameOver:
        print(" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #if (loopControl == 1): 
            
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

        #process on quantum simulator

        #check player progress
        loopControl = loopControl + 1
        if (loopControl >= 4):
            gameOver = True

        
if __name__ == "__main__":
    main()
    
    
