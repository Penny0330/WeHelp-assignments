# Week5 - Assignments
## 要求三：SQL CRUD
* 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
  ```
  第1筆
  
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES ('test', 'test', 'test', 0);
  
  第2~7筆
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES('阿貓', '人類救星', 'cat', 100000);
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES('阿狗', '阿貓ㄉ敵人', 'dog', 500);
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES('人類', '阿貓ㄉ僕人', 'human', 0);
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES('阿虎', '貓星球的警察', 'tiger', 8000);
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES('罐罐', '美味的食物', 'HP+1', 5000);
  INSERT INTO `member`(`name`, `username`, `password`, `follower_count`) VALUES('小蟑', '阿貓ㄉ玩具', 'toy', 3500);
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196123199-57b51dbc-be61-4e57-b0a2-cabbd512814e.png)
---

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
  ```
  SELECT * FROM `member`;
  ```
   ![image](https://user-images.githubusercontent.com/110281590/196124264-416eb6c8-d395-4ee4-831c-63f5b531acb1.png)
--- 

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
  ```
  SELECT * FROM `member` ORDER BY `time` DESC;
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196124408-de8e7a76-f405-4cb3-ae5e-367517492432.png)
---
  
* 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
  ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
  ```
  SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1,3;
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196125133-c7d222df-34a2-43f5-a712-4859f2dc12d7.png)
---

* 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
  ```
  SELECT * FROM `member` WHERE `username` = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196128864-c546555f-b959-4557-b685-682b104600e2.png)
---

* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
  ```
  SELECT * FROM `member` WHERE `username` = 'test' AND `password` = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196128749-4beccbae-0599-494c-a7e4-f33ce83f3c71.png)
---

* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
  ```
  UPDATE `member` SET `name` = 'test2' WHERE `username` = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196128598-7a3b9b79-0920-405e-b62b-a3fcbcf48f97.png)
  ![image](https://user-images.githubusercontent.com/110281590/196162923-7ee22d3a-d693-4a0b-b2c9-285572b72faf.png)
---

## 要求四：SQL Aggregate Functions

* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
  ```
  SELECT COUNT(*) FROM `member`;
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196128467-33d6b9b6-c1d9-46ec-942a-97577615ed41.png)
---

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
  ```
  SELECT SUM(`follower_count`) FROM `member`;
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196129589-fdaf4596-05a2-4f9b-bec0-159a1c469e4f.png)
---

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
  ```
  SELECT AVG(`follower_count`) FROM `member`;
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196129950-b246977a-0135-4a4a-ab53-6daf4aa8b6ca.png)
---

## 要求五：SQL JOIN (Optional)
* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
  ```
  SELECT `message`.`id`, `member_id`, `name`, `content`, `like_count`, `message`.`time`
  FROM `message` JOIN `member`
  ON `member`.`id` = `message`.`member_id`;
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196163945-03d9bcb4-5fe0-4f4f-986c-3305b856baf9.png)
---

* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
  ```
  SELECT `message`.`id`, `member_id`, `name`, `username`, `content`, `like_count`, `message`.`time`
  FROM `message` JOIN `member`
  ON `member`.`id` = `message`.`member_id`
  WHERE `username` = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196161058-5a0776b5-493b-4a73-b11b-f4a9bf114e53.png)
---

* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
  ```
  SELECT `username` , AVG(`like_count`)
  FROM `message` JOIN `member`
  ON `member`.`id` = `message`.`member_id`
  WHERE `username` = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/110281590/196162100-355d4c3d-1962-43b1-bfe2-b6e52cd788a5.png)












