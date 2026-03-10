##### CL6.5
accession = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

## Part A: contain the letters d and e in that order

import re

for a in accession:
     if re.search("d.*e", a):
        print("This is A:", a)

## Part B: contain both the letters d and e in any order

for a in accession:
    if re.search("d", a) and re.search("e", a):
        print("This is B: ", a)


## Part C: start with x or y and end with e
for a in accession:
    if re.search("^[xy].*e$",a):
        print("This is C: ", a)

## Part D: contain three or more numbers in a row
for a in accession:
    if re.search("[0-9]{3,}", a):
        print("This is D:", a)

## Part E: end with d followed by either a, r or p
for a in accession:
   if re.search('d[arp]$', a):
    print("This is E: ", a)
