document.querySelector("#toggle_header").addEventListener('click', function(){
    const headerClass = document.querySelector('header').getAttribute('class');
    if(headerClass === "red"){
        document.querySelector('header').setAttribute("class","green");
    }
    else{
        document.querySelector('header').setAttribute("class","red");
    }
});