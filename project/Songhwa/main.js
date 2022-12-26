// 햄버거 버튼 누르면 리스트 출력

const toggleBtn = document.querySelector('.navbar-togglebtn');
const menu = document.querySelector('.menu-list')
const menuitem = document.querySelector('.menu-item')

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active'); 
    $('.overlay').fadeIn();
});

$('.overlay').on('click', function () {
    $(menu).removeClass('active');
    $('.overlay').fadeOut();
});


// -------------------------------------

// 햄버거 애니메이션

var burger = $('.navbar-togglebtn');

burger.each(function(index){
var $this = $(this);

$this.on('click', function(e){
    e.preventDefault();
    $(this).toggleClass('active-' + (index+1));
})
});


// --------------------------------------

// 햄버거 드롭다운 애니메이션



// --------------------------------------

history.scrollRestoration = "manual";

// --------------------------------------

// 스크롤 여부 따라서 메뉴 업다운

var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('header').outerHeight();

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();
    
    // 델타값보다 더 스크롤 했을 때
    if(Math.abs(lastScrollTop - st) <= delta)
        return;
    
    // 스크롤 따라서 숨겼다가 나타나게 함
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        $('header').removeClass('nav-down').addClass('nav-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('header').removeClass('nav-up').addClass('nav-down');
        }
    }
    
    lastScrollTop = st;
}



// --------------------------------------

// 하단 탑버튼 누르면 스크롤 탑으로 이동

$(".btn_top").click(function() {
    $('html,body').scrollTop(0);
});


// --------------------------------------

// 마이페이지

const articleBtn = document.querySelector('.article-btn');
const myarticle = document.querySelector('.myarticle-list')

articleBtn.addEventListener('click', () => {
    myarticle.classList.toggle('active'); 
});

$('.overlay').on('click', function () {
    $(myarticle).removeClass('active');
});


const commentBtn = document.querySelector('.comment-btn');
const mycomment = document.querySelector('.mycomment-list')

commentBtn.addEventListener('click', () => {
    mycomment.classList.toggle('active'); 
});

$('.overlay').on('click', function () {
    $(mycomment).removeClass('active');
});


// 퀵메뉴

$(document).ready(function(){
    var currentPosition = parseInt($(".quickmenu").css("top"));
    $(window).scroll(function() {
    var position = $(window).scrollTop(); 
    $(".quickmenu").stop().animate({"top":position+currentPosition+"px"},1000);
    });
});