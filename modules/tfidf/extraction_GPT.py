from openai import OpenAI
import os
import json

client = OpenAI(api_key=OPENAI_API_KEY)

target_query = 'optim'
# 保存先のディレクトリを指定
save_directory = f"../../data/important_word/{target_query}/"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

file_path = f"../../data/text/{target_query}/{target_query}_top_words_by_tfidf.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": f"以下のテキストに基づいて、{target_query}や情報科学の文脈でよく使われる単語やフレーズを100個挙げてください。形容詞なども入れてください。\n\ntextが続きます。{text_content}"}
  ]
)

# JSON形式の応答を辞書に変換
output_content = json.loads(response.choices[0].message.content)

# JSONファイルに書き込む
output_file_path = f"../../data/important_word/{target_query}/{target_query}_top_words_by_GPT.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(output_content, output_file, ensure_ascii=False, indent=4)