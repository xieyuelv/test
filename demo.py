from demo001.demo_03 import food_name

# def food_name(*food):
#     food_name=''
#     for i in food:
#         food_name+=i
#         if i!=food[-1]:#判断如果i不等于最后一个元素就往后加顿号
#             food_name+='、'
#     print("我喜欢的食物：{}".format(food_name))
def open_file():
    file=open("gushi.txt",mode='r',encoding="utf-8")
    a=file.readlines()
    return a

if __name__ == '__main__':
    food_name("扑街","叼毛")
    #print(open_file())
    print(open_file())