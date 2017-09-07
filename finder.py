import requests
link=[]
domain=input("Enter the domain")
url="https://www.virustotal.com/en/domain/"+domain+"/information/"
r=requests.get(url)
t=r.text
f=open("D:\\file mer\\Github\\responses.txt","w",encoding="utf-8")
f.write(t)
f.close()
f=open("D:\\file mer\\Github\\response.txt","w",encoding="utf-8")
f.write(t)
f.write("ENDOFFILE")
f.close()
f=open("D:\\file mer\\Github\\response.txt",'r',encoding="utf-8")
a=""
n=0
for i in f:
           if i=="  <div class=\"enum \">\n":
                                            f.readline()
                                            a=f.readline()
                                            a.lstrip()
                                            if(a[-3:-1]=="om"):
                                                               print(a[6:-1])
                                                               link=link+[a[6:-1]]
                                                               n+=1
if input("Do you want to store the links y/n")=="y":
    path=input("Input the path where links are to be stored")
    #path.replace("\\","\\\\")
    f2=open(path,'w')
    for i in range(0,n):    
        f2.write(link[i])
        f2.write("\n")
    f2.close()
else:
    print("Finished")
'''
           
import webbrowser
url=""
n=0
f=open("D:\\file mer\Github\link.txt","r")
while f.readline()!='':
   n+=1
f.close()
f=open("D:\\file mer\Github\link.txt","r")
firefox_path="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(firefox_path),1)
line=0
while line<n:
   url=f.readline()
   print(url)
   line+=1
   webbrowser.get('firefox').open_new_tab(url)
f.close()
print("DONE")

'''                                                    

           
import requests
import re
def getcsrf(t):
	d=t[(t.find("csrf")+28):(t.find("csrf")+60)]
	return d
total=[]
def eliminate(l):
        if(l not in total):
                total.append(l)
                
url="https://dnsdumpster.com/"
dom=input("Enter the domain ")
r=requests.get(url)
t=r.text
#r=requests.post("https://dnsdumpster.com",data={'csrfmiddlewaretoken':getcsrf(t)})
tkn="csrftoken="+getcsrf(t)+";"
header = {"Referer":"https://dnsdumpster.com","Cookie" :tkn}
r=requests.post("https://dnsdumpster.com",data={'csrfmiddlewaretoken':getcsrf(t),'targetip':dom},headers=header)
#print(r.text)
'''
import urllib.request
import urllib.parse
values={'csrfmiddlewaretoken':getcsrf(t),'targetip':dom},headers=header)
'''
resp=r.text
sd=[]
l=re.findall((r'<tr><td class="col-md-4">(.*?).'+dom+'<br>'),resp)
for i in l:
        if(i!=''):
                v=i+'.'+dom
                eliminate(v)
for i in total:
        print(i,"\n")

