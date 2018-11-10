# chaizi
![status](artworks/progress.svg)


## 基本思路







## rule
量词/数词/方位词 + 单字 (该单字为偏旁部首)  
数词 = 数词+量词  

#### drawback of rules:
1.若方位词/special_case3组词，则规则失效  
示例：  
'上海下士念什么'  
'人加工念什么'  
'扌上下这个字念什么'
2.无法保证拆字组成的顺序  
示例：  
'左边是三点水，中间是文，右边是利刀旁'


#### useful information
##### 构字法
前后左右，上下里外  

##### radical(偏旁/部首)

1. Each chinese radical has its special meaning, it connect every word with the same radical. Even though, there some radical connection with itself.

   Such as, there is connection between '罒' and '网', '罒  目', '灬  火'... 

Unsupervised clustering of Chinese characters by radical similarity
https://github.com/alenarr/zi-space 
    

2. How to separate chinese word to radical?


3. Source of radical information
https://en.wikipedia.org/wiki/Radical_(Chinese_characters)

http://www.archchinese.com/

http://www.chise.org/ids/

http://unicode.org/charts/unihan.html

https://www.mdbg.net/chinese/dictionary?page=radicals

##### other
百度找字，解析其边界及内部原理：  
边界 - 即哪些问法，它可以查到，换一种问法却查不到？）  
原理 - 貌似也是规则实现...  
![baidu_chaizi](https://github.com/bifeng/chaizi/tree/master/dict/baidu_chaizi.png)

搜狗拼音输入法

##### reference
https://github.com/kfcd/chaizi  
https://www.hackingchinese.com/kickstart-your-character-learning-with-the-100-most-common-radicals/  
https://github.com/JianshuZhang/RAN  
https://github.com/fortyMiles/PAIP-Python/tree/master/eliza  
