let search_btn = document.querySelector(".search_btn");
search_btn.addEventListener("click", ()=>{
    let username = document.querySelector("#username").value;
    let result_username = document.querySelector(".result_username");
    fetch("http://127.0.0.1:3000/api/member?username=" + username)
    .then(function(response){
        return response.json();
    })
    .then(function(success){
        name = success.data.name;
        username = success.data.username;
        result_username.innerHTML = `${name} ( ${username} )`;
    })
    .catch(function(error){
        result_username.innerHTML = "無此人註冊";
    });
});


let update_btn = document.querySelector(".update_btn");
update_btn.addEventListener("click", ()=>{
    let update_name = document.querySelector("#update_name").value;
    let update_username = document.querySelector(".update_username");
    fetch("http://127.0.0.1:3000/api/member", {
        method:"PATCH",
        body:JSON.stringify({"name":update_name}),
        headers:{
            "Content-Type":"application/json"
        }
    })
    .then(function(response){
        return response.json();
    })
    .then(function(result){
        update_username.innerHTML = "更新成功";
    })
    .catch(function(error){
        update_username.innerHTML = "更新失敗";
    });
});
