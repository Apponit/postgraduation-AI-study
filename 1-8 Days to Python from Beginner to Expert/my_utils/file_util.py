# 作者: 苏尛鱼
# 2026年04月23日11时08分11秒
# xxx@qq.com
def print_file_info(file_name):
    f=None
    try:
        f=open(file_name,"r",encoding="UTF-8")
    except Exception as e:
        print(f"出现异常：{e}")
        f=open(file_name,"w",encoding="UTF-8")
    else:
        context=f.read()
        print(context)
    finally:
        if f:
            f.close()
def append_file_info(file_name,data):
    f=open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.flush()