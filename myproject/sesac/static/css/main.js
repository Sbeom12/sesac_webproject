// 햄버거 버튼 누르면 리스트 출력
const toggleBtn = document.querySelector('.navbar-togglebtn');
const menu = document.querySelector('.menu-list')

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active'); 
});


// 하단 탑버튼 누르면 스크롤 탑으로 이동
$(".btn_top").click(function() {
    $('html,body').scrollTop(0);
});
