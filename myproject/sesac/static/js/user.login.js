function enterFunc(event, id, focus) {
  data = document.querySelector(`#${id}`);
  if (event.code == "Enter") {
    console.log(data.value) 
    
    if(data.value.length==0){
      event.preventDefault()
      Swal.fire({
        icon: 'warning',
        text: "내용을 입력해주세요",
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
  clas = document.querySelectorAll(".clas")
  for(i=0; i<=2; i++){
    if(clas[i].value.length==0){
      Swal.fire({
        icon: 'error',
        text: "내용을 입력해주세요",
      });
      event.preventDefault()
    }
  }
} 
function inputClick(){
li = document.querySelector("#remv")
console.log(li)
li.remove()
}   
