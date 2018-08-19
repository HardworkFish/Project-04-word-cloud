from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 需要读取的文本
text = open('words-collection\const.txt').read()

# 生成词云对象放置到相应的坐标轴
word_cloud = WordCloud().generate(text)

plt.imshow(word_cloud)

# 关闭坐标轴信息
plt.axis("off")

# 显示生成的词云
plt.show()









