"""
This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2024//
Ending 2024//

"""

import os
import sys
import inspect
from termcolor import cprint
from collections import Counter
from glob import glob
from pymystem3 import Mystem
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    PER,
    NamesExtractor,
    Doc,
)


# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])

# Shows which module is currently running
# cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
# ' << '+'='*20, 'red', attrs=['bold'])


NAME_PROJECT = "****** Your project name "
cprint(os.getcwd(), "green")
path_prj = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + "/"
cprint(path_prj, "blue")
sys.path.append(path_prj)


def get_dir(NAME_START: str) -> list:
    """AI is creating summary for prog1"""
    print()
    cprint(
        "=" * 20 + " >> " + inspect.stack()[0][0].f_code.co_name + " << " + "=" * 20,
        "red",
        attrs=["bold"],
    )
    print()
    dd = [f.path for f in os.scandir(NAME_START) if f.is_dir()]
    return dd


def prog2():
    """AI is creating summary for prog2"""
    print()
    cprint(
        "=" * 20 + " >> " + inspect.stack()[0][0].f_code.co_name + " << " + "=" * 20,
        "red",
        attrs=["bold"],
    )
    print()





def get_array_text(sum_arr: dict, key: str, nf: str, m):

    with open(nf, "r") as i_f:
        all_text = i_f.read().strip().replace("\n", " ").lower().split()
    for word in all_text:
        # print(word)
        lemmas = m.lemmatize(word)
        # doc = Doc(word)
        # print(doc.tokens)
        # print(doc.sents)
        # print(lemmas)
        # print()
        sum_arr[key][lemmas[0]] += 1
        # break
    # print(sum_arr)


if __name__ == "__main__":
    NAME_START_POINT = "/home/al/Projects_My/hakaton_ozon_opg/dataset/"
    list_dir = get_dir(NAME_START_POINT)
    # print(list_dir)
    array_txt: dict = {}
    m = Mystem()
    for sd in list_dir:
        key_one = sd.split("/")[-1]
        # print(key_one)
        array_txt[key_one] = Counter()
        list_dir_two = get_dir(sd)
        for dt in list_dir_two:
            list_text = glob(dt + "/*.txt")
            # print(list_text)
            # print()
            for nf in list_text:
                get_array_text(array_txt, key_one, nf, m)
                # break
            # break
        # break
    for key in array_txt:
        print()
        print(key)
        print(array_txt[key])
        print()
from sklearn.datasets import __name__

dd = load_iris()
# prog2()
