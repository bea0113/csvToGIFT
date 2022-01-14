# PÁROSÍTÓS kérdés generáló moodle-höz, GIFT formátumban

# Elvárt sor excelben, A1-a1 alkot egy párt, legalább 3 pár kell, különben nem működik!:
# KÉRDÉS | A1 | a1 | A2 | a2 | A3 | a3

# Generált kérdés hozzá:
# KÉRDÉS { =A1 -> a1 =A2 -> a2 =A3 -> a3 }
# Match the following countries with their corresponding capitals. { =Canada -> Ottawa =Italy  -> Rome =Japan  -> Tokyo =India  -> New Delhi }
def matching_generator(_file):
    lines = []
    for line in _file:
        if not line.__contains__(";KÉRDÉS;"):
            line = line.strip("\n").split(";")
            lines.append(line)
    sample_text = """{0}{{ """
    for each in lines:
        result = sample_text.format(each[0])
        for i in range(1,len(each),2):
            result+=" ="+each[i]+" -> " +each[i+1]
        result+=" }"
        
        print(result,end="\n\n")

# ÍRD ÁT A FILE NEVET!!
file_name="MATCHING/input.csv"
with open(file_name,encoding="UTF-8") as file:
    matching_generator(file)
(file)
