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
    
    print(len(animal_list))
    animal_list.sort(key=itemgetter('genus', 'name'))
    print(len(animal_list))
    genus = animal_list[0]['genus']
    for ii in animal_list:       
        if genus==ii['genus']:
            if ii['sex']=='male':
                if m==None:
                    m=ii
                elif m['mass'] > ii['mass']:
                    m=ii
            elif ii['sex']=='female':
                if f==None:
                    f=ii
                elif f['mass'] > ii['mass']:
                    f=ii
        else:           
            noe.append(f)
            noe.append(m)
            genus=ii['genus']
            if ii['sex']=='male':
                m=ii
                f=None
            else:
                m=None
                f=ii
    noe.append(f)
    noe.append(m)
                
             
    print(len(noe))   
    return noe
    #print(noe)
    #noe.sort(key=itemgetter('genus', 'name'))
    #for i in noe[0:100]:
    #    print(i)
    
    """
    

    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """

#if __name__ == "__main__":
animals = load_animals()
filter_animals(animals)