#!/usr/bin/env python

import get_par
import numpy as num

par_list = ['amplitude','frequency','offset','grid','start','end']
par_file = 'parameters.dat'

par_values = get_par.get_parameters(par_file,par_list)
resolution = (par_values[5]-par_values[4])/par_values[3]

osc_file = 'osc_data.dat'
of = open(osc_file,'w+')

for i in range(int(par_values[3])):
    x = par_values[4]+i*resolution
    f = par_values[0]*num.sin(par_values[1]*x+par_values[2])
    of.write('%f %f\n' % (x,f))

of.close()

