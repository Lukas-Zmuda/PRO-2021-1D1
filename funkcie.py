# Tu napíšte svoj kód :-)

meno = "Lukas"
#print("Stredna odborna skola informacnych technologii")
print(meno)

def skola():
    print("+------------------------------------------------+")
    print("| Stredna odborna skola informacnych technologii |")
    print("+------------------------------------------------+")

#volanie funkcie
#skola()
#print("Fero")
#print("daco")
#skola()
#print("********************")
for i in range(5):
    skola()

def vitaj(meno_studenta):
    skola()
    print("Vitaj " + meno_studenta + " na nasej skole.")

def privitanie(meno_studenta, rok_narodenia):
    vek = 2021 - rok_narodenia
    print("Ahoj " + meno_studenta + ". Mas " + str(vek) + " rokov.")
vitaj("Peter")

vitaj("Katka")
