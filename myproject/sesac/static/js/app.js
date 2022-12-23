let data = [
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
  { idx: 1, title: "안녕하세요", cnt: 0 },
];
function update() {}

function display_table() {
  let rows = data.slice(0, 10);

  let table = document.querySelector("table");
  rows.forEach((row) => {
    // console.log(row);
    let tr = document.createElement("tr");
    let idx = document.createElement("idx");
    let title = document.createElement("title");
    let cnt = document.createElement("cnt");
    idx.innerHTML = row.idx;
    title.innerHTML = row.title;
    cnt.innerHTML = row.cnt;
    html =
      '<tr><th scope="col">날짜</th><th scope="col">이름</th><th scope="col">성별</th></tr>';

    console.log(html);
    // table.insertAdjacentHTML("beforeend", tr);
    // return tr;
  });
}
display_table();
