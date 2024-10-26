"""
Main like scrypt to process al the data into one.
"""

import subprocess
subprocess.run(['python', 'Code/DataProcessing/MovesetProcessor.py'])
print("processed movesets")
subprocess.run(['python', 'Code/DataProcessing/PokemonProcessor.py'])
print("processed moves")
subprocess.run(['python', 'Code/DataProcessing/MovesProcessor.py'])
