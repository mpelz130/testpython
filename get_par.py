#!/usr/bin/env python

#def get_parameters(par_file,par_list):
par_file = 'parameters.dat'
par_list = ['frequency:','offset:']

length = len(par_list)
par_value = []

f = open(par_file,'r')           
for n in range(length):
    par = par_list[n]
    for line in f:
        line = line.strip().split('\n')
        if par in line:
            break
            a = line.split(' ')
            par_value.append(float(a[1]))
            line = f.seek(0)
            print('asasa')
f.close()
 #   return par_value

