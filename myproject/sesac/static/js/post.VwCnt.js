function lnkClick(pstId){
  /* onclick으로 pstId 받아오기 */
  console.log("pstId:", pstId)

  /* pstId 저장해서 flask("/main/vw")에 비동기로 data(pstId) 보내기 */
  myData={
    "pstId":pstId
  }

  init = {
    method: "POST",
    body: JSON.stringify(myData),
    headers: {
      "Content-Type": "application/json"
    },
    credentials : "same-origin"
  } 

  fetch("/main/vw", init)
  .then(response => {
      if(response.status === 200){
        console.log("여기 여기 여기 여기 여기", response)
        return response.json()
      } 
      else {
        console.log(response.statusText);
      }
  })
  .then(jsonData => {
      pstIdReturn = jsonData['msg']
      //console.log(pstIdReturn)
  })
  .catch((error) => console.log("error:", error));
  
  /* page 이동 */
  location.href =`/post/pstId=${pstId}`  // pstId가 어떻게 전달이 되는거지,,?
}