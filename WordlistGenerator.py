import string


n = string.printable[10:36]

base = "fsrwjcfszeg"

generated = ""


with open("wordlist.txt" , "w") as f:
    for i in n:
        for j in n:
            for k in n:
                for z in n:
                    for l in n:
                        generated = base+i+j+k+z+l
                        f.write(f"{generated}\n")
print(n)