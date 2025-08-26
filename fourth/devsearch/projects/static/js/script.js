let searchForm = document.getElementById('search');
let pageLinks = document.querySelectorAll(".page-link");

if(searchForm){
for(let i=0; pageLinks.length > i; i++){
  pageLinks[i].addEventListener("click", function(event){
    event.preventDefault();

    let page = this.dataset.page;

    searchForm.innerHTML += `<input type='hidden' value=${page} name='page'>`;

    searchForm.submit();
  });
}
}

