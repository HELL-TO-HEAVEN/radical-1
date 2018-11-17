import pandas as pd
import os
'''
arc.head - 根据分词结果，当前词语所修饰的词语位置
'''


LTP_DATA_DIR = 'E:\\ltp_data_v3.4.0\\'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')

from pyltp import Segmentor
from pyltp import Parser
from pyltp import Postagger

segmentor = Segmentor()
postagger = Postagger()
parser = Parser()

segmentor.load(cws_model_path)
# segmentor.load_with_lexicon(cws_model_path, '/path/to/your/lexicon')
postagger.load(pos_model_path)
parser.load(par_model_path)
parser
# segmentor.release()
# postagger.release()
# parser.release()


def parser_out(input_sentence):
    words = segmentor.segment(input_sentence)
    postags = postagger.postag(words)
    arcs = parser.parse(words, postags)
    out_put = {'word':list(words),'pos':list(postags),'arc_head':[arc.head for arc in arcs],'arc_relation':[arc.relation for arc in arcs]}
    print(pd.DataFrame(out_put))
    # return out_put

input_sentence = '上面一个老下面一个日读什么'
parser_out(input_sentence)

