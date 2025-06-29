"""
使用match和case构造分支结构
替代if/elif/else，使代码结构更清晰
"""
status_code = int(input('响应状态码：'))
match status_code:
    case 400:
        description = 'Bad Request'
    case 401:
        description = 'Unauthorized'
    case 403:
        description = 'Forbidden'
    case 404:
        description = 'Not Found'
    case 405:
        description = 'Method Not Allowed'
    case 418:
        description = 'I\'m a teapot'
    case 429:
        description = 'Too Many Requests'
    case 500:
        description = 'Internal Server Error'
    case _:
        description = 'Unkonwn Status Code'

print(f'状态码描述: {description}')

# 也可以使用合并模式将多个状态码合并处理
# match status_code:
#     case 400 | 405: description = 'Invalid Request'
#     case 401 | 403 | 404: description = 'Not Allowed'
#     ...
