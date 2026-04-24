# 作者: 苏尛鱼
# 2026年04月24日17时14分45秒
# xxx@qq.com
__all__=["Record"]
class Record:
    date: str = None
    order_id: str = None
    money: int = None
    province: str = None

    def __init__(self, date: str, order_id: str, money: int, province: str):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"[{self.date},{self.order_id},{self.money},{self.province}]"

    __repr__ = __str__
