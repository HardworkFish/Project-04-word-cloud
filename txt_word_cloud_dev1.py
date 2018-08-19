import nltk
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 去掉停用词
stop = stopwords.words('english')
# 使用 set 集合过滤重复信息
stop = set(stop)


# 返回统计次数前 num 的字段
def common_words(tokens, num):
    return Counter(tokens).most_common(num)

# 导入数据集
# 数据集来源: https://www.usconstitution.net/const.txt
f = open('words-collection\const.txt')
text = f.read()

# 切分字段
tmp_tokens = nltk.word_tokenize(text)
data = [w.lower() for w in tmp_tokens]
print(common_words(data, 5))  # 输出出现次数最多的前 5 个字段（不区分大小写）


# 清洗停用词
data = [word for word in data if word not in stop]
print(common_words(data, 5))

# 去除标点符号
data = [word for word in data if word not in punctuation]
print(common_words(data, 5))

# 双线性插值
word_cloud = WordCloud().generate(text)
plt.imshow(word_cloud, interpolation="bilinear")
plt.axis("off")  # 关闭坐标轴
plt.show()

