#!/bin/env python3
'''
TODO
1. implement subprocess for calling journalctl log
2. make it cron/automation freindly as possible
3. make it in the form of 
3. finish it by the end of this week (april 11th) <--- dumbass failed to meet the deadlines
'''
import subprocess 
import re
import os
import json
home = os.path.expanduser("~")
path = f"{home}/journal_cursor.loc"
journ=subprocess.Popen(["journalctl",f"--cursor-file={path}","-p","3"],stdout=subprocess.PIPE, text=True)
# jrnl = []
# jrnl.append(l.stdout)
# zfile=open("sample_journal.log")
counter = 0
emit = []
T1=None
T2=""
T11=None
T22=""
lisp = {"mysql", "ACPI","Mysql"}
ditc=dict()
filed=dict()
for file in  journ.stdout:
    file=file.strip(" ")
    if "error" in file:
        k=(re.findall(r"\d{2}:\d{2}:\d{2}", file))
        for j in lisp:
            if j in file:
                for i in k:
                    if T1 == None:
                        T1 = i
                    T2 = i
                print((f"{k}\n {re.findall(r": (.+error.+)", file)}"))
                service=re.findall(j, file)
                ditc[j] = ditc.get(j, 0)+1
    elif "Failed" in file: 
        k=(re.findall(r"\d{2}:\d{2}:\d{2}", file))
        for j in lisp:
            if j in file:
                for i in k:
                    if T11 == None:
                        T11= i
                    T22 = i
                print((f"{k}\n {re.findall(r": (.+Failed.+)", file)}"))
                service=re.findall(j, file)
                filed[j] = filed.get(j, 0)+1
print(ditc)
print(filed)
t=(    
    f'''''
        report
    {T1}-{T2}
    Error in service:{ditc}
    {T11}-{T22}
    Failed Service:{filed}

    '''''
)
with open("/home/wowimoe/Documents/sys_report_dummy/repport.txt", "w") as file:
    file.write(t)
    file.close()
journ.terminate()
journ.wait()
