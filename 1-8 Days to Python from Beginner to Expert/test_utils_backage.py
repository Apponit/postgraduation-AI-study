# 作者: 苏尛鱼
# 2026年04月23日11时16分04秒
# xxx@qq.com
from my_utils import str_util
from my_utils import file_util
# print(str_util.str_reverse("123456"))
# print(str_util.substr("123456",0,2))
print("start------------")
file_util.print_file_info("file/test_utils.txt")
print("end------------")
file_util.append_file_info("file/test_utils.txt","Hello word!")
file_util.print_file_info("file/test_utils.txt")