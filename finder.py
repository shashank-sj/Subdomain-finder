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
