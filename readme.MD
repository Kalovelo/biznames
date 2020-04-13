# Business Username Generator

### enumerating users?
Here's a script to generate a possible list of usernames.  
Created for using it on Hackthebox pentesting challenges.

Generations based on :
https://activedirectorypro.com/create-bulk-users-active-directory/

| arg | use                             | example          |
| --- | ------------------------------- | ---------------- |
| -o  | output file                     | -o biznames.txt  |
| -w  | wordlist / namelist file        | -w fullnames.txt |
| -n  | generate output for single name | -n 'Niko Bellic' |
| -l  | username char limit             | -l 5             |

#### use 
```bash
python3 biznames.py -w fullnames.txt -o biznames.txt
```
```bash
python3 biznames.py -n 'Niko Bellic' -o biznames.txt -l 5
```