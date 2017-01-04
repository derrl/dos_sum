#!/usr/bin/python

#This script can sum many ion's special orbit density of states, you can specify the 's,p,d' orbit to calculate.
#Numpy is needed in this script!
#Dec.21.2016--writen by HZ.Liu lhzsdu@gmail.com

import os
import string
import numpy as np

ion_number=raw_input('Please input the ion number(e.g.1 2-5):')


list1=string.split(ion_number,'-')
list2=[]
list3=[]
list4=[]

# Interpolate in list2
if len(list1)>1:
    for i in range(len(list1)-1):
        diff1=int(string.split(list1[i])[-1])-int(string.split(list1[i+1])[0])
        if diff1<0:
            for j in range(-diff1-1):
                list2.append(str(int(string.split(list1[i])[-1])+1+j))
        else:
            for j in range(diff1-1):
                list2.append(str(int(string.split(list1[i])[-1])-1-j))
# Split and sort in list3
for i in range(len(list1)):
    list3.extend(string.split(list1[i]))
list1=list3
list1.extend(list2)
for i in range(len(list1)):
    list1.insert(0,int(list1.pop()))
list1.sort()
# Incorporate atom numbers
list4.extend(list1)
# Exclude the repeated numbers
for i in range(len(list1)-1):
    if list1[i]==list1[i+1]:
            list4.remove(list1[i])

i_num=map(str,list4)

ion_orbit=raw_input('Please input the orbit for calculation(s,p,d):')
if (ion_orbit != 's')and(ion_orbit != 'p')and(ion_orbit != 'd'):
	exit()
else:
	pass

i_all = i_num[:]
for ion in i_num: 
	if ion_orbit == 's':	
		try:
		    dos = open("DOS"+ion, 'r')
		except:
		    print '\nfail to open DOS'+ion+'!\n'
		    i_all.remove(ion)
		else:
		    out_s=open('dos'+ion+'.s','w')
		    for line in dos: 
		        nums = line.split()
			s = float(nums[1])
			print >>out_s,s
		    out_s.close()
		finally:
		    dos.close()
		    
	elif ion_orbit == 'p':	
		try:
		    dos = open("DOS"+ion, 'r')
		except:
		    print '\nfail to open DOS'+ion+'!\n'
		    i_all.remove(ion)
		else:
		    out_p=open('dos'+ion+'.p','w')
		    for line in dos: 
		        nums = line.split()
			p = float(nums[2])+float(nums[3])+float(nums[4])
			print >>out_p,p
		    out_p.close()
		finally:
		    dos.close()
	
	else:	
		try:
		    dos = open("DOS"+ion, 'r')
		except:
		    print '\nfail to open DOS'+ion+'!\n'
		    i_all.remove(ion)
		else:
		    out_d=open('dos'+ion+'.d','w')
		    for line in dos: 
		        nums = line.split()
			d = float(nums[5])+float(nums[6])+float(nums[7])+float(nums[8])+float(nums[9])
			print >>out_d,d
		    out_d.close()
		finally:
		    dos.close()
	

count = -1
for count, line_n in enumerate(open('dos'+i_all[0]+'.'+ion_orbit, 'rU')):
    pass
count += 1

b = np.zeros(count,float)
for ion in i_all:
        a = np.loadtxt('dos'+ion+'.'+ion_orbit,delimiter='\n')
        np.add(a,b,b)

out=open(ion_orbit+'_dos_sum','w')
print >>out,i_all
for i in b:
        print >>out,i
out.close()

for ion in i_all:
	filename = 'dos'+ion+'.'+ion_orbit
	if os.path.exists(filename):
		os.remove(filename)
