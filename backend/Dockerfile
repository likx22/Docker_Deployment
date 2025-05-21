# TODO: 补充Dockerfile
FROM python:3.8

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
# 网络卡顿,使用清华镜像源
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Copy application source code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1
