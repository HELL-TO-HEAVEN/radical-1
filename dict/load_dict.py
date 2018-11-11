import re
import pandas as pd
import os
dictionary_path = os.path.split(os.path.realpath(__file__))[0] + '\\'


def update_dict():
    with open(dictionary_path + 'chaizi-jt.txt', encoding='utf-8') as fi:
        jt_word = fi.readlines()
    with open(dictionary_path + 'chaizi-ft.txt', encoding='utf-8') as fi:
        ft_word = fi.readlines()
    all_word = jt_word + ft_word

    word_dict = {}
    # key is character of word, value is word
    for word in all_word:
        new_word = word.strip().split('\t')
        values_ = new_word[0]
        new_word.remove(new_word[0])
        for i in range(len(new_word)):
            word_dict[new_word[i].replace(' ','')] = values_
    return word_dict


word_component_dict = update_dict()


def get_word_radical():
    radical = pd.read_table(dictionary_path+'100-most-common-radicals.txt',usecols=[0,1,2,7],header=None)
    word_radical_dict = {}
    for index, row in radical.iterrows():
        if row[0]==row[1]:
            pianpang = [row[0]]
        else:
            pianpang = [row[0],row[1]]
        if row[2]:
            pianpang.append(row[2])

        if '（' not in row[7]:
            word_radical_dict[row[7]] = pianpang[0]
        else:
            words_ = row[7].split('，')
            for word in words_:
                word_c_l = re.findall('([^，].*)（(.*)）',word)[0]
                word_radical_dict[word_c_l[0]] = word_c_l[1]

    zi_radical_dict = {key[:2]:value for key,value in word_radical_dict.items() if len(key) > 1 and key[1]=='字'}
    return word_radical_dict, zi_radical_dict


word_radical_dict, zi_radical_dict = get_word_radical()


from sklearn.externals import joblib
joblib.dump([word_component_dict, word_radical_dict, zi_radical_dict], dictionary_path + 'chaizi_dict')