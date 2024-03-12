const pagetop_btn = document.querySelector(".pagetop");

// .pagetopをクリックしたら
pagetop_btn.addEventListener("click", scroll_top);

// ページ上部へスムーズに移動
function scroll_top() {
  window.scroll({ top: 0, behavior: "smooth" });
}

// スクロールされたら表示
window.addEventListener("scroll", scroll_event);
function scroll_event() {
  if (window.scrollY > 100) {
    pagetop_btn.style.opacity = "1";
  } else if (window.scrollY < 100) {
    pagetop_btn.style.opacity = "0";
  }
}