/*
function decode (input) {
    keyStr : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    var output = "";
    var chr1, chr2, chr3;
    var enc1, enc2, enc3, enc4;
    var i = 0;
    input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    while (i < input.length) {
        enc1 = this.keyStr.indexOf(input.charAt(i++));
        enc2 = this.keyStr.indexOf(input.charAt(i++));
        enc3 = this.keyStr.indexOf(input.charAt(i++));
        enc4 = this.keyStr.indexOf(input.charAt(i++));
        chr1 = (enc1 << 2) | (enc2 >> 4);
        chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
        chr3 = ((enc3 & 3) << 6) | enc4;
        output = output + String.fromCharCode(chr1);
        if (enc3 != 64) {
            output = output + String.fromCharCode(chr2);
        }
        if (enc4 != 64) {
            output = output + String.fromCharCode(chr3);
        }
    }
    output = utf8_decode(output);
    return output;
}




/*
decode : function (input) {

}


function utf_decode(utftext){
    var string = "";
    var i = 0;
    var c = c1 = c2 = 0;

    while ( i < utftext.length ) {

        c = utftext.charCodeAt(i);

        if (c < 128) {
            string += String.fromCharCode(c);
            i++;
        }
        else if((c > 191) && (c < 224)) {
            c2 = utftext.charCodeAt(i+1);
            string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
            i += 2;
        }
        else {
            c2 = utftext.charCodeAt(i+1);
            c3 = utftext.charCodeAt(i+2);
            string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
            i += 3;
        }
    }
    return string;
}

/*
// private method for UTF-8 decoding
_utf8_decode : function (utftext) {
}
*/


function base64_decode (data) {
  // http://kevin.vanzonneveld.net
  // +   original by: Tyler Akins (http://rumkin.com)
  // +   improved by: Thunder.m
  // +      input by: Aman Gupta
  // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  // +   bugfixed by: Onno Marsman
  // +   bugfixed by: Pellentesque Malesuada
  // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  // +      input by: Brett Zamir (http://brett-zamir.me)
  // +   bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  // *     example 1: base64_decode('S2V2aW4gdmFuIFpvbm5ldmVsZA==');
  // *     returns 1: 'Kevin van Zonneveld'
  // mozilla has this native
  // - but breaks in 2.0.0.12!
  //if (typeof this.window['atob'] === 'function') {
  //    return atob(data);
  //}
  var b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var o1, o2, o3, h1, h2, h3, h4, bits, i = 0,
    ac = 0,
    dec = "",
    tmp_arr = [];

  if (!data) {
    return data;
  }

  data += '';

  do { // unpack four hexets into three octets using index points in b64
    h1 = b64.indexOf(data.charAt(i++));
    h2 = b64.indexOf(data.charAt(i++));
    h3 = b64.indexOf(data.charAt(i++));
    h4 = b64.indexOf(data.charAt(i++));

    bits = h1 << 18 | h2 << 12 | h3 << 6 | h4;

    o1 = bits >> 16 & 0xff;
    o2 = bits >> 8 & 0xff;
    o3 = bits & 0xff;

    if (h3 == 64) {
      tmp_arr[ac++] = String.fromCharCode(o1);
    } else if (h4 == 64) {
      tmp_arr[ac++] = String.fromCharCode(o1, o2);
    } else {
      tmp_arr[ac++] = String.fromCharCode(o1, o2, o3);
    }
  } while (i < data.length);

  dec = tmp_arr.join('');

  return dec;
}

