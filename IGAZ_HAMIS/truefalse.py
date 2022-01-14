# IGAZ - HAMIS kérdés generáló moodle-höz, GIFT formátumban

# Elvárt sor excelben, Igaznál vagy hamisnál egy "x":
# KÉRDÉS CÍME | KÉRDÉS | Igaz | Hamis

# Generált kérdés hozzá:
# :: KÉRDÉS CÍME :: KÉRDÉS {HELYES VÁLASZ}
# ::FalseStatement about sun::The sun rises in the West.{FALSE}

def true_false_generator(_file):
    lines = []
    for line in _file:
        if  not line.__contains__("Kérdés;Igaz"):
            line = line.strip("\n").split(";")
            res = "TRUE" if line[2]=="x" else "FALSE"
            lines.append([line[0],line[1],res])
    sample_text = """::{0}::{1}{{{2}}}"""
    for each in lines:
        result = sample_text.format(*each)
        print(result)

with open("truefalse.csv",encoding="UTF-8") as file:
    true_false_generator(file)
