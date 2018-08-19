from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Preparation work# Prepa
stop = stopwords.words('english')
# stop.append('theWordYouWantToGetRidOf')
stop = set(stop)

# Import Data
# Constitution data found at: https://www.usconstitution.net/const.txt
f = open('words-collection\const.txt')
text = f.read()
usa_coloring = np.array(Image.open('images-collection\george.jpg'))

wc = WordCloud(background_color='white',
               max_words=500,
               max_font_size=60,
               mask=usa_coloring,
               stopwords=stop,
               random_state=50)
wc.generate(text)

image_colors = ImageColorGenerator(usa_coloring)

plt.imshow(usa_coloring, cmap='gray', interpolation="bilinear")
plt.axis("off")
plt.show()

plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()

