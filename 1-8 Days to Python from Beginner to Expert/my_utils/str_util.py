# 作者: 苏尛鱼
# 2026年04月23日11时08分00秒
# xxx@qq.com
def str_reverse(s):
    return s[::-1]
def substr(s,x,y):
    return s[x:y:1]
if __name__ == '__main__':
    print(str_reverse("123456"))
    print(substr("123456",0,2))