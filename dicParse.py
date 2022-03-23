def parseLines():
    simplified = []
    definition = []
    for line in dic:
        definition.append(line.split('/',1)[-1][:-1])
        try:
            simplified.append(line.split(' ',2)[1])
        except:
            print(line)

    return dict(zip(simplified,definition))

def getDicDef(simplified):
    if simplified in dic.keys():
        return dic[simplified]
    else:
        return "Failed to get"

with open("./Dictionaries/cedict_ts.u8","r",encoding='utf8') as file:
    dic = file.read()
    dic = dic.split('\n')
    dic = parseLines()
