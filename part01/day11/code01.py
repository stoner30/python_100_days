"""
原始字符串
"""
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

# 原始字符串中，如果加入了破坏字符串结构的单引号或双引号，会提示语法错误，但是如果使用\'或者\"这种转义字符，则会输出反斜杠（\）
