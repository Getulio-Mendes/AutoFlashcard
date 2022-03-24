def parseLines():
    newDic = {}
    for line in dic:
        try:
            char = line.split(' ',2)[1]
            defi = line.split('/',1)[-1][:-1]
        
            if char in newDic:
                # hard code limit of different definitions
                for i in range(6):
                    if i==0 and char+'1' not in newDic:
                        newDic[char+'1'] = defi 
                        break

                    elif char+str(i) in newDic:
                        newDic[char+str(i+1)] = defi 
                        break
            else:
                newDic[char] = defi
        except:
            print(f"Failed to parse: {line}")
            continue

    return newDic

def getDicDef(char):
    question = f"Use definition for {char}:"
    count = 1
    answer = dic[char]

    if char in dic.keys():
        for i in range(6):
            if i==0 and char in dic:
                question += f"\n{i}:{dic[char]}\n"
            elif char+str(i) in dic:
                question += f"\n{i}:{dic[char+str(i)]}\n"
                count += 1

        if count != 1:
            opt = input(question)
            if opt == '0':
                answer = dic[char]
            else:
                answer = dic[char+str(opt)]
        return answer

    else:
        return f"Failed to get {char}"

with open("./Dictionaries/cedict_ts.u8","r",encoding='utf8') as file:
    dic = file.read()
    dic = dic.split('\n')
    dic = parseLines()
