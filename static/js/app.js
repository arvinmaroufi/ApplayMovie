document.addEventListener("DOMContentLoaded", (e) => {
  let preload = document.getElementById("preload");
  let content = document.getElementById("content");

  preload.style.display = "none";
  content.style.display = "block";
});

let theme_option = document.getElementById("theme-option");
let change_options_btn = document.querySelector(".change-setting");
let changeToggle = true;

change_options_btn.addEventListener("click", (e) => {
  e.preventDefault();
  if (changeToggle) {
    theme_option.style.transform = "translate(0,-50%)";
    theme_option.classList.add("mobile");
    changeToggle = false;
  } else {
    theme_option.style.transform = "translate(-400px,-50%)";
    changeToggle = true;
  }
});

document
  .querySelector("#theme-option .close")
  .addEventListener("click", (e) => {
    e.preventDefault();
    theme_option.style.transform = "translate(-400px,-50%)";
    changeToggle = true;
    theme_option.classList.remove("mobile");
  });

if (document.getElementById("copyLink")) {
  var copyLink = document.getElementById("copyLink");
  if (document.getElementsByClassName("embedlink")) {
    var copyEmbed = document.getElementsByClassName("embedlink");
  }
  if ([copyLink, ...copyEmbed]) {
    var copyAll = [copyLink, ...copyEmbed];
    copyAll.map((item) => {
      item.addEventListener("click", (e) => e.preventDefault());
      new ClipboardJS(item);
    });
  }
}

if (document.querySelector(".comment-form")) {
  var form_send = document.querySelector(".comment-form");
  if (
    form_send.querySelectorAll(
      "input[type=text] , input[type=email] , textarea"
    )
  ) {
    var commentInput = form_send.querySelectorAll(
      "input[type=text] , input[type=email] , textarea"
    );
  }

  if (commentInput) {
    commentInput.forEach((item) => {
      inputOnBlur(item);
      inputOnInput(item);
    });
  }

  if (form_send) {
    form_send.addEventListener("submit", (e) => {
      e.preventDefault();

      if (
        commentInput[0].value != "" &&
        commentInput[1].value != "" &&
        commentInput[2].value != ""
      ) {
        let comment = document.createElement("div");
        comment.classList.add("col-md-12");
        comment.innerHTML = `
              <div class="card bg-info-lighten card-comment">
                  <div class="card-header d-flex justify-content-between mb-0">
                      <div class="d-flex align-items-center justify-content-center">
                          <h5 class="text-dark font-weight-bolder">${commentInput[0].value}</h5>
                          <span class="card-subtitle text-primary ml-2">مهر 1399 در 12</span>
                      </div>
                      <div class="comment-more">
                          <a href="#" class="dropdown" data-toggle="dropdown">
                              <i class="far fa-ellipsis-v"></i>
                              <div class="dropdown-menu">
                                  <li>
                                      <a href="#" class="dropdown-item">
                                          <i class="far fa-flag"></i>
                                          <span class="ml-1">گزارش تخلف</span>
                                      </a>
                                  </li>
                              </div>
                          </a>
                      </div>
                  </div>
                  <div class="card-body pb-0 pt-0">
                      <p>${commentInput[2].value}</p>
                  </div>
                  <div class="card-footer d-flex justify-content-end mb-1 mr-2 add-emoji">
                      <a href="#" class="btn btn-outline-danger btn-sm mr-1 text-danger dislike">
                          <span>0</span>
                          <i class="fas fa-thumbs-down"></i>
                      </a>
                      <a href="#" class="btn btn-outline-primary btn-sm like">
                          <span>0</span>
                          <i class="fas fa-thumbs-up"></i>
                      </a>
                  </div>
              </div>
              `;
        document.querySelector("#comments_container .row").appendChild(comment);
        commentInput[0].value = "";
        commentInput[1].value = "";
        commentInput[2].value = "";
      } else {
        commentInput[0].classList.add("is-invalid");
        commentInput[1].classList.add("is-invalid");
        commentInput[2].classList.add("is-invalid");
      }
    });
  }
}

function inputOnBlur(input) {
  input.addEventListener("blur", (e) => {
    if (input.value == "") {
      input.classList.add("is-invalid");
    } else {
      input.classList.remove("is-invalid");
    }
  });
}

function inputOnInput(input) {
  input.addEventListener("input", (e) => {
    if (input.value == "") {
      input.classList.add("is-invalid");
    } else {
      input.classList.remove("is-invalid");
    }
  });
}

