# sentence = '左边是人，右边是人，什么字'  # rule one
# sentence = '上八下白怎么读？'

# sentence = '入下面一个工怎么读？'  # rule two + rule three

# sentence = '三个人怎么读？'  # rule three
# sentence = '两个呆在一起念什么'
# sentence = '左边一个人 右边一个人怎么念'


# sentence = '前面一个“鱼”,后面一个“包”是什么字啊'
# sentence = '上下两个人是什么字'
# sentence = '两个人上下摞起来是什么字'


# sentence = '木加华合起来怎么念?'  # special_case3
# sentence = '月加并念什么意思'
# sentence = '牛加匕念什么关系'


# sentence = '穴字下加一音字是什么字'  #  top rule + special_case3
# sentence = '一个走之底加一个加怎么读'
# sentence = '草字头加内念什么?'
# sentence = '草字头下面加内念什么'
# sentence = '草字头加口再加内读什么'
# sentence = '三点水加口加内读什么'
# sentence = '草字头加門里面加口念什么'


# sentence = '日和成加起来念什么'  # regex rule + special_case3
# sentence = '女和为加一起念什么?'  #

# sentence = '草字头 穴字头 宝盖头 提手旁 提字旁 走之底 之字底 ...' # top rule


# Baidu Normal test:
# sentence = '宝盖头下面一个晨什么字'
# sentence = '宝盖头底下一个辰,念什么?'

# sentence = '一个女字旁和一个为念什么?'  # top rule + rule three

# sentence = '日和人拼一起念什么'  # regex rule
# sentence = '牛和字拼起来怎么读'
# sentence = '女和青一起是什么字'
# sentence = '女和羽拼在一起念什么'
# sentence = '女和为念什么'
# sentence = '日和成组合读什么字与拼音'


# sentence = '㵘的拼音是什么'  # rule five


# sentence = '㵘怎么读' # rule six
# sentence = '首或加起来念什么'
# sentence = '米更拼起来念什么'
# sentence = '“女禾”合在一起念什么'
# sentence = '王已合一起念什么'
# sentence = '吉力两个字合在一起念什么?'


# sentence = '吉力念什么?'
# sentence = '又双叒叕怎么读？'
# sentence = '又双叒叕的叕怎么读？'  # rule five

# sentence = '上面一个老下面一个日读什么'
# sentence = '一个口字旁上面一个老下面一个日读什么'

# sentence = '三个龙字怎么读？'
# sentence = '龘这个字怎么读？'
# sentence = '犇骉鱻羴麤飝龘怎么念'
# sentence = '㒶怎么读？'
# sentence = '又又又又支怎么读？'

# import jieba.posseg as pseg
# word_list = list(pseg.cut(sentence, HMM=False))
# print(word_list)

# from find_word import get_word
# print("Out put: \'{x}\'".format(x=get_word(sentence)))

# todo untest
sentence = '㵘读音是什么'
sentence = '㵘字的读音是什么'
sentence = '“㵘”字怎么读'
sentence = '一个"多"字加一个走之底,是什么字'
sentence = '草字头下面一个开右边一个利刀旁是什么字'
sentence = '一个草字头,下面一个豕,右边一个生是什么字'
sentence = '上下结构“功夫”是什么字'
