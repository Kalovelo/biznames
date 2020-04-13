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


def WriteBizname(output, fullname, limit=None):
    with open(output, 'w') as out:
        name, lastname = prepareName(fullname)
        for bizname in computeName(name, lastname, limit):
            if(bizname):
                out.write(f'{bizname}\n')


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

        if(singleName):
            WriteBizname(output, singleName, limit)
        else:
            readWriteBizname(output, namefile, limit)
    except Exception as error:
        print(error)
        print("==== BUSINESS NAME GENERATOR ====")
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
