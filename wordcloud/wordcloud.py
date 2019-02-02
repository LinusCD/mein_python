from os import path
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import pandas as pd
import numpy as np
from scipy.misc import imread
from PIL import Image

txt = open('white_night.txt',encoding="gbk")
line = txt.readlines()   #读取文字
type(line)             #list无法完成jieba分词
line=','.join(line)    #将list转化为str
type(line)

stoplist = open('wordclean_list.txt',encoding="gbk")
stopwords = [line.strip() for line in open('wordclean_list.txt', 'r',encoding="gbk").readlines()]
#stopwords={}.fromkeys([line.rstrip() for line in stoplist])    #字典
for add in ['雪穗','桐原','笹垣','友彦','唐泽','秋吉','筱冢','今枝','典子','利子','一成','']:
     stopwords.append(add)
#stopwords='，'.join(stopwords)   此处不需要转化为string

word_list=jieba.cut(line,cut_all=False)
#word_cut='，'.join(word_list)
word_cut=list(word_list)
type(word_cut

cloud_mask = np.array(Image.open('/Users/huxugang/Github/boyandgirl.jpeg'))

back_color = imread('/Users/huxugang/Github/boyandgirl.jpeg')
image_colors = ImageColorGenerator(back_color)

wd=WordCloud(font_path='/Users/huxugang/Github/wordcloud_whitenight/simhei.ttf',\
             background_color='white',max_words=500,
             max_font_size=30,
             random_state=15,
             width=1200,  # 图片的宽
             height=400,  #图片的长
             mask=cloud_mask)

WD=wd.generate(word_cut)

import matplotlib.pyplot as plt
17WD.to_file('whitenight.jpg')
18# 显示词云图片
19plt.figure(figsize=(10,10))
20plt.axis('off')  #去掉坐标轴
21plt.imshow(WD.recolor(color_func=image_colors))
22#plt.show()