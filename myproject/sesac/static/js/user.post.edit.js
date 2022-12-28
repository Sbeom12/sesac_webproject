function enterFunc(event, id, focus){
    data = document.querySelector(`#${id}`)
    
    if(event.code=="Enter"){
        console.log(data.value)
        if(data.value.length==0){
            event.preventDefault()
            Swal.fire({
                icon: 'waring',
                text: `${id}은 필수 입력 항목입니다.`,
            });
        }
        else{
            event.preventDefault()
            document.querySelector(`#${focus}`).focus() // enter 누르면 다음으로 focus 이동
        }
    }
}
function btnClick(event){
    i=0
    clas = document.querySelectorAll(".form-control")
    for(i=0; i<=6; i++){
    if(clas[i].value.length==0){
        Swal.fire({
            icon: 'error',
            text: "내용을 전부 입력해주세요.",
        });
        event.preventDefault()
        }
    }
}

