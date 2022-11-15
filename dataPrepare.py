# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:44:29 2022

@author: Rudra
"""

import shutil
import os
import pandas as pd
import glob
import json

data_folder = 'test_data_all/'
'''
for i in range(0,10):
    src_dir_n = '0'+str(i)
    src_dir = 'test_data/'+src_dir_n

    if(os.path.exists(src_dir)):
        files = os.listdir(src_dir)
   
        for fname in files:
            shutil.copy2(os.path.join(src_dir,fname), data_folder)
        
    

for i in range(10,100):
    src_dir_n = str(i)
    src_dir = 'test_data/'+src_dir_n

    if(os.path.exists(src_dir)):
        files = os.listdir(src_dir)
   
        for fname in files:
            shutil.copy2(os.path.join(src_dir,fname), data_folder)
    
    
for f in glob.glob(data_folder+'*.html'):
    os.remove(f)
'''
######################################################################
'''
df = pd.read_csv('final_eval_data.csv')
df_1 = df[['url1_lang', 'url2_lang', 'pair_id', 'OVERALL']]
#df_1 = df[['url1_lang', 'url2_lang', 'pair_id', 'Overall',
#           'Geography', 'Entities', 'Time', 'Narrative', 'Style', 'Tone']]

f_list = []
for f in glob.glob(data_folder+'*.json'):
    f_list.append(f.split('\\')[1].split('.')[0])

#count = 0 #4773 not found in test
list_of_dict = []
for ind in df_1.index:
    i = df_1['pair_id'][ind]
    f_1 = i.split('_')[0]
    f_2 = i.split('_')[1]
    
    
    #if(not((f_1 in f_list) and (f_2 in f_list))):
    #    count+=1
    
    
    if((f_1 in f_list) and (f_2 in f_list)):
        file_1 = json.load(open(data_folder+f_1+ '.json', 'r'))
        file_2 = json.load(open(data_folder+f_2+ '.json', 'r'))
        pair_dict = {}
        pair_dict['pair_id'] = i
        pair_dict['title_1'] = file_1['title']
        pair_dict['title_2'] = file_2['title']
        pair_dict['text_1'] = file_1['text']
        pair_dict['text_2'] = file_2['text']
        pair_dict['tags_1'] = file_1['tags']
        pair_dict['tags_2'] = file_2['tags']
        pair_dict['meta_lang_1'] = file_1['meta_lang']
        pair_dict['meta_lang_2'] = file_2['meta_lang']
        pair_dict['meta_description_1'] = file_1['meta_description']
        pair_dict['meta_description_2'] = file_2['meta_description']
        
        pair_dict['score'] = df_1['OVERALL'][ind]
        
        pair_dict['score_1'] = df_1['Geography'][ind]
        pair_dict['score_2'] = df_1['Entities'][ind]
        pair_dict['score_3'] = df_1['Time'][ind]
        pair_dict['score_4'] = df_1['Narrative'][ind]
        pair_dict['score_5'] = df_1['Style'][ind]
        pair_dict['score_6'] = df_1['Tone'][ind]
        
        list_of_dict.append(pair_dict)
    

json.dump(list_of_dict, open('test_data_meta.json','w'))
'''
file_1 = json.load(open('test_data_meta.json', 'r'))