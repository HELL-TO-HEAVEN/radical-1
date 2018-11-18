import regex
path = "C:\\Users\\kiss\\radical\\rule\\"

with open(path + 'sentence_components.txt',encoding='utf-8') as f1:
    tag_files = f1.readlines()
tag_dict = {}
last_keys = None
for each in tag_files:
    each_ = each.strip()
    if each_:
        if each_.startswith('t_') and each_ not in tag_dict.keys():
            tag_key = each_.strip(':')
            tag_dict[tag_key] = []
            last_keys = tag_key
        else:
            tag_dict[last_keys].append(each_)

with open(path + 'sentence_rules.txt',encoding='utf-8') as f1:
    rule_files = f1.readlines()
rule_dict = {}
last_keys = None
for each in rule_files:
    each_ = each.strip()
    if each_ and not each_.startswith('#'):
        if each_.startswith('p_') and each_ not in rule_dict.keys():
            rule_dict[each_] = []
            last_keys = each_
        else:
            rule_dict[last_keys].append(each_)

con = '\(\[|\]\|\)|\[|\]'
split_con = {'\)\(':')sep(','\)\[':')sep[','\]\(':']sep(','\]\[':']sep['}


def rule_extract(rule, sentence):
    # todo
    # 1.如果sentence_components有交集，则优先匹配长串。
    # 示例：
    # t_wg_and:加 与 t_wg_allin:加起来
    # 2.sentence_components，优先匹配长串（排序）。

    # keep rule order
    for sp,value in split_con.items():
        rule=regex.sub(sp,value,rule)
    rule = rule.split('sep')

    match_dict={}
    new_sentence = sentence
    for each_ in set(rule):
        if "*" not in each_:
            key_name = regex.sub(con, '', each_)
            rule_counts = rule.count(each_)
            if rule_counts > 1:
                for number in range(rule_counts):
                    new_key_name = key_name + '_' + str(number)
                    try:
                        match_dict[new_key_name] = regex.search(r'|'.join(tag_dict[key_name]), new_sentence).captures()[0]
                        new_sentence = new_sentence.replace(match_dict[new_key_name],'')
                    except:
                        match_dict[new_key_name] = None
            else:
                try:
                    match_dict[key_name] = regex.search(r'|'.join(tag_dict[key_name]), new_sentence).captures()[0]
                    new_sentence = new_sentence.replace(match_dict[key_name], '')
                except:
                    match_dict[key_name] = None

    # unmatch part is *
    unmatch = regex.sub('|'.join([i for i in match_dict.values() if i]),'', sentence)
    match_dict['*'] = unmatch

    return match_dict


# test
sentence = '两个人上下摞起来是什么字'
rule_extract('([t_wg_num]|)[*]([t_direction_wg]|)([t_direction_wg]|)([t_wg_allin]|)([t_wg_is]|)([t_wg_zi]|)[t_wg_end]', sentence)



rule_match = {}
for key,value in rule_dict.items():
    max_len=0
    max_len_dict={}
    for each_ in value:
        out=rule_extract(each_, sentence)
        if len([1 for key, value in out.items() if value])>max_len:
            max_len_dict = out

    rule_match[key] = max_len_dict

