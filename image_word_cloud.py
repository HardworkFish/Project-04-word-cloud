import nltk
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Preparation work# Prepa
stop = stopwords.words('english')
# stop.append('theWordYouWantToGetRidOf')
stop = set(stop)

def common_words(tokens, num):
    return Counter(tokens).most_common(num)

# Import Data
# Constitution data found at: https://www.usconstitution.net/const.txt
f = open('words-collection\const.txt')
text = f.read()

# Tokenize
tmp_toks = nltk.word_tokenize(text)
data = [w.lower() for w in tmp_toks]
common_words(data,5)

# Clear stop words
data = [word for word in data if word not in stop]
common_words(data,5)

data = [word for word in data if word not in punctuation]
common_words(data,5)

wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

usa_coloring = np.array(Image.open('images-collection\george.jpg'))

wc = WordCloud(background_color='white',
               max_words=500,
               max_font_size=60,
               mask=usa_coloring,
               stopwords=stop,
               random_state=50)
wc.generate(text)
image_colors = ImageColorGenerator(usa_coloring)
plt.imshow(usa_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.figure()