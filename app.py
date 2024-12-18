from flask import Flask, send_file, request, abort
import os
from functools import wraps

app = Flask(__name__)

# 从环境变量获取密码，默认为123456
AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD', '123456')

# 验证密码的装饰器
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or auth != f'Bearer {AUTH_PASSWORD}':
            return abort(401, 'Authentication required')
        return f(*args, **kwargs)
    return decorated

# 文件下载接口
@app.route('/<path:filepath>')
@require_auth
def get_file(filepath):
    try:
        # 构建完整的文件路径
        full_path = os.path.join('/', filepath)
        
        # 检查文件是否存在
        if not os.path.exists(full_path):
            return {'error': 'File not found'}, 404
            
        # 发送文件
        return send_file(full_path)
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
