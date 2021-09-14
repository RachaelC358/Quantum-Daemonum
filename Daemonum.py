#
# Quantum Daemonum 
# A simple game where you play as as a wicked spirit in a battle with
# Van Helsing who is played by a quantum computer. Van Helsing will
# attempt to guess your true name in an attempt to gain power over and
# and defeat you. You can attempt to thwart him with spiritual attacks
# that can either weaken his ability to guess or hide your name entirely.
#


import qiskit
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import IBMQ
import math


def runGame(programType):
    if ProgramType == 'real':
    # execute program on real quantum computer
    else:
    # execute program on quantum simulator
        start = time.time();
        job = qiskit.execute(program, qiskit.Aer.get_backend('qasm-simulator'), shots=shots)
        result = job.result().get_counts()
        stop = time.time();

def battleStatus(points):

    
def guessingGame():
    print("VH attempts to guess your name.")
    # quantum computer generates VH's guess
    qComputerResult = quantumGuess(secretName)
    if 
    else
    command = input


def guantumGuess()    
    # 4-bit Grover's search

def action(option):
    option = option.lower(0);

    switcher = {
    # thwart
    't':
    # 
    '':
    #
    '':
    }


def getDemonName(index):
    names = {
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
