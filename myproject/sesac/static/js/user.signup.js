function enterFunc(event, id, focus){
    data = document.querySelector(`#${id}`)

    if(event.code=="Enter"){
        console.log(data.value)
    
        if(data.value.length==0){
            event.preventDefault()
            Swal.fire({
                icon: 'warning',                         // Alert 타입
                title: '경고',         // Alert 제목
                text: `${id}은 필수 입력 항목입니다.`  // Alert 내용
            });
        }
        else{
            event.preventDefault()
            document.querySelector(`#${focus}`).focus() // enter 누르면 다음으로 focus 이동

            if(id=="pwcheck"){
                pwCheckValue = data.value
                dropDulp(pwCheckValue)
                }
            }
    }
}

function dropDulp(pwCheckValue){
    pwValue = document.querySelector('#userPw').value
    pwCheckValue2 = document.querySelector('#pwcheck')
    check = document.querySelector('#check')

    if(pwValue!=pwCheckValue){
        console.log("pw 와 pwCheck의 값이 다릅니다.")
        li = document.createElement('li')
        li.setAttribute("id" ,"new")
        li.innerText = "비밀번호와 일치하지 않습니다. 다시 입력해주세요."
        check.appendChild(li)
        pwCheckValue2.value=""
    }
    else{
        console.log("pw 와 pwCheck의 값이 같습니다.")
    }
}

function btnClick(event){
    i=0
    clas = document.querySelectorAll(".clas")
    for(i=0; i<=6; i++){
        if(clas[i].value.length==0){
            Swal.fire({
                icon: 'error',                         // Alert 타입
                title: '경고',         // Alert 제목
                text: "내용 다 채워주세요.",  // Alert 내용
            });
            event.preventDefault()
        }
    }
}

function inputClick(){
    p = document.querySelector("#new")
    if(p){
        p.remove()
    }
}

function duplicate(event){
    subNm = document.querySelector("#subNm").value
    if(subNm.length==0){
        event.preventDefault()
    }

    myData={
        "subNm":subNm
    }

    init = {
        method: "POST",
        body: JSON.stringify(myData),
        headers: {
          "Content-Type": "application/json"
        },
        credentials : "same-origin"
    }

    fetch("/user/respones", init)
    .then(response => {
        if(response.status === 200){
          return response.json()
        } else {
          console.log(response.statusText);
        }
    })
    .then(jsonData => {
        json = jsonData['msg']

        li = document.querySelector("#nick")
        a = document.createElement("li")
        a.setAttribute("id", "new")
        a.innerText= json
        li.appendChild(a)
    })
    //console.log(response)
}

function duplicate2(event){
    userId = document.querySelector("#userId").value
    if(userId.length==0){
        event.preventDefault()
    }
    
    myData={
        "userId":userId
    }

    init = {
        method: "POST",
        body: JSON.stringify(myData),
        headers: {
          "Content-Type": "application/json"
        },
        credentials : "same-origin"
    }

    fetch("/user/respones2", init)
    .then(response => {
        if(response.status === 200){
          return response.json()
        } else {
          console.log(response.statusText);
        }
    })
    .then(jsonData => {
        json = jsonData['msg']

        li = document.querySelector("#id")
        a = document.createElement("li")
        a.setAttribute("id", "new")
        a.innerText= json
        li.appendChild(a)
    })
    //console.log(response)
}
