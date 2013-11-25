function dataURLtoBlob(dataURL) {
    var binary = atob(dataURL.split(',')[1]);
    var array = [];
    for(var i = 0; i < binary.length; i++) {
        array.push(binary.charCodeAt(i));
    }
    return new Blob([new Uint8Array(array)], {type: 'image/png'});
}

function getCheckedRadioValue(radioGroupName) {
    var rads = document.getElementsByName(radioGroupName),
    i;
    for (i=0; i < rads.length; i++)
        if (rads[i].checked)
            return rads[i].value;
    return null;
}


function save(tipo_imagen) {
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

    var idpregunta = $('input#idpregunta').val();
    var select = document.getElementById("select-agility");
    var grado = select.options[select.selectedIndex].value;
    var pregunta = document.getElementById("textarea-agility").value;
    var imagen_edit_type = document.getElementById("imagen_edit_type");

    var file1 = dataURLtoBlob(dataURL1);
    var file2 = dataURLtoBlob(dataURL2);
    var file3 = dataURLtoBlob(dataURL3);
    var file4 = dataURLtoBlob(dataURL4);
    var file5 = dataURLtoBlob(dataURL5);
    var file6 = dataURLtoBlob(dataURL6);
    var agilidad = getCheckedRadioValue("agilidad");
    var fd = new FormData();
    fd.append("imagen1", file1);
    fd.append("imagen2", file2);
    fd.append("imagen3", file3);
    fd.append("imagen4", file4);
    fd.append("imagen5", file5);
    fd.append("imagen6", file6);
    fd.append("idpregunta", idpregunta);
    fd.append("agilidad", agilidad);
    fd.append("grado", grado);
    fd.append("pregunta", pregunta);

    var edit = new FormData();
    edit.append("imagen1", file1);
    edit.append("imagen2", file2);
    edit.append("imagen3", file3);
    edit.append("imagen4", file4);
    edit.append("imagen5", file5);
    edit.append("imagen6", file6);
    edit.append("idpregunta", idpregunta);
    edit.append("agilidad", agilidad);
    edit.append("imagen_edit_type", imagen_edit_type);

    if(cont1<6 || cont2<6 || cont3<6 || cont4<6 || cont5<6 || cont6<6){
        alert("cada respuesta debe contener 6 imagenes");
    }else if(pregunta == ""){
        alert("la pregunta no puede estar vacia");
    } else{
        if(tipo_imagen == 1){
            $.ajax({
                type: "POST",
                url: "/register_question_crafs_agility/",
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                data: fd,
                success: function(){
                    window.location = '/question_success_agility/';
                }
                 //$("#formId").submit();
            });
        }else if(tipo_imagen == 2){
            $.ajax({
                type: "POST",
                url: "/register_question_geometrics_agility/",
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                data: fd,
                success: function(){
                    window.location = '/question_success_agility/';
                }
                //$("#formId").submit();
            });
        }else if(tipo_imagen == 3){
            $.ajax({
                type: "POST",
                url: "/register_question_objects_agility/",
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                data: fd,
                success: function(){
                    window.location = '/question_success_agility/';
                }
                //$("#formId").submit();
            });
        }
    }
}

