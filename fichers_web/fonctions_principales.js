// l'arriere plan
function bg_color(){
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)";
    if (document.body.style.background == color1){
        document.body.style.backgroundColor = color2;
    }else{
        document.body.style.background = color1;
    }
}

// ouvrir et fermer la partie 1
function rap_ouv_I() {
    let object = document.getElementsByClassName("somm1_2");
    for (let i = 0; i < object.length; i++) {
        let currentDisplay = window.getComputedStyle(object[i]).display;
        if (currentDisplay === "none") {
            object[i].style.display = "block";
        } else {
            object[i].style.display = "none";
            console.log("eee");
        }
    }
}


// asombrir a la navigation rapide
const box = document.getElementById("panneau_droite");

box.addEventListener("mouseenter", () => {
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)";
    var color3 = "rgb(0, 0, 1)";
    var color4 = "rgb(0, 0, 0)";
    if (document.body.style.background == color1){
        document.body.style.background = color3;
    }else{
        document.body.style.background = color4;
    }
    document.getElementById("la_page").style.opacity = "0.1";
});

box.addEventListener("mouseleave", () => {
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)";
    var color3 = "rgb(0, 0, 1)";
    var color4 = "rgb(0, 0, 0)";
    if (document.body.style.background == color3){
        document.body.style.background = color1;
    }else{
        document.body.style.background = color2;
    }
    document.getElementById("la_page").style.opacity = "1";
});