import random

def get_hint(diff):
    if diff == 0:
        return "恭喜你，猜对了！"
    elif diff <= 2:
        return "太接近了！只差一点点！"
    elif diff <= 5:
        return "很接近了！"
    elif diff <= 10:
        return "有点接近。"
    else:
        return "差得有点远哦~"

def guess_number():
    number = random.randint(1, 100)
    print("欢迎来到猜数字游戏！")
    name = input("请先输入你的名字：")
    print(f"{name}，我已经想好了1到100之间的一个数字。你能猜到吗？")
    attempts = 0
    while True:
        guess = input("请输入你的猜测（1-100）：")
        try:
            guess = int(guess)
        except ValueError:
            print("请输入有效的数字！")
            continue
        if guess < 1 or guess > 100:
            print("数字要在1到100之间哦！")
            continue
        attempts += 1
        diff = abs(guess - number)
        hint = get_hint(diff)
        if diff == 0:
            print(f"{hint}你一共猜了{attempts}次。")
            break
        elif guess < number:
            print(f"{hint}再大一点试试！")
        else:
            print(f"{hint}再小一点试试！")

if __name__ == "__main__":
    guess_number()