# Business Username Generator

```
             ,,                                                                 
`7MM"""Yp,   db                                                                 
  MM    Yb                                                                      
  MM    dP `7MM  M"""MMV `7MMpMMMb.   ,6"Yb.  `7MMpMMMb.pMMMb.  .gP"Ya  ,pP"Ybd 
  MM"""bg.   MM  '  AMV    MM    MM  8)   MM    MM    MM    MM ,M'   Yb 8I   `" 
  MM    `Y   MM    AMV     MM    MM   ,pm9MM    MM    MM    MM 8M"""""" `YMMMa. 
  MM    ,9   MM   AMV  ,   MM    MM  8M   MM    MM    MM    MM YM.    , L.   I8 
.JMMmmmd9  .JMML.AMMmmmM .JMML  JMML.`Moo9^Yo..JMML  JMML  JMML.`Mbmmd' M9mmmP
```

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