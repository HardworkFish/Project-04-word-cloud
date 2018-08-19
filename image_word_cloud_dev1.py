#!/usr/bin/env python
"""
Using custom colors
===================

Using the recolor method and custom coloring functions.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

mask = np.array(Image.open(r"images-collection\black_cat_version2.png"))

# movie script of "a new hope"
# http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
# May the lawyers deem this fair use.
text = open(r'words-collection\shakespeare-alls-11.txt').read()

# pre-processing the text a little bit
text = text.replace("HAN", "Han")
text = text.replace("LUKE'S", "Luke")

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)
# store default colored image
default_colors = wc.to_array()
# plt.title("Custom colors")
# plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
#            interpolation="bilinear")

# plt.axis("off")
# plt.figure()
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
wc.to_file(r"images-collection\a_new_cat.png")
plt.axis("off")
plt.show()
