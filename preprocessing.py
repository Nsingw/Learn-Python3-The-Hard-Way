# 典型的文本预处理过程
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


# 原始文本
raw_text = 'Life is like a box of chocolates. You never know what you\‘re gonna get.'

# 分词
raw_words = nltk.word_tokenize(raw_text)  # nltk.word_tokenize()分词，nltk.sent_tokenize()按句子分割

#词形还原，如ate还原为eat
wordnet_lematizer = WordNetLemmatizer()
words = [wordnet_lematizer(raw_word) for raw_word in raw_words]  # 好像没有指定单词的词性

# 去除停用词
filtered_words = [word for word in words if word not in stopwwords.words('english')]

print('原始文本：', raw_word)
print('预处理结果：', filtered_words)
