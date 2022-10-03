function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        new_data = data["result"]["results"];
        let n = 0;
        for(let i = 0; i < 2; i++){
            // 上面兩個框框
            let pro_div = document.createElement("div");
            pro_div.setAttribute("class", "promotion");
            //取的 file 裡的第一張圖片網址
            let pro_pic = new_data[i].file;
            let pro_pic_1 = pro_pic.split("https");
            pro_pic_1 = "https" + pro_pic_1[1];
            // 將圖片放入
            let pro_img = document.createElement("img");
            pro_img.src = pro_pic_1;
            // 取德 file 裡的 stitle 文字
            let pro_text = document.createTextNode(new_data[i].stitle);
            // 將節點放入
            pro_div.appendChild(pro_img);
            pro_div.appendChild(pro_text);
            let pro_section = document.querySelector(".pro");
            pro_section.appendChild(pro_div);
        }

        for(let i = 2; i < 10; i++){
            // 下面八個框框
            let item_div = document.createElement("div");
            item_div.setAttribute("class", "item1");
            //取的 file 裡的第一張圖片網址
            let item_pic = new_data[i].file;
            let item_pic_1 = item_pic.split("https");
            item_pic_1 = "https" + item_pic_1[1];
            // 將圖片放入
            let item_img = document.createElement("img");
            item_img.src = item_pic_1;
            // 取德 file 裡的 stitle 文字
            let item_text = document.createTextNode(new_data[i].stitle);
            // 將節點放入
            item_div.appendChild(item_img);
            item_div.appendChild(item_text);
            let item_section = document.querySelector(".item");
            item_section.appendChild(item_div);
        }
    })
}

// 點擊 button 生成八張圖
let button = document.querySelector(".btn");
let n = 10
button.addEventListener("click", function(){
    
    for(let i = n; i <  n + 8; i++){
        let item_div = document.createElement("div");
        item_div.setAttribute("class", "item1");
        let item_pic = new_data[i].file;
        let item_pic_1 = item_pic.split("https");
        item_pic_1 = "https" + item_pic_1[1];
        let item_img = document.createElement("img");
        item_img.src = item_pic_1;
        let item_text = document.createTextNode(new_data[i].stitle);
        item_div.appendChild(item_img);
        item_div.appendChild(item_text);
        let item_section = document.querySelector(".item");
        item_section.appendChild(item_div);
    }
    n = n + 8;
})