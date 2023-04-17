# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
'''

# Solution one, This works but is not good enough
def DNA_strand(dna):
	result = []
	for i in dna:
		if i == "A":
			result.append("T")
		elif i == "T":
			result.append("A")
		elif i == "G":
			result.append("C")
		elif i == "C":
			result.append("G")
	return "".join(result)

print(DNA_strand("ATATAATATTACGCGGCGC"))

# Solution two
def DNA_strand(dna):
	dna = dna.replace("T", "a")
	dna = dna.replace("A", "t")
	dna = dna.replace("C", "g")
	dna = dna.replace("G", "c")
	return dna.upper()

print(DNA_strand("ATATAATATTACGCGGCGC"))


