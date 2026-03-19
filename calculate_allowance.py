def calculate_allowance(weeks: int) -> int:
    """
    计算指定周数的总零花钱。
    周一到周五每天5元，周六周日每天10元。
    :param weeks: 周数
    :return: 总零花钱（元）
    """
    weekday_money = 5 * 5      # 周一到周五
    weekend_money = 10 * 2     # 周六周日
    total = weeks * (weekday_money + weekend_money)
    return total

# 示例
if __name__ == "__main__":
    weeks = int(input("请输入周数："))
    print(f"{weeks}周的总零花钱为：{calculate_allowance(weeks)}元")