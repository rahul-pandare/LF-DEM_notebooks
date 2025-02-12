# importing libraries

import os
import matplotlib
import numpy             as     np
import pandas            as     pd
import scipy.optimize    as     opt
import matplotlib.pyplot as     plt
from   matplotlib        import font_manager
from   fractions         import Fraction
import pickle
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning, module='mkl')


'''
script to read and pickle data.
Here we read, concatenate and pickle the simulation data from data_*.dat file, F_rig and z_net

'''

# Reading directory:

TopDir      = "/media/rahul/Rahul_2TB/high_bidispersity/" #(samsung ssd)

pkldumpdir  ="/home/rahul/Dropbox (City College)/CUNY/Research/Bidisperse Project/analysis/" #home linux

NP          = [1000]

run         = {500:8,1000:4,2000:2,4000:1}

phi         = [0.75]

ar          = [1.0, 1.4, 1.8, 2.0, 4.0]

data_file = 'data_contact_1.pkl'

if os.path.exists(pkldumpdir+data_file):
    with open(pkldumpdir+data_file, 'rb') as file:
        datasets_dict = pickle.load(file)
    print(f"\nData loaded from existing '{data_file}' pickle file")

else:
    # files to read
    file_names = ['int_random_seed_params_stress100r_shear.dat']
    sum_variables = ['conct']
    
    # initializing the dictionary
    datasets=[]                    
    datasets_dict = {key: None for key in datasets}
    
    for i in range(len(NP)):
        for j in range(len(phi)):
            # redefining phi
            phir = '{:.3f}'.format(phi[j]) if len(str(phi[j]).split('.')[1])>2 else '{:.2f}'.format(phi[j])
            for k in range(len(ar)):
                dataname=TopDir+'NP_'+str(NP[i])+'/phi_'+phir+'/ar_'+str(ar[k])+'/Vr_0.5'
                if os.path.exists(dataname):
                    temp=[]
                    for l in range (run[NP[i]]):
                        for m, file_name in enumerate(file_names):
                            dat_run=0
                            with open(f'{dataname}/run_{l+1}/{file_name}', 'r') as file:
                                dat_run = np.loadtxt(file)
                                
                        temp.append(dat_run)
                    datasets_dict['NP_'+str(NP[i])+'_phi_'+phir+'_ar_'+str(ar[k])]=temp
                    
    with open(pkldumpdir+data_file, 'wb') as file:
        pickle.dump(datasets_dict, file)
    with open(pkldumpdir+data_file, 'rb') as file:
        datasets_dict = pickle.load(file)
    
    print("\nData read and loaded \n")
    
    
m='''
Data structure - 
datasets_dict contains the data of all parameters and all samples

datasets_dict: {'key1':[run1, run2, run3, run4], 'key2': [run1, run2, run3, run4],.....}

eg: 'key1': 'NP_1000_phi_0.70_ar_1.0'
    run1.shape = (5001 (samples),35 (parameters))

'''