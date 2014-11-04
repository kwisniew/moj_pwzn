# -*- coding: utf-8 -*-

import pickle
import pathlib
import operator
from operator import itemgetter


def load_animals(large_dataset=False):

    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def filter_animals(animal_list):
    
    m=None
    f=None
    genus = None
    noe = []
    animal_list_tmp = []
    mass_list = []
    

            
    animal_list.sort(key=itemgetter('genus'))
    
    for idx, d in enumerate(animal_list): 
        mass, unit = d['mass']
        if unit == 'kg':
            mass_list.append(mass*1000)
        if unit == 'g':
            mass_list.append(mass/1000)
        if unit == 'mg':
            mass_list.append(mass/1000000)
        if unit == 'Mg':
            mass_list.append(mass*1000)    

    
    f_idx=None
    m_idx=None
    genus = animal_list[0]['genus']
    for idx, ii in enumerate(animal_list):       
        if genus==ii['genus']:
            if ii['sex']=='male':
                if m==None:
                    m=ii
                    m_idx=idx   
                elif mass_list[idx]<mass_list[m_idx]:
                    m=ii
                    m_idx=idx
            elif ii['sex']=='female':
                if f==None:
                    f=ii
                    f_idx=idx
                elif mass_list[idx]<mass_list[f_idx]:
                    f=ii
                    f_idx=idx
        else:
            noe.append(m)
            noe.append(f)
            genus=ii['genus']
            if ii['sex']=='male':
                m=ii
                m_idx=idx
                f=None
            else:
                m=None
                f=ii
                f_idx=idx
    noe.append(f)
    noe.append(m)
                
             
    noe.sort(key=itemgetter('genus', 'name'))
    return noe

animals = load_animals(True)
filter_animals(animals)