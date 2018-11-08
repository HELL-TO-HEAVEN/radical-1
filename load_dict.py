import re
from pypinyin import load_phrases_dict
import pandas as pd
dictionary_path = 'D:\\my_github\\chaizi\\'


# Add new word!!!
new_word_split_dict = {'八白': '㒶',
                       '口口口口':'㗊',
                        '水水水水':'㵘',
                        '土土土土':'㙓',
                       '又又又又支':'敠'}
new_word_pinyin_dict = {'㒶': [['gōng']],
                        '敠': [['duō'], ['què']]}


def update_dict(split, pinyin):
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

    word_dict.update(split)
    load_phrases_dict(pinyin)
    return word_dict


word_component_dict = update_dict(new_word_split_dict, new_word_pinyin_dict)


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
    return word_radical_dict


word_radical_dict = get_word_radical()


def find_num(input):
    result = re.findall('[一二三四五六]|[0-9]',input)
    return result


number_dict = {
    '一':1,
    '二':2,
    '两':2,
    '俩':2,
    '三':3,
    '四':4,
    '五':5,
    '六':6
}




