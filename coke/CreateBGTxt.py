# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:18:19 2018

@author: rithanya
"""

import os

def create_pos_n_neg():
    for file_type in ['Train']:
        
        for img in os.listdir(file_type):

            if file_type == 'Train':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.data','a') as f:
                    f.write(line)
            elif file_type == 'Neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)