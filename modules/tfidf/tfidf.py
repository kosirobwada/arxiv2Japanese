from sklearn.feature_extraction.text import TfidfVectorizer
import json
import os

# ターゲットクエリ
target_query = 'optim'

# JSONファイルが格納されているディレクトリ
directory_path = f'../../data/json/{target_query}/'

# 結果を保存するテキストファイルのパス
output_file_path = f'../../data/text/{target_query}/{target_query}_top_words.txt'

# ディレクトリ内の全JSONファイルからテキストを読み込む
texts = []
for json_file in os.listdir(directory_path):
    if json_file.endswith('.json'):
        json_file_path = os.path.join(directory_path, json_file)
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            texts.append(data['optim'])
        print(f"Processed {json_file}")

# TF-IDFを計算
vectorizer = TfidfVectorizer(max_features=500, stop_words='english', ngram_range=(1, 3))
tfidf_matrix = vectorizer.fit_transform(texts)

# 各特徴(単語)のTF-IDFスコアに基づいて重要な単語を取得
feature_names = vectorizer.get_feature_names_out()

# 重要な単語をテキストファイルに保存
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for feature in feature_names:
        output_file.write(feature + '\n')

print(f"Top 2000 words have been saved to {output_file_path}")
