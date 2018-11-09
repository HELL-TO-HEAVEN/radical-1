> refer:  
https://github.com/kfcd/chaizi  
https://github.com/mozillazg/python-pinyin  
https://github.com/saigyo/common-chinese-radicals  
https://github.com/fortyMiles/PAIP-Python/tree/master/eliza  


## 基本思路
中文构字法:  
前后左右，上下里外  

生僻字构字法  
baidu找字，解析原理（哪些字它可以查到，哪些查不到？）  


## rule
量词/数词/方位词 + 单字 (该单字为偏旁部首)  
数词 = 数词+量词  

> notes:
1.若方位词/special_case3组词，则规则失效  
示例：  
'上海下士念什么'  
'人加工念什么'  
'扌上下这个字念什么'
2.无法区分拆字/词组  
笔画判断？  
3.无法保证拆字组成的顺序  
示例：  
'左边是三点水，中间是文，右边是利刀旁'


chaizi-jt.txt/chaizi-ft.txt
问题字：
□	目 仑  
□	目 军  
...  
睘	罒 一 口   

多种拆分-间隔不一：  
□	手 负	扌 负	才 负  
𢰻	手 臼 丨 丂	扌 臼 丨 丂	才 臼 丨 丂

拆法不全：  
'两个习，一个高'  
'一个口字里面有一个八和一个口字'  

特点：  
四百多个字，笔画一样，顺序不同.  


100-most-common-radicals.txt
问题字：
火	火	灬


pypinyin  
没有处理多音字


eliza  


