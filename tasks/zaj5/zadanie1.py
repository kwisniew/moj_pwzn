# -*- coding: utf-8 -*-

import operator
import numpy as np
from collections import defaultdict


def next_item(input):
    
    """
    Zwraca "następny" ngram dla podanego n-gramu. Działa to dla ciągów znaków ASCII.
    To jest hak, ale działa.

    Można zaimplementować to lepiej.
    :param input:
    :return:
    """
    return input[:-1] + chr(ord(input[-1])+1)


def load_data(path):
    #path="/home/kon/Documents/pwzn/dane/enwiki-20140903-pages-articles_part_1.xmlascii.bin"
    mytype = np.dtype([
        ("ngram", np.dtype('a7')),
        ("count", np.uint32)])
    data = np.memmap(path, dtype=mytype, mode='r')
    return data
    """
    Funkcja która ładuje dane z pliku zawierającego ngramy. Plik ten jest
    plikiem binarnym zaiweającym N wieszy w każdym wierszu jest 7 bajtów 
    zawierających 7-gram a następie czterobajtowa liczba całkowita zawierającą 
    ilość zlieczeń.

    Funkcja zwraca tablicę numpy. Tablica ja jest tylko do odczytu.

    Podpowiedźź: starczą dwie linikji kodu definicja dtype oraz otwarcie macierzy.
    Typ danych jest złożony --- należy użyć Structured Array.
    """


def suggester(input, data):

   # wynik = np.logical_equal(input,data[:,0])
    to_be_inserted = [input, next_item(input)]
    numb = np.searchsorted(data['ngram'], to_be_inserted)
    suma = np.sum(data["count"][numb[0]:numb[1]])
    lista = []

    for i in range(numb[0], numb[1]):
        lista.append( (chr(data["ngram"][i][-1]),data["count"][i]/int(suma)) )

    #lista = sorted(lista, key=operator.itemgetter(1), reverse=True )
    d = defaultdict(list)
    for k,v in lista:
        d[k].append(v)
    e = []
    for ii in d.items():
        #print(ii)
        e.append((ii[0], sum(ii[1])))
    e = sorted(e, key=operator.itemgetter(1), reverse=True )
    return e
    #next_item(input)
    """
    Funkcja która sugeruje następną literę ciągu ``input`` na podstawie n-gramów
    zawartych w ``data``.

    :param str input: Ciąg znaków o długości 6 znaków. **UWAGA** W zajęciach trzecich
                      input mógł mieć dowolną długość.
    :param np.ndarray data: Wynik działania ``load_data``.
    :return: Dowolną strukturę którą można zaindeksować w następującyc sposób:
            ret[0][0] zwraca najbardziej prawdopodobną nasßępną literę. ret[0][1]
            jej prawdopodobieństwo. ret[-1][0] zwraca najmniej prawdopodobną literę.
            Dane posortowane są względem prawodpodobieństwa.

    By wygenerować częstotliwości należy:

    Dla ustalenia uwagi zakładamy ze input zawiera ciąg znaków `foo`

    1. Znaleźć "następny" n-gram. Krótka funkcja "hak", która zwraca następny
       n-gram jest z
    2. Odnaleźć pierwsze i ostatnie wystąpienie ngramu rozpoczynającego się od wartości
       ``foo``.
    3. Wyznaczyć prawdopodobieństwo wystąpienia kolejnej litery, posortować i zwrócić.

    Przykład zastosowania:

    >>> data = load_data("path")
    >>> suggester('ąęćś', data)
    []
    >>> suggester('pytho', data)
    [('n', 1.0)]
    >>> suggester('pyth', data)
    [('o', 0.7794117647058824),
     ('a', 0.1323529411764706),
     ('e', 0.07352941176470588),
     ('i', 0.014705882352941176)]
    """
    
#suggester("aleksa", load_data("/opt/pwzn/zaj5/enwiki-20140903-pages-articles_part_0.xmlascii.bin"))   
#data=load_data("/home/kon/Documents/pwzn/dane/enwiki-20140903-pages-articles_part_1.xmlascii.bin")
#print(chr(data['ngram'][0][0]))
#print(data['count'][0]/100)
#print(next_item('pytho'))
#print(len(data))
#to_be_inserted = ['python', next_item('python')]
#numb = np.searchsorted(data['ngram'], to_be_inserted)
#suma = np.sum(data["count"][numb[0]:numb[1]])
#print(to_be_inserted)
#print(numb)
#print(suma)
#print(suggester('python', data))
