from pypinyin import load_phrases_dict
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

    ft_word_dict = {}
    for word in all_word:
        new_word = word.strip().split('\t')
        values_ = new_word[0]
        new_word.remove(new_word[0])
        for i in range(len(new_word)):
            ft_word_dict[new_word[i].replace(' ','')] = values_

    ft_word_dict.update(split)
    load_phrases_dict(pinyin)
    return ft_word_dict


ft_word_dict = update_dict(new_word_split_dict,new_word_pinyin_dict)


number_dict = {
    '一':1,
    '二':2,
    '三':3,
    '四':4,
    '五':5
}

