import re
import sys
import getopt


def prepareName(fullname):
    nameParts = fullname.split(" ")
    return nameParts[0], nameParts[1]


def computeName(first, last, limit=None,):
    nameList = []
    nameList.append(first)
    nameList.append(last)
    nameList.append(first[0]+last)
    nameList.append(f"{first[:3]}{last[:3]}")
    nameList.append(first[0]+last)
    nameList.append(first[:2]+last)
    nameList.append((first[0]+last))

    if(limit):
        nameList = [word[:limit] for word in nameList]

    if(bool(re.match(r'[A-Z]+', first)) or re.match(r'[A-Z]+', last)):
        nameList += computeName(first.lower(), last.lower(), limit=limit)
    return nameList


def readWriteBizname(output, namefile, limit=None):
    with open(namefile) as readFile:
        with open(output, 'w') as out:
            for fullname in readFile.read().splitlines():
                name, lastname = prepareName(fullname)
                for bizname in computeName(name, lastname, limit):
                    if(bizname):
                        out.write(f'\n{bizname}')


def writeBizname(output, fullname, limit=None):
    with open(output, 'w') as out:
        name, lastname = prepareName(fullname)
        for bizname in computeName(name, lastname, limit):
            if(bizname):
                out.write(f'{bizname}\n')


def appendBizname(output, fullname, limit=None):
    with open(output, 'a+') as out:
        name, lastname = prepareName(fullname)
        for bizname in computeName(name, lastname, limit):
            if(bizname):
                out.write(f'\n{bizname}')


def main(argv):
    namefile = ''
    output = 'biznames.txt'
    singleName = ''
    limit = None
    try:
        opts, _ = getopt.getopt(
            argv, "l:n:o:w:", ["limit=", "name=", "output=", "wordlist="])
        for opt, arg in opts:
            if opt == "-o":
                output = arg
            if opt == "-l":
                limit = int(arg)
            if opt == "-w":
                namefile = arg
            if opt == "-n":
                singleName = arg

        if(singleName and namefile):
            readWriteBizname(output, namefile, limit)
            appendBizname(output, singleName, limit)
        else:
            readWriteBizname(output, namefile, limit) if namefile else writeBizname(
                output, singleName, limit)
    except:
        print(
            '''                                                                 
             ,,                                                                 
`7MM"""Yp,   db                                                                 
  MM    Yb                                                                      
  MM    dP `7MM  M"""MMV `7MMpMMMb.   ,6"Yb.  `7MMpMMMb.pMMMb.  .gP"Ya  ,pP"Ybd 
  MM"""bg.   MM  '  AMV    MM    MM  8)   MM    MM    MM    MM ,M'   Yb 8I   `" 
  MM    `Y   MM    AMV     MM    MM   ,pm9MM    MM    MM    MM 8M"""""" `YMMMa. 
  MM    ,9   MM   AMV  ,   MM    MM  8M   MM    MM    MM    MM YM.    , L.   I8 
.JMMmmmd9  .JMML.AMMmmmM .JMML  JMML.`Moo9^Yo..JMML  JMML  JMML.`Mbmmd' M9mmmP'                                                                          
''')
        print("[*] Args List [*]")
        print("|| -o output file")
        print("|| -w wordlist/namelist file")
        print("|| -n single name generate")
        print("|| -l username char limit")
        print("[*] use :")
        print("|| > python3 biznames.py -w fullnames.txt -o biznames.txt")
        print("|| > python3 biznames.py -n 'Niko Bellic' -o biznames.txt")


if __name__ == "__main__":
    main(sys.argv[1:])
