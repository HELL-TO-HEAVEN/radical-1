# radical
![status](artworks/progress.svg)


## 基本思路
如何通过含有偏旁部首的问句，回答所问的字？  
譬如：  
上面宝盖中间心下面用念什么？ -- 甯-nìng

这是一个拆字和一个拼字的过程，看起来就是一个简单的查字典+规则方法就可以解决。

1). 列举50个左右常用问法(生僻字、百度找字等)  
2). 分析句子的特征(词性、语法等)  
3). 总结规则  

**由拆字引发的一点思考**  
​	在总结规则过程中，你会发现这个问题对应的有效信息非常强，而噪音比较弱，因此解决方法可以将重点放在有效信息的提取。  
​	我们发现在通信中解决噪音干扰的基本思路适用于大部分的自然语言处理任务，无论是采用规则还是统计的方法，都不会脱离这两种思路，即要么加强通信模型的抗干扰能力，要么过滤噪音、还原信息。  
​	在这两种思路的指导下，选择合适的方法去解决问题。

以拆字为例：  
1). 在有效信息较强的情况下，直接提取句子的偏旁部首

2). 在噪音较强的情况下，去除句子中不含偏旁部首的字  
这类噪音比较多，规则的方法无法穷举，因此可以采用模型的方法。

非监督 - 可以探索问句中的词向量聚类（偏旁部首的向量与噪音的字向量）  

监督 - 建立句子（x）与字（y）的关系
​       tfidf...
​       词向量...偏旁部首的向量与字向量是否存在数量关系?


## rule
[Rules](https://github.com/bifeng/radical/blob/master/Rules.md)


#### drawback of rules:
1. 基于词性建立的规则，依赖于词性的判断是否准确

2. 若拆字的顺序或问法不规范，则无法查找

```
'人工和石念什么'  # baidu ok - 百度找字，可以正确返回该字
'石和人工念什么'  # baidu ok

'一个口字里面有一个八和一个口字是什么意思啊'
```

分析字典中偏旁部首相同、顺序不同的字的特征

3. 未通过测试的样例

若方位词/特殊干扰词等词语与关键字组词，则规则失效

若方位词也是关键字，则规则失效

...

```
'上海下士念什么'  
'人加工念什么'  # baidu ok - 百度找字，可以正确返回该字
'扌上下这个字念什么'
'日+成,上下结构,念什么?'
'上下边是人念啥'  # baidu ok
'上下结构都是乂念什么'
'外面是口,里面是四面,八方这两个字是什么啊'
'一个草字头两个口地下一个焦去四点底念什么'
```


#### useful information
##### 中文构字法
前后左右，上下里外  

##### radical(偏旁/部首)

1. Each chinese radical has its special meaning, it connect every word with the same radical. Even though, there some radical connection with itself.

   Such as, there is connection between '罒' and '网', '罒  目', '灬  火'... 

   Unsupervised clustering of Chinese characters by radical similarity
   https://github.com/alenarr/zi-space 
   Radical Analysis Network for Learning Hierarchies of Chinese Characters
   https://github.com/JianshuZhang/RAN

2. How to separate chinese word to radical?

   what's the correlation between the word embedding and radical embedding?

3. IDS - Ideographic Description Sequences

    Unicode 组织在 3.0 版本开始，对 CJKV 统一表意文字做了一个新的支持——[表意文字描述序列](https://zh.wikipedia.org/zh-hk/%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E6%8F%8F%E8%BF%B0%E5%AD%97%E7%AC%A6)（Ideographic Description Sequences，以下简称IDS）。**其目的是利用十二种组合字符，来描述所定义的汉字内部构字部件的相对位置，从而精确表示生僻字（或未被电脑字符集收入的缺字）。**

http://www.babelstone.co.uk/Fonts/PUA.html

https://github.com/cjkvi/cjkvi-ids

https://github.com/LingDong-/rrpl

http://www.chise.org/ids/ - 繁体字

Inspired by: http://bangumi.tv/group/topic/341210

4. Source of radical information
   https://en.wikipedia.org/wiki/Radical_(Chinese_characters)

   https://en.wikipedia.org/wiki/Kangxi_radical

  [Unihan Database Lookup](http://unicode.org/charts/unihan.html)

  https://www.mdbg.net/chinese/dictionary?page=radicals

##### other
百度找字，解析其边界及内部原理：  
​	边界 - 即哪些问法，它可以查到，换一种问法却查不到？）  
​	原理 - 貌似也是规则实现...  
![baidu_chaizi](https://github.com/bifeng/radical/raw/master/dict/baidu_chaizi.png)

搜狗拼音输入法：  
​	居然可以打拼音声调和偏旁部首...

##### reference
https://github.com/kfcd/chaizi

https://github.com/LingDong-/rrpl

http://www.archchinese.com/  

https://www.hackingchinese.com/kickstart-your-character-learning-with-the-100-most-common-radicals/  
https://github.com/JianshuZhang/RAN  
https://github.com/fortyMiles/PAIP-Python/tree/master/eliza  