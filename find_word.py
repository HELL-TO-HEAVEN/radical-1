from pypinyin import pinyin
from load_dict import ft_word_dict, number_dict


# 中文构字法
上下左右


# test
import jieba
import jieba.posseg as pseg
jieba.suggest_freq(('八', '下'), True)  # 八下


# sentence = '三个人怎么读？'  rule four
# sentence = '左边一个人 右边一个人'  rule four
# sentence = '左边是人，右边是人'
# sentence = '上下结构是八白怎么读'
# sentence = '上下结构为八白怎么读'
# sentence = '上下结构八白怎么读'
# sentence = '㵘这个怎么读'
# sentence = '㵘怎么读'
# sentence = '㵘的读音'
# sentence = '上八下白怎么读？'
sentence = '提手旁，右边一个是'
sentence = '提手旁，加个是'
words = list(pseg.cut(sentence, HMM=False))
print(words)


def get_word(input_sentence):
    new_sentence = input_sentence.replace(' ','').replace('字','')
    word_list = list(pseg.cut(new_sentence, HMM=False))
    words = [i.word for i in word_list]
    flags = [i.flag for i in word_list]

    # using the rules of pos

    # rule one: f + . f + .


    # rule two: f + v + .  multiple

    # rule three: f + n + (v/p)  number of f decide the number of '.'

    # rule four: m + .  multiple
    if 'm' in flags:
        str_dict = {}
        for index, i in enumerate(flags):
            if 'm' == i:
                number_ = words[index].replace('个','')
                try:
                    number = int(number_)
                except:
                    number = number_dict.get(number_)
                str_dict[words[index+1]] = number

        complete_str_ = ''.join([key*value for key,value in str_dict.items()])

    # last rule: x / . + r(multi) + v / . + uj + n


get_word(sentence)


def get_pinyin(input_complete_word):
    if len(input_complete_word) > 1:
        out_word = ft_word_dict.get(input_complete_word)
        if not out_word:
            out_pinyin = pinyin(out_word)[0][0]
            output = out_word + ': ' + out_pinyin
            print(output)
        else:
            print('I can\'t find the word!')
    else:
        out_pinyin = pinyin(input_complete_word)[0][0]
        if out_pinyin != input_complete_word:
            output = input_complete_word + ': ' + out_pinyin
            print(output)
        else:
            print('I don\'t know how to pronounce the word!')


# get_pinyin()

