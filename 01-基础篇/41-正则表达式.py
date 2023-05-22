

# 正则表达式：匹配指定规则的字符串
import ipaddress
import re

# s = '''xyg
# zyg yx
# zyx xy
# xygxyg
# xyggyx'''

# print(re.findall('.+', 'abc\ndef\ng', flags=re.DOTALL))
# print(re.findall('^x', s, flags=re.M))


phone_num = '''13880689999     15591888888
ab13430826666
15591558888
1339737977777
14678555555
15517444444
158027533333
13339900000
14763111111'''

# print(re.findall(r'\b(?:13[0-9]|14[5-9]|15[0-35-9])\d{8}\b', phone_num))
# res = re.search('(\d{3,4})-(\d{7,8})', 'Tel:028-7654321')
# print(res.group(2))

# res = re.finditer('(\d{3,4})-(\d{7,8})', 'Tel:028-7654321 Tel:029-87654321')
# for m in res:
#     print(m.group(2))


s = '''Host: movie.douban.com
Pragma: no-cache
Referer: https://cn.bing.com/'''
# dic = {}
# res = re.finditer('(.*): (.*)', s)
# for m in res:
#     dic[m.group(1)] = m.group(2)
#
# print(dic)

# re.match()
# re.fullmatch()

# def des(m):
#     tel = m.group(2)
#     return tel[:2]+'***'+tel[-2:]
#
# print(re.subn('(\d{3,4})-(\d{7,8})', des, 'Tel:028-7654321 Tel:029-87654321'))
#
# s = 'xyg,- time,  !dog,  cat'
# print(re.split('\W+', s))


# res = re.compile('.*',flags=)
# res.






