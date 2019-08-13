#!/usr/bin/env python

import get_par

par_cha = 'frequency'

par_set = [par_cha+'_grid',par_cha+'_start',par_cha+'_end']
par_file = 'parameters.dat'

par_values = get_par.get_parameters(par_file,par_set)
resolution = (par_values[2]-par_values[1])/par_values[0]

f = open(par_file,'rw')           
for line in f:
    line.strip().split('\n')
    if par_cha in line:
        break
a = line.split(' ')
b = float(a[1])+resolution
newline = line.replace(a[1],str(b))
f.write(newline)
f.close()

