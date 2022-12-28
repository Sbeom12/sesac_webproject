function enterFunc(event, id, focus){
    data = document.querySelector(`#${id}`)
    //next = document.querySelector(`#${focus}`)
    
    if(event.code=="Enter"){
        console.log(data.value)
        if(data.value.length==0){
            event.preventDefault()
            Swal.fire({
                icon: 'warning',
                text: '댓글을 작성해주세요.'
            });
        }
        else{
            event.preventDefault()
            document.querySelector(`#${focus}`).focus() // enter 누르면 다음으로 focus 이동
        }
      }
    }
  
function btnClick(event){
  cmtCntnt = document.querySelector("#cmtCntnt")

  if(cmtCntnt.value.length==0){
      event.preventDefault()
      Swal.fire({
        icon: 'warning',
        text: '댓글을 작성해주세요.'
    });
    }
}