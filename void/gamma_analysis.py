#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:33:02 2023

@author: rahul
"""

import os
import matplotlib
import numpy             as     np
import pandas            as     pd
import scipy.optimize    as     opt
import matplotlib.pyplot as     plt
from   fractions         import Fraction


#%% INITIALIZING

plt.close('all')

sigma       = 100

#TopDir      = "/Volumes/Extreme SSD/high_bidispersity"
TopDir      = "/Users/rahul/sshfs/high_bidispersity"


#etaS_maxFit = 5000

#symbols     = np.array(['v', '^', '>', '<', 's', 'o', '*', 'p'])

NP          = np.array([500, 1000])

phi         = np.array([0.74])

ar          = np.array([1.0, 1.4, 1.8, 2.0, 4.0])
    
run         = {NP[0]:8,NP[1]:4}#,NP[2]:2,NP[3]:1}
    
data = {};data1={}
npl=[];phil=[];arl=[];runl=[];
params=[];
time=[];
ll=0;
print('')
print('Reading data')

for i in range(len(NP)):
        for j in range(len(phi)):
            for k in range(len(ar)):          
                for l in range (run[NP[i]]):
                    with open(TopDir+'/NP_'+str(NP[i])+'/phi_'+"{:.2f}".format(phi[j])+'/ar_'+str(ar[k])+'/Vr_0.5/run_'+str(l+1)+'/data_random_seed_params_stress100r_shear.dat','r') as file:
                        lines=file.readlines()
                        b=lines[-1].strip()
                        params.append('/NP_'+str(NP[i])+'/phi_'+"{:.2f}".format(phi[j])+'/ar_'+str(ar[k])+'/Vr_0.5/run_'+str(l+1)+' ')
                        time.append(float(b.split()[1]))
                        #print('/NP_'+str(NP[i])+'/phi_'+"{:.2f}".format(phi[j])+'/ar_'+str(ar[k])+'/Vr_0.5/run_'+str(l+1)+' - '+b.split()[1])
                        data={'Params':params,'Time':time}
                        npl.append(NP[i]); phil.append(float("{:.2f}".format(phi[j]))); arl.append(ar[k]); runl.append(l+1);
                        #print(pd.DataFrame(data))
data1={'NP':npl,'Phi':phil,'ar':arl,'#run':runl,'Time':time}             
pd.DataFrame(data1)
                        
#pd.DataFrame(data).to_csv('output.txt',index=False)


#Np=500
k=phil[0:npl.count(500)].count(.74);
#fig, axs = plt.subplots(2, 2, figsize=(8, 8))
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

for i in range(run[NP[0]]):
    axs[0].plot(arl[i:k:run[NP[0]]],time[i:k:run[NP[0]]],'-*'); axs[0].set_title('Phi='+str(phi[0]));axs[0].set_xticks(list(ar));
    axs[0].set_title('NP=500')
    axs[0].legend(['run1', 'run2', 'run3', 'run4','run5','run6','run7','run8'], loc='lower right',bbox_to_anchor=(.9, .3),ncol=2)


#Np=1000
off=npl.count(500)
k=phil[off:off+npl.count(1000)].count(.74);
ncol=1;nrow=1;

for i in range(run[NP[1]]):
    axs[1].plot(arl[off+i:off+k:run[NP[1]]],time[off+i:off+k:run[NP[1]]],'-*'); axs[1].set_title('Phi='+str(phi[0]));axs[1].set_xticks(list(ar))
    axs[1].set_title('NP=1000')

fig.legend(['run1', 'run2', 'run3', 'run4'], loc='upper right',bbox_to_anchor=(.95, .7),ncol=1)
fig.text(0.5, -0.02, 'ar', ha='center', fontsize=14, weight='bold')
fig.text(-0.02, 0.5, 'gamma', va='center', fontsize=14, weight='bold', rotation='vertical')

plt.tight_layout()
#plt.savefig('NP1000_gamma.jpeg',dpi=500,bbox_inches='tight')
plt.show()