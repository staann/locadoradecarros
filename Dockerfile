# Usando uma imagem base do Python
FROM python:3.10-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo requirements.txt se existir (opcional)
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código do projeto para dentro do container
COPY . .

EXPOSE 5000

# Comando para rodar o arquivo route.py
CMD ["python3", "route.py"]
