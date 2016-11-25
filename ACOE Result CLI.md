
# ACOE Result CLI

## Get Input from user

Get the Registeration number and Password from the user using the option `-n` for new entry


```bash
#!/bin/bash

if [ "$1" = "-n" ]; then
    echo ""
    echo -n "Register Number: "
    read REGISTER
    
```

Read Password in hidden mode using option `-s` with read function


```bash
    echo -n "Password: "
    read -s P
    echo
```

## Encrypt the password

Encrypt the Password using **SHA512**


```bash
    PASSWORD=`echo -n $P | openssl dgst -sha512`
    LEN=`expr ${#PASSWORD} - 9`
    PASSWORD=${PASSWORD:9:$LEN}
```


```bash
else
    REGISTER="XXXXXX"
    PASSWORD="YYYYYY"
fi
```


```bash
if [ "$REGISTER" = "XXXXXX" ]; then
    echo "Hey, Please install properly to stop seeing this message! Execute the following Command"
    echo "cd ~/ACOE-Result-Command-Line && sudo make install"
    echo
    echo "To check the result manually, execute the following command"
    echo "auresult -n"
fi
```

## Create a Cookie for ACOE site

Pass the Registration number and Password as arguments for `curl` function and create `.c0.txt` cookie file


```bash
echo "Please be patient..."

if curl --connect-timeout 10 -c .c0.txt -s --data "user=$REGISTER&password=&p=$PASSWORD" https://acoe.annauniv.edu/student/process_login.php; then
    
```

## Scrap the Result

Scrap the page https://acoe.annauniv.edu/student/result.php by passing the cookie to curl function and save it in **.temp**


```bash
    curl -s -b .c0.txt https://acoe.annauniv.edu/student/result.php > .temp
    echo 
```

## Create a Python Script

Create a Python Script for displaying the Results


```bash
    echo '
# import dependencies
from bs4 import BeautifulSoup
from prettytable import PrettyTable
```

Read **./.temp** and parse it using `BeautifulSoup`


```bash
page = open("./.temp", "r").read()
soup = BeautifulSoup(page, "html.parser")
```

Filter all `table` tags and store it in `results`


```bash
results = soup.findAll("table")
```

Give **Headings** for the table to be displayed


```bash
res = ["REGULAR", "ARREAR", "REVALUATION"]
```

Display Regular, Arrear and Revaluation Results separately


```bash
i = 0
for result in results:
        if result.findParent("table") is None:
                print "\t\t\t\t%s" % res[i]     
```

## Create a PrettyTable

Create a `PrettyTable` with columns of Subject Code, Subject Name and Grade


```bash
                t = PrettyTable(["Subject Code", "Subject Name", "Grade"])
                
```

Parse every table row by filtering `tr`


```bash
                for tr in result.find_all("tr")[1:]:
                        
```

Parse every table data field by filtering `td` and add a row to the `PrettyTable`


```bash
                        tds = tr.find_all("td")
                        t.add_row([tds[0].text, tds[1].text, tds[2].text])
```

## Print the PrettyTable


```bash
                print t
                print "\n"
                i+=1
' > .display.py
```

## Run the Python Script

Run the Python Script `.display.py`


```bash
    python .display.py
    
```


```bash
Remove unnecessary files like `.display.py`,`.c0.txt` and `.temp`
```


```bash
    rm .display.py .c0.txt .temp
else
    echo
    echo "ACOE server is down! Try after sometime"
fi
```

Thus we have built a working code for displaying **ACOE results**. Check our [GitHub Page](https://github.com/lost-plus-found/ACOE-Result-Command-Line) for code. We have a few other projects in our [Organization](https://github.com/lost-plus-found)
