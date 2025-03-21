# Python 3.9 の軽量イメージを使用
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをコピー
COPY . .

# Gunicorn で PORT 環境変数を適切に処理
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} app:app"]

