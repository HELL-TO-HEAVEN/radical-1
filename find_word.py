import re
from pypinyin import pinyin, load_phrases_dict
from add_new_word_dict import new_word_pinyin_dict, new_word_split_dict
import os
from sklearn.externals import joblib
import jieba
import jieba.posseg as pseg
jieba.load_userdict(['左 f', '口 n', '日 n','月 n', '年 n','一起 s','米 n'])
jieba.suggest_freq(('八', '下'), True)  # 八下
jieba.suggest_freq(('一个','包'), True)
load_phrases_dict(new_word_pinyin_dict)


dictionary_path = os.path.split(os.path.realpath(__file__))[0] + '\\dict\\'
word_component_dict, word_radical_dict, zi_radical_dict = joblib.load(dictionary_path+'chaizi_dict')

word_component_dict.update(new_word_split_dict)


def find_num(input):
    result = re.findall('[一二两俩三四五六]|[0-9]',input)
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


def get_word(input_sentence):
    remove_str_list = [' ','“','”','，','？','这个','应该','究竟']
    for i in remove_str_list:
        input_sentence = input_sentence.replace(i, '')
    new_sentence = input_sentence

    new_sentence = re.sub(r'加起来|拼起来|摞起来|合一起|合在一起',' ', new_sentence)

    # top rules
    complete_str_top = ''
    match_word = re.findall('|'.join(list(word_radical_dict.keys())), new_sentence)
    if len(match_word):
        for word in match_word:
            complete_str_top += word_radical_dict.get(word)
            new_sentence = new_sentence.replace(word, ' ')

    complete_str_top_zi = ''
    match_word_zi = re.findall('|'.join(list(zi_radical_dict.keys())), new_sentence)
    if len(match_word_zi):
        for word in match_word_zi:
            complete_str_top_zi += zi_radical_dict.get(word)
            new_sentence = new_sentence.replace(word, ' ')

    word_list = list(pseg.cut(new_sentence, HMM=False))
    words = [i.word for i in word_list]
    flags = [i.flag for i in word_list]

    special_case1 = ['是', '为']
    need_pop_index = []
    for i in special_case1:
        shi_ = [index for index, value in enumerate(words) if value == i]
        if len(shi_):
            for each_ in shi_:
                if flags[each_-1] in ['n','f']:
                    need_pop_index.append(each_)
    if len(need_pop_index):
        words = [v for i,v in enumerate(words) if i not in need_pop_index]
        flags = [v for i,v in enumerate(flags) if i not in need_pop_index]

    special_case2 = '字'
    zi_ = [i for i, value in enumerate(words) if value in special_case2]
    if len(zi_):
        zi_index = words.index(special_case2)
        if flags[zi_index-1] not in ['f','c']:
            words.pop(zi_index)
            flags.pop(zi_index)

    word_number = len(words)
    special_case3 = '加'
    jia_index = [index for index,word in enumerate(words) if word == special_case3]
    if len(jia_index):
        count_ = 0
        for index, jia_ in enumerate(jia_index):
            if jia_+1 < word_number and words[jia_+1] not in [' ','一起','起来']:
                new_index = jia_+1 + count_
                if flags[new_index] not in ['m','r']:
                    count_ += 1
                    words = words[:new_index] + ['一个'] + words[new_index:]
                    flags = flags[:new_index] + ['m'] + flags[new_index:]

        if words[words.index(special_case3)-1] not in [' '] and words[words.index(special_case3)+1] not in ['一起','起来'] and flags[words.index(special_case3)-1] not in ['f']:
            index_jia = words.index(special_case3)-1
            words = words[:index_jia] + ['一个'] + words[index_jia:]
            flags = flags[:index_jia] + ['m'] + flags[index_jia:]


    empty_index = [i for i,value in enumerate(words) if value in [' ']]
    if len(empty_index):
        coun_t = 0
        for i in empty_index:
            if flags[i-1-coun_t] in ['m','f']:
                words.pop(i-1-coun_t)
                flags.pop(i-1-coun_t)
                coun_t += 1

    print('words: {x}'.format(x=words))
    print('flags: {x}'.format(x=flags))

    # using the rules of pos
    complete_str_f = ''
    complete_str_uj = ''
    complete_str_q = ''
    complete_str_c = ''


    if 'f' in flags:
        f_index = [i for i, v in enumerate(flags) if v == 'f']
        if len(f_index) > 1:
            complete_str_f = ''
            for f_each in f_index:
                if flags[f_each + 1] not in ['q']:
                    # For sentence contain the pos of 'f' and 'q'/'m', use rule three.
                    if flags[f_each + 1]=='m' and len(words[f_each + 1])==2:
                        pass
                    else:
                        # rule one: f + . f + .
                        complete_str_f += words[f_each + 1][0]
        else:
            if flags[f_index[0]+1] not in ['q','m'] and flags[f_index[0]+2] not in ['q','m']:
            # rule two: f + n  number of f decide the number of '.'
                index_ = flags.index('f')
                complete_str_f = ''.join(words[index_+2:])[:len(words[index_])]

    # rule three: q + . /m + . multiple
    if 'q' in flags or 'm' in flags:
        if 'q' not in flags:
            str_q = ''
            m_word = words[flags.index('m')]
            if len(m_word) == 2:
                for index, i in enumerate(flags):
                    if i == 'm':
                        nex_word = words[index + 1][0]
                        numbers_ = find_num(words[index])
                        try:
                            numbers_ = int(numbers_[0])
                        except:
                            numbers_ = number_dict.get(numbers_[0])
                        str_q += nex_word * numbers_

        else:
            str_q = ''
            for index, i in enumerate(flags):
                if i == 'q' and words[flags.index('q')+1] != ' ':
                    nex_word = words[index + 1][0]
                    if flags[index - 1] == 'm':
                        number_ = find_num(words[index - 1])
                        try:
                            number = int(number_[0])
                        except:
                            number = number_dict.get(number_[0])
                        str_q += nex_word * number
                    else:
                        str_q += nex_word * 1

        complete_str_q = str_q

    if 'uj' in flags:
        # rule five:  uj + . + r + v/. + uj + n/v
        index_ = flags.index('uj')
        flags_number = len(flags)
        if index_+3 < flags_number:
            if flags[index_+2] == 'r' and flags[index_+3] == 'v':
                complete_str_uj = words[index_+1]
        elif flags[index_+1] in ['n','v']:
            complete_str_uj = ''.join(words[:index_])

    if 'c' in flags and words[flags.index('c')] not in ['并','或']:
        c_index = flags.index('c')
        if words[c_index-1] != ' ':
            if flags[c_index-1] != 'p' or flags[c_index+1] != 'm':
                complete_str_c = ''.join(list(re.findall('(.?)和(.?)',new_sentence)[0]))

    print('complete_str_top: {a} \ncomplete_str_top_zi: {b} \ncomplete_str_f: {x} \ncomplete_str_q: {y} \ncomplete_str_uj: {z} \ncomplete_str_c: {e}'.format(a=complete_str_top,b=complete_str_top_zi, x=complete_str_f,y=complete_str_q, z=complete_str_uj, e=complete_str_c))
    complete_str_list = [i for i in [complete_str_top, complete_str_top_zi, complete_str_f, complete_str_q, complete_str_uj, complete_str_c] if len(i)]
    complete_str_ = ''.join(complete_str_list)

    if not complete_str_:
        # rule six:  . + r(multi) + v
        if 'r' in flags:
            flags_number = len(flags)
            index_ = flags.index('r')
            if index_+1 < flags_number:
                if flags[index_+1] == 'v':
                    complete_str_ = ''.join(words[:index_])

            if flags[index_-1] == 'v':
                complete_str_ = ''.join(words[:index_-1])
    return complete_str_.replace(' ','')


def get_pinyin(input_sentence):
    try:
        input_complete_word = get_word(input_sentence)
    except:
        return "Sorry, I don't know!"

    if len(input_complete_word) > 1:
        out_word = word_component_dict.get(input_complete_word)  # 拆字 - 单字
        if out_word:
            out_pinyin = pinyin(out_word)[0][0]
            if out_pinyin != out_word:
                output = out_word + ': ' + out_pinyin
            else:
                return 'I don\'t know how to pronounce the word!'
        else:
            out_cz_pinyin = pinyin(input_complete_word)  # 词组
            out_cz_pinyin = ' '.join([le for br in out_cz_pinyin for le in br])
            if out_cz_pinyin.replace(' ','') != input_complete_word:
                output = input_complete_word + ': ' + out_cz_pinyin
            else:
                return 'I don\'t know how to pronounce the word!'
    else:
        out_pinyin = pinyin(input_complete_word)[0][0]  # 单字
        if out_pinyin != input_complete_word:
            output = input_complete_word + ': ' + out_pinyin
        else:
            return 'I don\'t know how to pronounce the word!'

    return output

