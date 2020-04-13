#!/usr/bin/python
import re
import sys


def prepareName(fullname):
    nameParts = fullname.split(" ")
    return nameParts[0], nameParts[1]


biznames = []


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


with open('fullnames.txt') as readFile:
    with open('biznames.txt', 'w') as out:
        for fullname in readFile.read().splitlines():
            name, lastname = prepareName(fullname)
            for bizname in computeName(name, lastname):
                if(bizname):
                    out.write(f'\n{bizname}')
