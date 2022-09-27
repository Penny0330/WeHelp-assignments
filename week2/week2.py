# 要求一：函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可以假設 max 一定大於 min 且為整數，step 為正整數。

def calculate(min, max, step):
    if max > step:
        sum = 0
        for x in range(min, max, step):
            sum += x
        print(sum + max)
    else:
        sum = 0
        for x in range(min, max, step):
            sum += x
        print(sum)


calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0

# 解題心得:
# 第一時間在理解題目時，想說到底是講什麼!!!! 突然靈光乍現，想起 for loop range裡的第3個參數的意義。

# ------------------------------------------------------------------------------------

# 要求二：Python 字典與列表
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量


def avg(data):
    count = len(data["employees"])
    x_count = 0
    sum_salary = 0
    for x in range(0, count):
        if data["employees"][x]["manager"] == False:
            x_count += 1
            sum_salary += data["employees"][x]["salary"]
    print(sum_salary/x_count)


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})  # 呼叫 avg 函式

# 解題心得:
# 不得不說，其實這題我卡超級無敵久，一直覺得我在dict、list的部分是不是有還不懂的地方，才一直解不出來。
# 後來解到很焦慮，就先跑去睡了，雖然睡前躺在床上還是瘋狂的想。
# 隔天一早: 突然想到應該要加變數 x_count = 0、sum_salary = 0，終於在昨天卡住的地方順利解脫\Y _ Y/\Y _ Y//\Y _ Y/
# 果然剛睡醒比較冷靜。

# ------------------------------------------------------------------------------------

# 要求三：


def func(a):
    def multiply(num1, num2):
        print(a + (num1*num2))
    return multiply


func(2)(3, 4)  # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5)  # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9)  # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# 解題心得:
# 這題莫名的就解開了，但底層的原理還不是很清楚，先記下這幾天要搞懂!

# -------------------------------------------------------------------------------

# 要求四：
# 找出至少包含兩筆整數的列表 (Python)中，兩兩數字相乘後的最大值。


def maxProduct(nums):
    length = len(nums)
    max_multiply = nums[0] * nums[1]
    for x in range(length-1):
        for y in range(x+1, length):
            total = nums[x] * nums[y]
            if total > max_multiply:
                max_multiply = total
    print(max_multiply)


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10

# 解題心得:
# 以前有解過比大小的題目，很快就知道要使用巢狀迴圈，在第一個迴圈中，range的次數要-1，在第二個迴圈中，起頭的地方要比第一圈的起頭+1，
# 這樣就不會有重覆相比數字的狀況。

# ------------------------------------------------------------------------------------

# 要求五：
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.


def twoSum(nums, target):
    length = len(nums)
    for x in range(length-1):
        for y in range(x+1, length):
            if nums[x] + nums[y] == target:
                return [x, y]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

# 解題心得:
# 整體架構與要求四的相似，邏輯想清楚很更就可以解開

# ------------------------------------------------------------------------------------

# 要求六 ( Optional )：
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
# 長度。


def maxZeros(nums):
    length = len(nums)
    max_zeros = 0
    sum_zeros = 0
    for x in range(length):
        if nums[x] == 0:
            sum_zeros += 1
        else:
            sum_zeros = 0
        if max_zeros < sum_zeros:
            max_zeros = sum_zeros
    print(max_zeros)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3

# 解題心得:
# 這題有點小卡，但其實不難，只要針對題目要求設定所需的變數，再for loop每個list的值去計算!
