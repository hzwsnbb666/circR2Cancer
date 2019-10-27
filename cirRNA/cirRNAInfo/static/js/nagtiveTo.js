
/*获取到Url里面的参数*/

(function ($) {

  $.getUrlParam = function (name) {

   var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");

   var r = window.location.search.substr(1).match(reg);

   if (r != null) return unescape(r[2]); return null;

  }

 })(jQuery);

function clickTo() {
    var label=$.getUrlParam('name');
    alert(label);
    if(label == 'index'){
        document.getElementById("label1").style.color="blue";
    }
    else if(label == 'browse'){
        document.getElementById("label2").style.color="blue";
    }
    else if(label == 'search'){
        document.getElementById("label3").style.color="blue";
    }
    else if(label == 'download'){
        document.getElementById("label4").style.color="blue";
    }
    else if (label == 'about'){
        document.getElementById("label5").style.color="blue";
    }
}