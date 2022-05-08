import requests
from bs4 import BeautifulSoup
r=requests.get("http://ips.chacuo.net/view/s_SX")
soup=BeautifulSoup(r.text,"lxml")
count=0
for line in soup.select(".list dd span"):
    if(count==0):
        link=line.get_text()
        count=1
        continue
    if(count==1):
        with open("./ip.txt","a+") as f:
            f.write(link+"-"+line.get_text()+"\n")
            f.close()
        count=0
file_ip=open('./ip.txt','r')
while True:
    ip=file_ip.readline()
    if not ip:
            break
    ip_1,*ip_2=ip.split(".")
    if(ip_2[0]!=ip_2[3]):
        ip_yanma="16"
        max_ip_number=ip_2[3]
        update_number=ip_2[0]
        while(int(ip_2[0])!= int(max_ip_number)+1):
            with open('./firewall.sh', 'a+') as f:
                f.write('firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="'+str(ip_1)+"."+str(ip_2[0])+"."+str(ip_2[1])+"."+"0"+"/"+str(ip_yanma)+'" port protocol="tcp" port="1723" accept"\n')
                f.close()
            ip_2[0]=int(ip_2[0])+1
    elif(ip_2[1]!=ip_2[4]):
        ip_yanma="24"
        max_ip_number=ip_2[4]
        update_number=ip_2[1]
        while(int(ip_2[1])!= int(max_ip_number)+1):
            with open('./firewall.sh', 'a+') as f:
                f.write('firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="'+str(ip_1)+"."+str(ip_2[0])+"."+str(ip_2[1])+"."+"0"+"/"+str(ip_yanma)+'" port protocol="tcp" port="1723" accept"\n')
                f.close()
            ip_2[1]=int(ip_2[1])+1
file_ip.close()
