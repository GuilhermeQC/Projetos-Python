copo1 = "laranja"
copo2 = "acerola"

print(f"Copo 1: {copo1}. Copo 2: {copo2}.")

#Solução apresentada pelo livro:
# copo1, copo2 = copo2, copo1 #

if copo1 != "acerola":
    copo3 = copo1
    copo1 = copo2
    copo2 = copo3

    print(f"Copo 1: {copo1}. Copo 2: {copo2}.")
