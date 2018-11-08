from find_word import get_word
# sentence = '左边是人，右边是人'  # rule one
# sentence = '上下结构八白怎么读'  # rule two
# sentence = '三个人怎么读？'  # rule three

# pos: f/q
# sentence = '上八下白怎么读？'  # rule one
# sentence = '左边一个人 右边一个人'  # rule three
# sentence = '右边是个草' # rule three

# sentence = '穴字下加一音字是什么字'
# sentence = '一个走之底加一个加怎么读'
# sentence = '草字头 穴字头 宝盖头 提手旁 提字旁 走之底 之字底 ...' # top rule

# Baidu Normal test:
# sentence = '宝盖头下面一个晨什么字'
# sentence = '宝盖头底下一个辰,念什么?'

# sentence = '草字头加内念什么?'
# sentence = '草字头下面加内念什么'  # rule two
# sentence = '草字头加口再加内读什么'  # special_case3

# sentence = '女和为加一起念什么?'
# sentence = '牛和字拼起来怎么读'
# sentence = '女和为念什么'
# sentence = '草与和念什么'
# sentence = '一个女字旁和一个为念什么?'

# sentence = '前面一个“鱼”,后面一个“包”是什么字啊'

# sentence = '㵘的拼音'  # rule five
# sentence = '㵘怎么读' # rule six
# sentence = '又双叒叕怎么读？'
# sentence = '又双叒叕的叕怎么读？'  # rule five

# sentence = '上面一个老下面一个日读什么'
# sentence = '一个口字旁上面一个老下面一个日'

# import jieba.posseg as pseg
# word_list = list(pseg.cut(sentence, HMM=False))
# print(word_list)

# print("Out put: \'{x}\'".format(x=get_word(sentence)))


