from wordcloud import WordCloud


def get_keywords(words):
    unique_words = sorted(set(words))

    dict={}
    for word in unique_words:
        # print(words.count(word), word)
        dict[word]=words.count(word)
    sorted_wordlist = sorted(dict.items(), key=lambda kv: kv[1])
    sorted_wordlist.reverse()

    ten_kw = []
    max_kw = 10
    for i in range(0,max_kw):
        ten_kw.append(sorted_wordlist[i][0])

    return sorted_wordlist, ten_kw


def get_wordart(words):
    dict ={}
    for word in words:
        dict[word[0]]=0

    for word in words:
        dict[word[0]]=dict[word[0]]+1

    sorted_x = sorted(dict.items(), key=lambda kv: kv[1])
    sorted_x.reverse()

    word_dict={}
    for x in sorted_x:
        word_dict[x[0]]=x[1]
        
    wordart = WordCloud(font_path='kalpurush.ttf',min_font_size = 10, scale = 2.5, background_color="white").generate_from_frequencies(word_dict)

    return wordart