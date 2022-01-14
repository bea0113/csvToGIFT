# TÖBBVÁLASZTÁSOS kérdés generáló moodle-höz 1 helyes válasszal, GIFT formátumban

# Elvárt sor excelben, Igaznál vagy hamisnál egy "x":
# KÉRDÉS CÍME | KÉRDÉS | Helyes válasz | Rossz válasz 1 | Rossz válasz 2 | Rossz válasz 3 | ...

# Generált kérdés hozzá:
# :: KÉRDÉS CÍME :: KÉRDÉS { =Helyes válasz ~Rossz válasz 1 ~Rossz válasz 2 ~Rossz válasz 3 ... }
# ::Grants tomb::Who is buried in Grant's tomb in New York City? { =Grant ~No one ~Napoleon ~Churchill ~Mother Teresa }

def multiple_choice_1_generator(_file):
    lines = []
    for line in _file:
        if  not line.__contains__(";Kérdés;"):
            line = line.strip("\n").split(";")
            lines.append(line)
    sample_text = """::{0}::{1}{{={2} """
    for each in lines:
        result = sample_text.format(*each)
        for wrong in each[3:]:
            result+="~"+wrong+" "
        result+="}"
        
        print(result,end="\n\n")

# ÍRD ÁT A FILE NEVET!!
file_name="MULTIPLECHOICE_1/multiple_choice_1.csv"
with open(file_name,encoding="UTF-8") as file:
    multiple_choice_1_generator(file)
