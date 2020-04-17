import os
from bs4 import BeautifulSoup as bs
import requests as req

os.system("g++ -o o1 prog1.cpp")
os.system("g++ -o o2 prog2.cpp")
cases=[]
problem_code="COINS"
sor=req.get("http://spojtoolkit.com/history/"+problem_code).text
#print(sor.status_code)
soup = bs(sor,'lxml').text


#check if problem code is found or not
check=False
tmp_1=soup
for i in tmp_1:
    if(i=='#'):
        check=True
        break
if(check==False):
    print("Problem Not Found . Please check problem code")
else:
    print("Spoj Problem "+problem_code+" Found")


#Extracting Test cases
temp_1=""
strt=False
for i in soup:
    #print(i)
    if(strt and i=='#'):
        #print("re1")
        strt=False
        cases.append(temp_1)
        temp_1=""
        continue
    if(strt):
        #print("re2")
        temp_1=temp_1+i
    if(i=='.'):
        #print("re3")
        strt=True
        continue
#if all the test cases to be checked irrespective of being correct
out=False

print("Test Cases Extracted")
#check start
for i in cases:
    #print(i)
    with open("input.txt","w") as f:
        f.seek(0)
        f.write(i)
    #print("Did this1")
    os.system("./o1 < input.txt > output.txt")
    ch1=""
    with open("output.txt","r") as f:
        ch1=f.read()
    #print("Did this1")
    os.system("./o2 < input.txt > output.txt")
    #print("First prb")
    ch2=""
    with open("output.txt","r") as f:
        ch2=f.read()
    #print("Did this1")
    if(ch1==ch2):
        print("Passed test case: ")
    else:
        print("Did not pass test case : ")
        print(i)
        if(out):
            exit()
#print("Successfuly passed every test case")
