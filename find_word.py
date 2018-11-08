import re
from pypinyin import pinyin
from load_dict import word_component_dict, find_num, number_dict, word_radical_dict


# 中文构字法
# 前后上下左右

# rule:
# 量词/数词/方位词 + 单字 (该单字为偏旁部首)
# 数词 = 数词+量词

# notes:
# 1.若方位词组词，则规则失效
# 示例：
# '上海下士念什么'
# 2.无法区分拆字/词组
# 3.无法保证拆字组成的顺序


# test
import jieba
import jieba.posseg as pseg
jieba.load_userdict(['左 f'])
jieba.suggest_freq(('八', '下'), True)  # 八下
jieba.suggest_freq(('一个','包'), True)

# sentence = '左边是人，右边是人'  rule one
# sentence = '上八下白怎么读？'   rule one

# sentence = '上下结构八白怎么读'  rule two

# sentence = '三个人怎么读？'  rule three
# sentence = '左边一个人 右边一个人'  rule three

# sentence = '右边是个草字'
# sentence = '右边是草字'

# sentence = '草字头 穴字头 宝盖头 提手旁 提字旁 走之底 之字底 ...' top rule


# Baidu Normal test:
# sentence = '草字头加内'
# sentence = '草字头下面加内念什么'
# sentence = '草字头加口再加内读什么'
# sentence = '一个走之底加一个加怎么读'
# sentence = '女和为加一起念什么?'
# sentence = '牛和字拼起来怎么读'
# sentence = '女和为念什么'
# sentence = '草与和念什么'
# sentence = '一个女字旁和一个为念什么?'

# sentence = '前面一个包，后面是为'
# sentence = '上面是老，下面一个美'

# sentence = '㵘的拼音'  rule five
# sentence = '又双叒叕的叕怎么读？'  rule five

# sentence = '㵘怎么读'  rule six


# word_list = list(pseg.cut(sentence, HMM=False))
# print(word_list)


def get_word(input_sentence):
    remove_str_list = [' ','“','”','，','？','这个','应该','究竟']
    for i in remove_str_list:
        input_sentence = input_sentence.replace(i, '')
    new_sentence = input_sentence

    # top rules
    match_word = re.findall('|'.join(list(word_radical_dict.keys())), new_sentence)
    if len(match_word):
        complete_str_ = ''
        for word in match_word:
            complete_str_ += word_radical_dict.get(word)
            new_sentence = new_sentence.replace(word, ' ')

    word_list = list(pseg.cut(new_sentence, HMM=False))
    words = [i.word for i in word_list]
    flags = [i.flag for i in word_list]
    empty_ = [i for i,value in enumerate(words) if value in [' ']]
    if len(empty_):
        words.pop(empty_[0])
        flags.pop(empty_[0])

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
        for jia_ in jia_index:
            if jia_+1 < word_number:
                if flags[jia_+1] not in ['m','r']:
                    words = words[:jia_+1] + ['一个'] + words[jia_+1:]
                    flags = flags[:jia_+1] + ['m'] + flags[jia_+1:]

    print(words)
    print(flags)

    # using the rules of pos

    if 'f' in flags:
        f_index = [i for i, v in enumerate(flags) if v == 'f']
        if len(f_index) > 1:
            complete_str_ = ''
            for f_each in f_index:
                if flags[f_each + 1] not in ['q', 'm']:
                # For sentence contain the pos of 'f' and 'q'/'m', use rule three.
                    # rule one: f + . f + .
                    complete_str_ += words[f_each + 1][0]
        else:
            if flags[f_index[0]+1] not in ['q','m']:
            # rule two: f + n  number of f decide the number of '.'
                index_ = flags.index('f')
                complete_str_ = ''.join(words[index_+2:])[:len(words[index_])]

    # rule three: q + .  multiple
    if 'q' in flags or 'm' in flags:
        if 'q' not in flags:
            str_dict = {}
            m_word = words[flags.index('m')]
            if len(m_word) == 2 and m_word not in ['一起']:
                for index, i in enumerate(flags):
                    if i == 'm':
                        nex_word = words[index + 1][0]
                        numbers_ = find_num(words[index])
                        try:
                            numbers_ = int(numbers_[0])
                        except:
                            numbers_ = number_dict.get(numbers_[0])
                        str_dict[nex_word] = numbers_

        else:
            str_dict = {}
            for index, i in enumerate(flags):
                if i == 'q':
                    nex_word = words[index + 1][0]
                    if flags[index - 1] == 'm':
                        number_ = find_num(words[index - 1])
                        try:
                            number = int(number_[0])
                        except:
                            number = number_dict.get(number_[0])
                        str_dict[nex_word] = number
                    else:
                        str_dict[nex_word] = 1

        complete_str_ = ''.join([key*value for key,value in str_dict.items()])

    if 'uj' in flags:
        # rule five:  uj + . + r + v/. + uj + n/v
        index_ = flags.index('uj')
        if flags[index_+2] == 'r' and flags[index_+3] == 'v':
            complete_str_ = ''.join(words[:index_])
        elif flags[index_+1] in ['n','v']:
            complete_str_ = ''.join(words[:index_])

    if 'c' in flags:
        c_index = flags.index('c')
        if flags[c_index-1] != 'p' or flags[c_index+1] != 'm':
            complete_str_ = ''.join(list(re.findall('(.?)和(.?)|(.?)与(.?)',new_sentence)[0]))

    if complete_str_:
        # rule six:  . + r(multi) + v
        if 'r' in flags:
            index_ = flags.index('r')
            if flags[index_+1] == 'v':
                complete_str_ = ''.join(words[:index_])

    return complete_str_


def get_pinyin(input_complete_word):
    if len(input_complete_word) > 1:
        out_word = word_component_dict.get(input_complete_word)  # 拆字
        out_cz_pinyin = pinyin(input_complete_word)  # 词组
        if out_word:
            out_pinyin = pinyin(out_word)[0][0]
            output = out_word + ': ' + out_pinyin
            print(output)
        elif out_cz_pinyin:
            output = input_complete_word + ': ' + ' '.join([le for br in out_cz_pinyin for le in br])
            print(output)
    else:
        out_pinyin = pinyin(input_complete_word)[0][0]  # 单字
        if out_pinyin != input_complete_word:
            output = input_complete_word + ': ' + out_pinyin
            print(output)
        else:
            print('I don\'t know how to pronounce the word!')


# get_pinyin()

