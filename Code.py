import os
c=input('Enter Directory in the format "C:\Program Files (x86)\Common Files\"(without ""): \n')
d=input('Enter prefix: ')
e=input('Enter \n"1" for inbound \n"2" for outbound \n"3" for both \nWithout ""\n')
a=[];b=[]
for root, dirs, files in os.walk(c):
	for name in files:
		a=a+[[(os.path.join(root,name))]]
for i in range(len(a)):
	if a[i][0][-3:]=='exe':
		b=b+a[i]
print('Number of files: '+str(len(a))+'\nNumber of .exe files: '+str(len(b)))
f=input('Continue? [Y/N] ')
if f=='y' or f=='Y':
	for i in range (len(b)):
		name=d+str(i)
		if e=='1':
			os.popen('netsh advfirewall firewall add rule name="'+name+'" dir=in action=block program= "'+ b[i]+'" enable=yes profile=any')
		if e=='2':
			os.popen('netsh advfirewall firewall add rule name="'+name+'" dir=out action=block program= "'+ b[i]+'" enable=yes profile=any')
		if e=='3':
			os.popen('netsh advfirewall firewall add rule name="'+name+'" dir=in action=block program= "'+ b[i]+'" enable=yes profile=any')
			os.popen('netsh advfirewall firewall add rule name="'+name+'" dir=out action=block program= "'+ b[i]+'" enable=yes profile=any')
elif f=='N' or f=='n':
	pass
