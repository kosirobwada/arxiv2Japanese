import fitz  # PyMuPDF
import json
import os

# PDFファイルが格納されているディレクトリ
directory_path = '../../data/pdf/optim/'

# JSONファイルを保存するディレクトリ
json_directory_path = '../../data/json/optim/'

# JSONファイル保存用ディレクトリが存在しない場合は作成
if not os.path.exists(json_directory_path):
    os.makedirs(json_directory_path)

# ディレクトリ内のPDFファイルのリストを取得
pdf_files = [file for file in os.listdir(directory_path) if file.endswith('.pdf')]
if not pdf_files:
    print("PDFファイルがディレクトリ内に見つかりませんでした。")
else:
    for pdf_file in pdf_files:
        # PDFファイルを開き、テキストを抽出
        doc = fitz.open(os.path.join(directory_path, pdf_file))
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        # 抽出したテキストをJSON形式で保存
        json_data = {"optim": text}
        json_filename = os.path.splitext(pdf_file)[0] + '.json'  # PDFと同じ名前でJSONファイルを作成
        with open(os.path.join(json_directory_path, json_filename), 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        print(f"{json_filename}にテキストを保存しました。")