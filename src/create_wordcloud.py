from matplotlib import pyplot as plt
import wordcloud as wc

fontpath = 'ipaexg.ttf'

def init_wordcloud_obj():
    wordcloud = wc.WordCloud(
        font_path=fontpath,
        background_color="white",
        width=900,
        height=500,
    )
    return wordcloud

# 学習済みのwordcloudオブジェクトからワードクラウド画像を作成・表示します
def show_wordcloud(wordcloud):
    plt.figure(figsize=(16,10), dpi=60)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

def create_from_list(word_list):
    text = ' '.join(word_list)
    wordcloud = init_wordcloud_obj().generate(text)
    show_wordcloud(wordcloud)
        
# 単語の出現頻度の辞書からワードクラウドを作成します
def create_from_dict(word_dic):
    wordcloud = init_wordcloud_obj().generate_from_frequencies(word_dic)
    show_wordcloud(wordcloud)