from find_word import get_word
# sentence = '左边是人，右边是人'
sentence = '上八下白怎么读？'

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

print(get_word(sentence))


