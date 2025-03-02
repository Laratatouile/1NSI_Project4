function bg_color(){
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)"
    if (document.body.style.background == color1){
        document.body.style.backgroundColor = color2;
    }else{
        document.body.style.background = color1;
    }
}