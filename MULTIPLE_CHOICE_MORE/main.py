# TÖBBVÁLASZTÁSOS kérdés generáló moodle-höz 1 helyes válasszal, GIFT formátumban

# Elvárt sor excelben:
# KÉRDÉS CÍME | KÉRDÉS | Helyes válaszok száma(N) | Helyes válasz 1 | Helyes válasz 2 | ... | Helyes válasz N | Rossz válasz 1 | Rossz válasz 2 | ... | Rossz válasz M

# Generált kérdés hozzá:
# :: KÉRDÉS CÍME :: KÉRDÉS { ~%50%Helyes válasz ~%50%Helyes válasz 2 ~%0%Rossz válasz 1 ~%0%Rossz válasz 2 ... }
# ::Grants tomb::Who is buried in Grant's tomb in New York City? { ~%50%Grant ~%50%Grant's wife ~%0%No one ~%0%Napoleon ~%0%Churchill ~%0%Mother Teresa }

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
file_name="MULTIPLECHOICE_1/input.csv"
with open(file_name,encoding="UTF-8") as file:
    multiple_choice_1_generator(file)
