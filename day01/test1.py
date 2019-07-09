'''
.   可以匹配任意字符，除换行符
[内容]    匹配括号中的所有的
[a-z]     匹配小写的字母
[A-Z]     匹配大写的字母
[0-9]     匹配任意数字
'''
import re

print(re.findall('.', 'hello world'))
print(re.findall('[oel]', 'hello world'))
print(re.findall('[A-Z]', 'hello wolrd'))
print(re.findall('[0-9]', 'hello world123'))
print(re.findall('[0-9a-z]', 'hello world123'))
#       匹配除了小写的a-z以外的字符
print(re.findall('[^a-z]', 'hello world123'))
# \d    匹配数字 效果和[0-9]
print(re.findall('\d', 'hello world123'))
# \D    匹配除数字外的 效果和[^0-9]
print(re.findall('\D', 'hello world123'))
# \w    匹配字母数字和下划线[a-zA-Z0-9]
print(re.findall('\w', 'hello world123_,'))
# \W    匹配除了字母数字和下划线以外的
print(re.findall('\W', 'hello world123_,'))
# \s    匹配空格和换行符
print(re.findall('\s', 'hello world123_,\n'))
# \S    匹配非空格和换行符
print(re.findall('\S', 'hello world123_,\n'))
print('----------------------------------------------')
#   ^可以匹配多行开头，必须要加re.M
print(re.findall('^hello', 'hello...world\nhello 123', re.M))
#   $可以匹配每一行的结尾，必须要加re.M，符号放后面
print(re.findall('3$', 'hello...world\nhello 123', re.M))
#   \A只匹配整个字符串的开头，写re.M也没用
print(re.findall('\Ahello', 'hello...world\nhello 123d', re.M))
#   \Z匹配结尾，re.M不起作用，放后面
print(re.findall('d\Z', 'hello...world\nhello 123d', re.M))
#   \b匹配单词
print(re.findall(r'\bhello', 'helloworld\nhello 123d', re.M))
print('----------------------------------------------')
#   ()作为整体去匹配
print(re.findall('(or)', 'hello...world'))
#   x?匹配0个或任意一个x
print(re.findall('o?', 'hello...world\nabooo'))
#   x*匹配0个或多个x  贪婪匹配
print(re.findall('o*', 'hello...world\nabooo'))
# 匹配至少1个，贪婪匹配
print(re.findall('a+', 'hhhello..  hd.world'))
# 匹配{n}个
print(re.findall('h{2}', 'hhhhhello..  hd.world'))
# 匹配至少1个至多3个
print(re.findall('h{1,3}', 'hhhhhello..  hd.world'))
# 匹配至少一个
print(re.findall('h{1,}', 'hhhhhello..  hd.world'))
print(re.findall('h|a', 'hhhhhelaaalo..  hd.world'))
