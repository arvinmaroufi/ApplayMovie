// Advanced search result
let searchResultInput = document.getElementById('searchAd');
let showResult = document.getElementById('searchBoxResult');


searchResultInput.addEventListener('focus',(e)=>{
        showResult.classList.add('show');
})
searchResultInput.addEventListener('focusout',(e)=>{
    showResult.classList.remove('show');
    
})

let sideMain = document.querySelector('.sidebar-app');
let sideBtnShowe = document.querySelectorAll('.sidebar-app-show');
sideBtnShowe.forEach(item => {
    item.addEventListener('click',(e)=>{
        e.preventDefault();
        sideMain.style.transform = "translate(3%,0)";
        sideMain.classList.add('mobile');
    })
});

let sideBtnCloser = sideMain.querySelector('.sidebar-closer');
sideBtnCloser.addEventListener('click',(e)=>{
    sideMain.style.transform = "translate(-1000px,0)";
    sideMain.classList.remove('mobile');
})


let searchAS = document.querySelectorAll('a[search]');
searchAS.forEach(item => {
    item.addEventListener('click',(e)=>{
        e.preventDefault();
        searchResultInput.value += item.getAttribute('search');
        searchResultInput.focus();
    })
})

