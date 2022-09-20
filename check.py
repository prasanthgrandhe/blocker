from time import *  
from datetime import *



host_path = r"C:\Windows\System32\drivers\etc\hosts"  
redirect = "127.0.0.1"
# websites = ["www.facebook.com", "https://www.facebook.com"]

f1 = open("hos.txt","r")
s = f1.readlines()
f1.close()

file = open("Employees.txt", "r")
s1 = file.readlines()
file.close()

websites = s1

with open(host_path,"w+") as fileptr:
    content = fileptr.read()
    fileptr.writelines(s)
    for website in websites:
        if website in content:
            pass
        else:
            fileptr.write(redirect+"        "+website)