function save() {
    var canvas1 = $("#canvas1")[0];
    var ctx1 = canvas1.getContext('2d');
    dataURL1 = canvas1.toDataURL();
    //$("#imagensita1").attr('src',dataURL1);

    var canvas2 = $("#canvas2")[0];
    var ctx2 = canvas2.getContext('2d');
    dataURL2 = canvas2.toDataURL();

    //$("#imagensita2").attr('src',dataURL2);

    var canvas3 = $("#canvas3")[0];
    var ctx3 = canvas3.getContext('2d');
    dataURL3 = canvas3.toDataURL();
    //$("#imagensita3").attr('src',canvas3.toDataURL());

    var canvas4 = $("#canvas4")[0];
    var ctx4 = canvas4.getContext('2d');
    dataURL4 = canvas4.toDataURL();
    //$("#imagensita4").attr('src',canvas4.toDataURL());

    var canvas5 = $("#canvas5")[0];
    var ctx5 = canvas5.getContext('2d');
    dataURL5 = canvas5.toDataURL();
    //$("#imagensita5").attr('src',canvas5.toDataURL());
    
    var canvas6 = $("#canvas6")[0];
    var ctx6 = canvas6.getContext('2d');
    dataURL6 = canvas6.toDataURL();
    //$("#imagensita6").attr('src',canvas6.toDataURL());
    var idpregunta = $('input#idpregunta').val()

    //$('form#formId').attr((this.encoding ? 'encoding' : 'enctype') , 'multipart/form-data');
    datadecoded = base64_decode(dataURL1);
    $.ajax({
        type: "POST",
        url: "/regiter_respuesta_agilidad/",
        data: {'imagen1': datadecoded,'idpregunta':idpregunta}
        //$("#formId").submit();
        

    });
    return data;
}
        function empezar(e){
            e.dataTransfer.effectAllowed = 'move';
            e.dataTransfer.setData("Data", e.target.getAttribute('id'));
            e.dataTransfer.setDragImage(e.target, 0, 0);
            return true;
        }

        function enter(e){
            return true;
        }

        function over(e){
            var esarrastrable = e.dataTransfer.getData("Data");
            var id = e.target.getAttribute('id');
            return false;
        }

        var cont1 = 1;
        function drop1(e){
            context = e.target.getContext('2d');
            var esarrastrable = e.dataTransfer.getData("Data");
            var base_image = document.getElementById(esarrastrable);
            if(cont1 == 1){
                context.drawImage(base_image, 10, 10, 60, 60);
                e.stopPropagation();
            }
            else if(cont1 == 2){
                    context.drawImage(base_image, 90, 15, 60, 60);
                    e.stopPropagation();
            }
            else if(cont1 == 3){
                    context.drawImage(base_image, 170, 12, 60, 60);
                    e.stopPropagation();
                }
            else if(cont1 == 4){
                    context.drawImage(base_image, 10, 90, 60, 60);
                    e.stopPropagation();
                }
            else if(cont1 == 5){
                    context.drawImage(base_image, 100, 95, 60, 60);
                    e.stopPropagation();
                }
            else if(cont1 == 6){
                    context.drawImage(base_image, 160, 92, 60, 60);
                    e.stopPropagation();
                }
            else if(cont1 > 6){
                    alert("demasiadas imagenes");
                }
            cont1 += 1
            return false;
        }

        var cont2 = 1;
        function drop2(e){
            context = e.target.getContext('2d');
            var esarrastrable = e.dataTransfer.getData("Data");
            var base_image = document.getElementById(esarrastrable);
            if(cont2 == 1){
                context.drawImage(base_image, 10, 10, 60, 60);
                e.stopPropagation();
            }
            else if(cont2 == 2){
                    context.drawImage(base_image, 90, 15, 60, 60);
                    e.stopPropagation();
            }
            else if(cont2 == 3){
                    context.drawImage(base_image, 170, 12, 60, 60);
                    e.stopPropagation();
                }
            else if(cont2 == 4){
                    context.drawImage(base_image, 10, 90, 60, 60);
                    e.stopPropagation();
                }
            else if(cont2 == 5){
                    context.drawImage(base_image, 100, 95, 60, 60);
                    e.stopPropagation();
                }
            else if(cont2 == 6){
                    context.drawImage(base_image, 160, 92, 60, 60);
                    e.stopPropagation();
                }
            else if(cont2 > 6){
                    alert("demasiadas imagenes");
                }
            cont2 += 1
            return false;
        }
        var cont3 = 1;
        function drop3(e){
            context = e.target.getContext('2d');
            var esarrastrable = e.dataTransfer.getData("Data");
            var base_image = document.getElementById(esarrastrable);
            if(cont3 == 1){
                context.drawImage(base_image, 10, 10, 60, 60);
                e.stopPropagation();
            }
            else if(cont3 == 2){
                    context.drawImage(base_image, 90, 15, 60, 60);
                    e.stopPropagation();
            }
            else if(cont3 == 3){
                    context.drawImage(base_image, 170, 12, 60, 60);
                    e.stopPropagation();
                }
            else if(cont3 == 4){
                    context.drawImage(base_image, 10, 90, 60, 60);
                    e.stopPropagation();
                }
            else if(cont3 == 5){
                    context.drawImage(base_image, 100, 95, 60, 60);
                    e.stopPropagation();
                }
            else if(cont3 == 6){
                    context.drawImage(base_image, 160, 92, 60, 60);
                    e.stopPropagation();
                }
            else if(cont3 > 6){
                    alert("demasiadas imagenes");
                }
            cont3 += 1
            return false;
        }
        var cont4 = 1;
        function drop4(e){
            context = e.target.getContext('2d');
            var esarrastrable = e.dataTransfer.getData("Data");
            var base_image = document.getElementById(esarrastrable);
            if(cont4 == 1){
                context.drawImage(base_image, 10, 10, 60, 60);
                e.stopPropagation();
            }
            else if(cont4 == 2){
                    context.drawImage(base_image, 90, 15, 60, 60);
                    e.stopPropagation();
            }
            else if(cont4 == 3){
                    context.drawImage(base_image, 170, 12, 60, 60);
                    e.stopPropagation();
                }
            else if(cont4 == 4){
                    context.drawImage(base_image, 10, 90, 60, 60);
                    e.stopPropagation();
                }
            else if(cont4 == 5){
                    context.drawImage(base_image, 100, 95, 60, 60);
                    e.stopPropagation();
                }
            else if(cont4 == 6){
                    context.drawImage(base_image, 160, 92, 60, 60);
                    e.stopPropagation();
                }
            else if(cont4 > 6){
                    alert("demasiadas imagenes");
                }
            cont4 += 1
            return false;
        }

        var cont5 = 1;
        function drop5(e){
            context = e.target.getContext('2d');
            var esarrastrable = e.dataTransfer.getData("Data");
            var base_image = document.getElementById(esarrastrable);
            if(cont5 == 1){
                context.drawImage(base_image, 10, 10, 60, 60);
                e.stopPropagation();
            }
            else if(cont5 == 2){
                    context.drawImage(base_image, 90, 15, 60, 60);
                    e.stopPropagation();
            }
            else if(cont5 == 3){
                    context.drawImage(base_image, 170, 12, 60, 60);
                    e.stopPropagation();
                }
            else if(cont5 == 4){
                    context.drawImage(base_image, 10, 90, 60, 60);
                    e.stopPropagation();
                }
            else if(cont5 == 5){
                    context.drawImage(base_image, 100, 95, 60, 60);
                    e.stopPropagation();
                }
            else if(cont5 == 6){
                    context.drawImage(base_image, 160, 92, 60, 60);
                    e.stopPropagation();
                }
            else if(cont5 > 6){
                    alert("demasiadas imagenes");
                }
            cont5 += 1
            return false;
        }
        var cont6 = 1;
        function drop6(e){
            context = e.target.getContext('2d');
            var esarrastrable = e.dataTransfer.getData("Data");
            var base_image = document.getElementById(esarrastrable);
            if(cont6 == 1){
                context.drawImage(base_image, 10, 10, 60, 60);
                e.stopPropagation();
            }
            else if(cont6 == 2){
                    context.drawImage(base_image, 90, 15, 60, 60);
                    e.stopPropagation();
            }
            else if(cont6 == 3){
                    context.drawImage(base_image, 170, 12, 60, 60);
                    e.stopPropagation();
                }
            else if(cont6 == 4){
                    context.drawImage(base_image, 10, 90, 60, 60);
                    e.stopPropagation();
                }
            else if(cont6 == 5){
                    context.drawImage(base_image, 100, 95, 60, 60);
                    e.stopPropagation();
                }
            else if(cont6 == 6){
                    context.drawImage(base_image, 160, 92, 60, 60);
                    e.stopPropagation();
                }
            else if(cont6 > 6){
                    alert("demasiadas imagenes");
                }
            cont6 += 1
            return false;
        }

        function end(e){
            e.dataTransfer.clearData("Data");
            return true;
        }