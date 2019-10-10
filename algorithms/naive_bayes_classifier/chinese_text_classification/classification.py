# %%
import os
import jieba  # chinese word cut/tokenization package
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


# %%

warnings.filterwarnings('ignore')

# %%


def cut_words(file_path):
    """
    tokenization
    :param file_path: txt file path
    :return: whitespace separated string
    """
    text_with_spaces = ''
    text = open(file_path, 'r', encoding='gb18030').read()
    textcut = jieba.cut(text)
    for word in textcut:
        text_with_spaces += word + ' '
    return text_with_spaces


def loadfile(file_dir, label):
    """
    load all files
    :param file_dir: txt file directory
    :param label: document labels
    :return: document list and labels after tokenization
    """
    file_list = os.listdir(file_dir)
    words_list = []
    labels_list = []
    for file in file_list:
        file_path = file_dir + '/' + file
        words_list.append(cut_words(file_path))
        labels_list.append(label)
    return words_list, labels_list


# %%
# get base directory
script_dir = os.path.dirname(__file__)

# %%
# load training data
train_words_list1, train_labels1 = loadfile(
    os.path.join(script_dir, 'text/train/女性'), '女性')
train_words_list2, train_labels2 = loadfile(
    os.path.join(script_dir, 'text/train/体育'), '体育')
train_words_list3, train_labels3 = loadfile(
    os.path.join(script_dir, 'text/train/文学'), '文学')
train_words_list4, train_labels4 = loadfile(
    os.path.join(script_dir, 'text/train/校园'), '校园')

train_words_list = train_words_list1 + train_words_list2 + \
    train_words_list3 + train_words_list4
train_labels = train_labels1 + train_labels2 + train_labels3 + train_labels4

# %%
# load testing data
test_words_list1, test_labels1 = loadfile(
    os.path.join(script_dir, 'text/test/女性'), '女性')
test_words_list2, test_labels2 = loadfile(
    os.path.join(script_dir, 'text/test/体育'), '体育')
test_words_list3, test_labels3 = loadfile(
    os.path.join(script_dir, 'text/test/文学'), '文学')
test_words_list4, test_labels4 = loadfile(
    os.path.join(script_dir, 'text/test/校园'), '校园')

test_words_list = test_words_list1 + test_words_list2 + \
    test_words_list3 + test_words_list4
test_labels = test_labels1 + test_labels2 + test_labels3 + test_labels4

# %%
# get stop words
stop_words = open(os.path.join(script_dir, 'text/stop/stopword.txt'),
                  'r', encoding='utf-8').read()
stop_words = stop_words.encode('utf-8').decode('utf-8-sig')  # \ufeff transform
stop_words = stop_words.split('\n')  # split by newline

# %%
# weight of words
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)

# %%
# fit and transform
train_features = tf.fit_transform(train_words_list)
test_features = tf.transform(test_words_list)

# %%
# multinominal bayesian classifier
clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
predicted_labels = clf.predict(test_features)

# %%
# calc accuracy
print('prediction accuracy is：', metrics.accuracy_score(
    test_labels, predicted_labels))
