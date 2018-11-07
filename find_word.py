from pypinyin import pinyin
from load_dict import ft_word_dict, number_dict


# 中文构字法
# 上下左右


# test
import jieba
import jieba.posseg as pseg
jieba.load_userdict(['左 f'])
jieba.suggest_freq(('八', '下'), True)  # 八下

# sentence = '左边是人，右边是人'  rule one
# sentence = '上八下白怎么读？'   rule one

# sentence = '上下结构八白怎么读'  rule two

# sentence = '三个人怎么读？'  rule three
# sentence = '左边一个人 右边一个人'  rule three

sentence = '提手旁，右边一个是'  rule three + rule four
sentence = '提字旁，加个是'  rule three + rule four
sentence = '穴字头音字底是什么' rule four

sentence = '女和为' ？

# sentence = '㵘的拼音'  rule five
# sentence = '六安的六怎么读？'  rule five

# sentence = '㵘怎么读'  rule six


word_list = list(pseg.cut(sentence, HMM=False))
print(word_list)


def get_word(input_sentence):
    remove_str_list = [' ','“','”','，','？','这个','应该','究竟']
    for i in remove_str_list:
        input_sentence = input_sentence.replace(i, '')
    new_sentence = input_sentence
    word_list = list(pseg.cut(new_sentence, HMM=False))
    words = [i.word for i in word_list]
    flags = [i.flag for i in word_list]

    special_case1 = ['是', '为']
    for i in special_case1:
        index_shi = words.index(i)
        if flags[index_shi-1] == 'n' or flags[index_shi-1] == 'f':
            words.pop(index_shi)
            flags.pop(index_shi)

    special_case2 = '字'
    zi_index = words.index(special_case2)
    if flags[zi_index+1] != 'f':
        words.pop(zi_index)
        flags.pop(zi_index)

    # using the rules of pos

    if 'f' in flags:
        if flags.count('f') > 1:
        # rule one: f + . f + .
            complete_str_ = ''
            for index, i in enumerate(flags):
                if 'f' == i:
                    complete_str_ += words[index+1]
        else:
        # rule two: f + n  number of f decide the number of '.'
            index_ = flags.index('f')
            complete_str_ = ''.join(words[index_+2:])[:len(words[index_])]

    # rule three: 个 + .  multiple
    if '个' in words:    # todo
        str_dict = {}
        for index, i in enumerate(flags):
            if 'q' == i:
                if flags[index-1] == 'm':
                    number_ = words[index-1]
                    try:
                        number = int(number_)
                    except:
                        number = number_dict.get(number_)
                    str_dict[words[index+1]] = number
                else:
                    str_dict[words[index+1]] = 1
        complete_str_ = ''.join([key*value for key,value in str_dict.items()])

    if 'uj' in flags:
        # rule five:  uj + . + r + v/. + uj + n/v
        index_ = flags.index('uj')
        if flags[index_+2] == 'r' and flags[index_+3] == 'v':
            complete_str_ = ''.join(words[:index_])
        elif flags[index_+1] in ['n','v']:
            complete_str_ = ''.join(words[:index_])
    else:
        # rule six:  . + r(multi) + v
        if 'r' in flags:
            index_ = flags.index('r')
            if flags[index_+1] == 'v':
                complete_str_ = ''.join(words[:index_])
    return complete_str_



get_word(sentence)


def get_pinyin(input_complete_word):
    if len(input_complete_word) > 1:
        # todo 区分拆字/词组
        out_word = ft_word_dict.get(input_complete_word)  # 拆字
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

