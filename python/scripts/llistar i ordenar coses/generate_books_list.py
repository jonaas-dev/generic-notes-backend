
# 23/12/20
# Llistar contingut d'un determinat directori
"""
	LLista tots els llibres (documents) per categories (carpetes) i
	realitza un sumatori que s'exposa al final del bucle.
"""


import os
import sys

path = 'E:/MEGA/MATERIAL_DE_CONSULTA/Lectura/LLIBRES/'
n_books = 0

# Main 

sys.stdout = open("Inventari_llibres.txt", "w")

print("Inventari dels llibres per categoria ... ")
entries = os.listdir(path)

for entry in entries:
	sub_entries = os.listdir(path + entry)
	n_books += len(sub_entries)

	# Category of books
	print("## ", entry, " (", len(sub_entries), ")") 
	print('-' * 100) # Print line 

	# Print entries (books)
	for sub_entry in sub_entries:
		print(sub_entry)
	print() # endl

print('-' * 100) # Print line
print("Total llibres: ", n_books)

sys.stdout.close()