function save_edit(numero){
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

    var idpregunta = $('input#idpregunta').val();
    var id1 = $('input#id1').val();
    var id2 = $('input#id2').val();
    var id3 = $('input#id3').val();
    var id4 = $('input#id4').val();
    var id5 = $('input#id5').val();
    var id6 = $('input#id6').val();
    var imagen_edit_type = $('input#imagen_edit_type').val();

    var file1 = dataURLtoBlob(dataURL1);
    var file2 = dataURLtoBlob(dataURL2);
    var file3 = dataURLtoBlob(dataURL3);
    var file4 = dataURLtoBlob(dataURL4);
    var file5 = dataURLtoBlob(dataURL5);
    var file6 = dataURLtoBlob(dataURL6);
    var agilidad = getCheckedRadioValue("agilidad");
    var edit = new FormData();
    edit.append("imagen1", file1);
    edit.append("imagen2", file2);
    edit.append("imagen3", file3);
    edit.append("imagen4", file4);
    edit.append("imagen5", file5);
    edit.append("imagen6", file6);
    edit.append("idpregunta", idpregunta);
    edit.append("agilidad", agilidad);
    edit.append("id1", id1);
    edit.append("id2", id2);
    edit.append("id3", id3);
    edit.append("id4", id4);
    edit.append("id5", id5);
    edit.append("id6", id6);
    if(limpio1 == 1 && cont_edit1 < 6 || limpio2 == 1 && cont_edit2 < 6 || limpio3 == 1 && cont_edit3 < 6 || limpio4 == 1 && cont_edit4 < 6 || limpio5 == 1 && cont_edit5 < 6 || limpio6 == 1 && cont_edit6 < 6){
        alert("las respuestas deben tener 6 imagenes");
    }else{
        if(numero == 1){
            $.ajax({
                type: "POST",
                url: "/edit/respuesta/agilidad/dados/",
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                data: edit,
                success: function(){
                    window.location = '/question_success_agility/';
                }
            });
        }else if(numero == 2){
            $.ajax({
                type: "POST",
                url: "/edit/respuesta/agilidad/geometricas/",
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                data: edit,
                success: function(){
                    window.location = '/question_success_agility/';
                }
            });
        }else if(numero == 3){
            $.ajax({
                type: "POST",
                url: "/edit/respuesta/agilidad/objetos/",
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                data: edit,
                success: function(){
                    window.location = '/question_success_agility/';
                }
            });
        }
    }
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

function limpiar1() {
    canvas1 = document.getElementById("canvas1");
    var ctx1 = canvas1.getContext('2d');
    ctx1.clearRect(0, 0, canvas1.width, canvas1.height);
    cont1 = 1;
}

function limpiar2() {
    canvas2 = document.getElementById("canvas2");
    var ctx2 = canvas2.getContext('2d');
    ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
    cont2 = 1;
}

function limpiar3() {
    canvas3 = document.getElementById("canvas3");
    var ctx3 = canvas3.getContext('2d');
    ctx3.clearRect(0, 0, canvas3.width, canvas3.height);
    cont3 = 1;
}

function limpiar4() {
    canvas4 = document.getElementById("canvas4");
    var ctx4 = canvas4.getContext('2d');
    ctx4.clearRect(0, 0, canvas4.width, canvas4.height);
    cont4 = 1;
}

function limpiar5() {
    canvas5 = document.getElementById("canvas5");
    var ctx5 = canvas5.getContext('2d');
    ctx5.clearRect(0, 0, canvas5.width, canvas5.height);
    cont5 = 1;
}

function limpiar6() {
    canvas6 = document.getElementById("canvas6");
    var ctx6 = canvas6.getContext('2d');
    ctx6.clearRect(0, 0, canvas6.width, canvas6.height);
    cont6 = 1;
}

var cont1 = 1;
function drop1(e){
    context = e.target.getContext('2d');
    var esarrastrable = e.dataTransfer.getData("Data");
    var base_image = document.getElementById(esarrastrable);
    if(cont1 == 1){
        context.drawImage(base_image, 18, 7, 80, 60);
        e.stopPropagation();
    }
    else if(cont1 == 2){
            context.drawImage(base_image, 105, 9, 80, 60);
            e.stopPropagation();
    }
    else if(cont1 == 3){
            context.drawImage(base_image, 195, 8, 80, 60);
            e.stopPropagation();
        }
    else if(cont1 == 4){
            context.drawImage(base_image, 15, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont1 == 5){
            context.drawImage(base_image, 105, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont1 == 6){
            context.drawImage(base_image, 195, 82, 80, 60);
            e.stopPropagation();
        }
    else if(cont1 > 6){
            alert("demasiadas imagenes");
        }
    cont1 += 1;
    return false;
}


var cont2 = 1;
function drop2(e){
    context = e.target.getContext('2d');
    var esarrastrable = e.dataTransfer.getData("Data");
    var base_image = document.getElementById(esarrastrable);
    if(cont2 == 1){
        context.drawImage(base_image, 18, 7, 80, 60);
        e.stopPropagation();
    }
    else if(cont2 == 2){
            context.drawImage(base_image, 105, 9, 80, 60);
            e.stopPropagation();
    }
    else if(cont2 == 3){
            context.drawImage(base_image, 195, 8, 80, 60);
            e.stopPropagation();
        }
    else if(cont2 == 4){
            context.drawImage(base_image, 15, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont2 == 5){
            context.drawImage(base_image, 105, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont2 == 6){
            context.drawImage(base_image, 195, 82, 80, 60);
            e.stopPropagation();
        }
    else if(cont2 > 6){
            alert("demasiadas imagenes");
        }
    cont2 += 1;
    return false;
}

var cont3 = 1;
function drop3(e){
    context = e.target.getContext('2d');
    var esarrastrable = e.dataTransfer.getData("Data");
    var base_image = document.getElementById(esarrastrable);
    if(cont3 == 1){
        context.drawImage(base_image, 18, 7, 80, 60);
        e.stopPropagation();
    }
    else if(cont3 == 2){
            context.drawImage(base_image, 105, 9, 80, 60);
            e.stopPropagation();
    }
    else if(cont3 == 3){
            context.drawImage(base_image, 195, 8, 80, 60);
            e.stopPropagation();
        }
    else if(cont3 == 4){
            context.drawImage(base_image, 15, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont3 == 5){
            context.drawImage(base_image, 105, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont3 == 6){
            context.drawImage(base_image, 195, 82, 80, 60);
            e.stopPropagation();
        }
    else if(cont3 > 6){
            alert("demasiadas imagenes");
        }
    cont3 += 1;
    return false;
}

var cont4 = 1;
function drop4(e){
    context = e.target.getContext('2d');
    var esarrastrable = e.dataTransfer.getData("Data");
    var base_image = document.getElementById(esarrastrable);
    if(cont4 == 1){
        context.drawImage(base_image, 18, 7, 80, 60);
        e.stopPropagation();
    }
    else if(cont4 == 2){
            context.drawImage(base_image, 105, 9, 80, 60);
            e.stopPropagation();
    }
    else if(cont4 == 3){
            context.drawImage(base_image, 195, 8, 80, 60);
            e.stopPropagation();
        }
    else if(cont4 == 4){
            context.drawImage(base_image, 15, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont4 == 5){
            context.drawImage(base_image, 105, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont4 == 6){
            context.drawImage(base_image, 195, 82, 80, 60);
            e.stopPropagation();
        }
    else if(cont4 > 6){
            alert("demasiadas imagenes");
        }
    cont4 += 1;
    return false;
}

var cont5 = 1;
function drop5(e){
    context = e.target.getContext('2d');
    var esarrastrable = e.dataTransfer.getData("Data");
    var base_image = document.getElementById(esarrastrable);
    if(cont5 == 1){
        context.drawImage(base_image, 18, 7, 80, 60);
        e.stopPropagation();
    }
    else if(cont5 == 2){
            context.drawImage(base_image, 105, 9, 80, 60);
            e.stopPropagation();
    }
    else if(cont5 == 3){
            context.drawImage(base_image, 195, 8, 80, 60);
            e.stopPropagation();
        }
    else if(cont5 == 4){
            context.drawImage(base_image, 15, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont5 == 5){
            context.drawImage(base_image, 105, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont5 == 6){
            context.drawImage(base_image, 195, 82, 80, 60);
            e.stopPropagation();
        }
    else if(cont5 > 6){
            alert("demasiadas imagenes");
        }
    cont5 += 1;
    return false;
}

var cont6 = 1;
function drop6(e){
    context = e.target.getContext('2d');
    var esarrastrable = e.dataTransfer.getData("Data");
    var base_image = document.getElementById(esarrastrable);
    if(cont6 == 1){
        context.drawImage(base_image, 18, 7, 80, 60);
        e.stopPropagation();
    }
    else if(cont6 == 2){
            context.drawImage(base_image, 105, 9, 80, 60);
            e.stopPropagation();
    }
    else if(cont6 == 3){
            context.drawImage(base_image, 195, 8, 80, 60);
            e.stopPropagation();
        }
    else if(cont6 == 4){
            context.drawImage(base_image, 15, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont6 == 5){
            context.drawImage(base_image, 105, 80, 80, 60);
            e.stopPropagation();
        }
    else if(cont6 == 6){
            context.drawImage(base_image, 195, 82, 80, 60);
            e.stopPropagation();
        }
    else if(cont6 > 6){
            alert("demasiadas imagenes");
            return false;
        }
    cont6 += 1;
    return false;
}

function end(e){
    e.dataTransfer.clearData("Data");
    return true;
}


var limpio1 = 0;
var limpio2 = 0;
var limpio3 = 0;
var limpio4 = 0;
var limpio5 = 0;
var limpio6 = 0;


function limpiar_edit(numero) {
    if (numero == 1){
        canvas1 = document.getElementById("canvas1");
        var ctx1 = canvas1.getContext('2d');
        ctx1.clearRect(0, 0, canvas1.width, canvas1.height);
        cont1 = 1;
        limpio1 = 1;
    }else if(numero == 2){
        canvas2 = document.getElementById("canvas2");
        var ctx2 = canvas2.getContext('2d');
        ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
        cont2 = 1;
        limpio2 = 1;
    }else if(numero == 3){
        canvas3 = document.getElementById("canvas3");
        var ctx3 = canvas3.getContext('2d');
        ctx3.clearRect(0, 0, canvas3.width, canvas3.height);
        cont3 = 1;
        limpio3 = 1;
    }else if(numero == 4){
        canvas4 = document.getElementById("canvas4");
        var ctx4 = canvas4.getContext('2d');
        ctx4.clearRect(0, 0, canvas4.width, canvas4.height);
        cont4 = 1;
        limpio4 = 1;
    }else if(numero == 5){
        canvas5 = document.getElementById("canvas5");
        var ctx5 = canvas5.getContext('2d');
        ctx5.clearRect(0, 0, canvas5.width, canvas5.height);
        cont5 = 1;
        limpio5 = 1;
    }else if(numero == 6){
        canvas6 = document.getElementById("canvas6");
        var ctx6 = canvas6.getContext('2d');
        ctx6.clearRect(0, 0, canvas6.width, canvas6.height);
        cont6 = 1;
        limpio6 = 1;
    }
}

cont_edit1 = 1
cont_edit2 = 1
cont_edit3 = 1
cont_edit4 = 1
cont_edit5 = 1
cont_edit6 = 1

function drop_edit(e,numero){
    mensaje = "Primero limpia la imágen";
    if(numero == 1){
        if (limpio1 == 0){
            alert(mensaje);
        }else{
            drop1(e);
            cont_edit1 += 1;
        }
    }else if(numero == 2){
        if (limpio2 == 0){
            alert(mensaje);
        }else{
            drop2(e);
            cont_edit2 += 1
        }
    }else if(numero == 3){
        if (limpio3 == 0){
            alert(mensaje);
        }else{
            drop3(e);
            cont_edit3 += 1
        }
    }else if(numero == 4){
        if (limpio4 == 0){
            alert(mensaje);
        }else{
            drop4(e);
            cont_edit4 += 1
        }
    }else if(numero == 5){
        if (limpio5 == 0){
            alert(mensaje);
        }else{
            drop5(e);
            cont_edit5 += 1
        }
    }else if(numero == 6){
        if (limpio6 == 0){
            alert(mensaje);
        }else{
            drop6(e);
            cont_edit6 += 1
        }
    }
return false;
}