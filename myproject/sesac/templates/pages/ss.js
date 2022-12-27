const likebtn = document.querySelectorAll(".likebtn");

// url?pstId=1&type=int&post=1
likebtn.forEach((btn) => {
  btn.addEventListener("click", function update() {
    let data = btn.value.split(" ");
    let type = data[1];
    let pstId = data[0];
    let post = "1";
    data = `${type}/${pstId}/${post}`;
    console.log(pstId, type, post, data);
    let baseUrl = "http://127.0.0.1:5000/post/like";
    let url = `${baseUrl}?data=${data}`;
    // let url = `${baseUrl}?pstId=${pstId}?type=${type}?post=${post}`;
    // let url = `${baseUrl}?pstId=${pstId}?type=${type}?post=${post}`;
    // let url = `${baseUrl}?type=${type}`;
    // let url = `${baseUrl}?pstId=${pstId}`;
    //     fetch(
    //       "http://" +
    //         document.domain +
    //         ":" +
    //         location.port +
    //         "/like/" +
    //         pstId +
    //         "/" +
    //         type +
    //         "/" +
    //         post +
    //         "/"
    //     )
    //       .then((response) => response.json())
    //       .then((data) => console.log(data));
    //   });
    fetch(url);
  });
});