// Recommended post like
let like_post = document.querySelectorAll('.recommend_post_like');
like_post.forEach(item => {
  let value = true;
  item.addEventListener('click',(e)=>{
    e.preventDefault();
    if(value){
      item.innerHTML = '';
      item.innerHTML = '<i class="fas fa-heart" style="color:#ff5252"></i>' ;
      value = !value;
      console.log(value)
    } else{
      item.innerHTML = '';
      item.innerHTML = '<i class="far fa-heart"></i>';
      value = !value;
    }
  })
})

// Theme Option
let inputTheme = document.querySelectorAll(".layout-name");
inputTheme.forEach((item) => {
  if (item.checked) {
    var value = item.getAttribute("theme");
    document.body.classList.add(`${value}-layout`);
    if (document.querySelector(".navbar")) {
      document.querySelector(".navbar").classList.add(`navbar-${value}`);
    }
  }
  item.addEventListener("change", (e) => {
    if (item.checked) {
      var newValue = item.getAttribute("theme");
      document.body.className = "";
      document.body.classList.add(`${newValue}-layout`);
      if (document.querySelectorAll(".navbar , #footer")) {
        let customChange = document.querySelectorAll(".navbar , #footer , #sub_footer , #social_media");
        if (newValue == "light") {
          customChange[0].className = "";
          customChange[0].classList.add(
            "navbar",
            "navbar-expand-lg",
            "navbar-light"
          );
          customChange[1].className = '',
          customChange[1].classList.add('bg-white');
          customChange[2].className = '',
          customChange[2].classList.add('bg-white');
          customChange[3].className = '',
          customChange[3].classList.add('bg-white');
        } else {
          customChange[0].className = "";
          customChange[0].classList.add(
            "navbar",
            "navbar-expand-lg",
            "navbar-dark"
          );
          customChange[1].className= '';
          customChange[1].classList.add('bg-dark');
          customChange[2].className = '',
          customChange[2].classList.add('bg-dark');
          customChange[3].className = '',
          customChange[3].classList.add('bg-dark');
        }
      }
    }
  });
});

// ScrollTop
if (document.querySelector(".goTop")) {
  var goTopBtn = document.querySelector(".goTop");
  goTopBtn.addEventListener("click", (e) => {
    scrollTop(0);
    ShowandHideScrollTop();
  });

  function scrollTop(scroll) {
    document.documentElement.scrollTop = scroll;
  }

  function ShowandHideScrollTop() {
    let scrollShowBtn = document.querySelector("input[name=scrollTopShow]");
    if (scrollShowBtn.checked) {
      goTopBtn.style.display = "flex";
    } else {
      goTopBtn.style.display = "none";
    }
    scrollShowBtn.addEventListener("change", (e) => {
      if (scrollShowBtn.checked) {
        goTopBtn.style.display = "flex";
      } else {
        goTopBtn.style.display = "none";
      }
    });
  }

  ShowandHideScrollTop();
}

// Cards box shadow
let cardShadowBtn = document.getElementById("card-shadow");
cardShadowBtn.addEventListener("click", (e) => {
  document.body.classList.toggle("no-card-shadow");
});

// Fullscreen website
let fullScreenBtn = document.getElementById("fullscreen-option");
fullScreenBtn.addEventListener("click", (e) => {
  if (
    document.fullscreenElement ||
    document.webkitFullscreenElement ||
    document.mozFullScreenElement ||
    document.msFullscreenElement
  ) {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    }
  } else {
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen();
    } else if (document.documentElement.webkitRequestFullscreen) {
      document.documentElement.webkitRequestFullscreen();
    } else if (document.documentElement.mozRequestFullScreen) {
      document.documentElement.mozRequestFullScreen();
    } else if (document.documentElement.msRequestFullscreen) {
      document.documentElement.msRequestFullscreen();
    }
  }
});

// Footer option
let footerOption = document.querySelectorAll("input[name=footer-option]");
footerOption.forEach((item) => {
  item.addEventListener("change", (e) => {
    if (document.getElementById("footer")) {
      var footer = document.getElementById("footer");
    }
    let value = item.getAttribute("footer");
    if (value == "hidden") {
      footer.classList.remove("static");
      footer.classList.remove("sticky");
      footer.classList.add("hidden");
    } else if (value == "static") {
      footer.classList.add("static");
      footer.classList.remove("sticky");
      footer.classList.remove("hidden");
    } else if (value == "sticky") {
      footer.classList.remove("static");
      footer.classList.add("sticky");
      footer.classList.remove("hidden");
    } else {
      footer.classList.add("static");
    }
  });
});


