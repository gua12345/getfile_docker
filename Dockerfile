FROM python:3.9-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt

# 复制应用代码
COPY app.py .

# 设置默认密码
ENV AUTH_PASSWORD=123456

# 暴露端口
EXPOSE 80

# 启动应用
CMD ["python", "app.py"]
