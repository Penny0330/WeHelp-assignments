// 要求一：函式與流程控制
// 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可以假設 max 一定大於 min 且為整數，step 為正整數。

function calculate(min, max, step){
    if (max > step){
        let sum = 0;
        for(let i = min; i < max; i += step){
            sum += i;
        }
        console.log(sum + max);
    }else{
        let sum = 0;
        for(let i = min; i < max; i += step){
            sum += i;
        }
        console.log(sum);
    }
}

    calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
    calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
    calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0

// ---------------------------------------------------------------------------------------

// 要求二：JavaScript 物件與陣列
// 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
// manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
// 不定的情況。

function avg(data){
    let count = data["employees"].length;
    let x_count = 0;
    let sum_salary = 0;
    for(let i = 0; i < count; i++){
        if(data["employees"][i]["manager"] == false ){
            x_count += 1;
            sum_salary += data["employees"][i]["salary"];
        }
    }
    console.log(sum_salary / x_count);
}

    avg({
    "employees":[
    {
    "name":"John",
    "salary":30000,
    "manager":false
    },
    {
    "name":"Bob",
    "salary":60000,
    "manager":true
    },
    {
    "name":"Jenny",
    "salary":50000,
    "manager":false
    },
    {
    "name":"Tony",
    "salary":40000,
    "manager":false
    }
    ]
    }); // 呼叫 avg 函式

// ---------------------------------------------------------------------------------------

// 要求三：

function func(a){
    function multiply(num1, num2){
        console.log(a + (num1 * num2));
    }
    return multiply;
}

    func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
    func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
    func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
    // 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

// ---------------------------------------------------------------------------------------

// 要求四：
// 找出至少包含兩筆整數的陣列 (JavaScript) 中，兩兩數字相乘後的最大值。

function maxProduct(nums){
    let max_multiply = nums[0] * nums[1];
    for(let i = 0; i < nums.length - 1; i++){
        for(let j = i+1; j < nums.length; j++){
            let total = nums[i] * nums[j];
            if (total > max_multiply){
                max_multiply = total;
            }
        }
    }
    console.log(max_multiply); 
}

    maxProduct([5, 20, 2, 6]); // 得到 120
    maxProduct([10, -20, 0, 3]); // 得到 30
    maxProduct([10, -20, 0, -3]) ;// 得到 60
    maxProduct([-1, 2]); // 得到 -2
    maxProduct([-1, 0, 2]); // 得到 0 或 -0
    maxProduct([5, -1, -2, 0]); // 得到 2
    maxProduct([-5, -2]); // 得到 10

// ---------------------------------------------------------------------------------------

// 要求五：
// Given an array of integers, show indices of the two numbers such that they add up to a
// specific target. You can assume that each input would have exactly one solution, and you
// can not use the same element twice.

function twoSum(nums, target){
        let len = nums.length;
        for(let i = 0; i < len-1; i++){
            for(let j = i + 1; j <len; j++){
                if(nums[i] + nums[j] == target){
                    return [i, j];
                }
            }
        }
    }
    
    let result=twoSum([2, 11, 7, 15], 9);
    console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// ---------------------------------------------------------------------------------------

// 要求六 ( Optional )：
// 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
// 長度。

function maxZeros(nums){
    let nums_len=nums.length;
    let max_zeros=0;
    let sum_zeros=0;
    for (let i = 0; i < nums_len; i++){
        if(nums[i]==0){
            sum_zeros+=1;
        }else{
            sum_zeros=0;
        }
        if(max_zeros < sum_zeros){
            max_zeros = sum_zeros;
        }
    }
    console.log(max_zeros);
}

    maxZeros([0, 1, 0, 0]); // 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
    maxZeros([1, 1, 1, 1, 1]); // 得到 0
    maxZeros([0, 0, 0, 1, 1]) // 得到 3
