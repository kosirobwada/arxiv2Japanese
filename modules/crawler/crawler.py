import requests
from bs4 import BeautifulSoup
import os

# 検索クエリ
search_query = 'optim'

# 保存先のディレクトリを指定
save_directory = f"../../data/{search_query}/"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# 検索結果ページのURL
url = f'https://arxiv.org/search/?query={search_query}&searchtype=all&abstracts=show&order=-announced_date_first&size=50'

# requestsでURLからHTMLを取得
response = requests.get(url)
page_content = BeautifulSoup(response.text, 'html.parser')

# 検索結果からPDFのリンクを抽出（改善された方法）
pdf_links = [f"https://arxiv.org/pdf/{tag.get('href').split('/')[-1]}.pdf" for tag in page_content.find_all('a', href=True) if '/abs/' in tag.get('href')]

# PDFをダウンロードして保存
for link in pdf_links:
    response = requests.get(link)
    pdf_filename =  os.path.join(save_directory, link.split('/')[-1])  # URLからファイル名を抽出
    with open(pdf_filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {pdf_filename}")
