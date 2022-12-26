function enterFunc(event, id, focus) {
  data = document.querySelector(`#${id}`);
  if (event.code == "Enter") {
    console.log(data.value) 
    if(data.value.length==0){
      event.preventDefault()
      alert(`${id}은 필수 입력 항목입니다.`)
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
        event.preventDefault()
    }
  }
}   

function inputClick(){
//console.log("클릭 클릭")
li = document.querySelector("#remv")
console.log(li)
li.remove()
}   
