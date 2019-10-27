function click_img(index) {
    var links = 3;
    for (var i = 1; i <= links; i++) {
        var menu = document.getElementById("species-img" + i);
        var table=document.getElementById("table"+i);
        if (menu.className == "on") {
            menu.className = "off";
            table.className="database-content2";
            break;
        }
    }
    var a=document.getElementById("species-img"+index);
    a.className="on";
    var b=document.getElementById("table"+index);
    b.className="database-content1";
}

