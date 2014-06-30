function actualiza_componentes_li(data, posicion){
    $('#table'+posicion+'>tbody').empty(); //elimino el cotenido actual del ul
    // agrego los tipos obtenidos por ajax
    var sorters = [sorter3];
    try{
        sorters = [sorter3, sorter4];
    }catch(e){}
    try{
        sorters = [sorter3, sorter4, sorter5];
    }catch(e){}
    $.each(data, function(index, objeto){
        var agregar = document.createElement("tr");
        agregar.setAttribute('class', 'elemento');
        agregar.setAttribute('draggable', 'true');
        agregar.setAttribute('id', posicion+"-"+objeto['pk']);
        var td1 = document.createElement("td");
        var td2 = document.createElement("td");
        // agregar.setAttribute('ondragstart', 'return dragStart(event)');
        // agregar.setAttribute('ondragend', 'return dragEnd(event)');
        var contenidotd1 = document.createTextNode(objeto['modelo']);
        var contenidotd2 = document.createTextNode(objeto['precio']);
        td1.appendChild(contenidotd1);
        td2.appendChild(contenidotd2);
        agregar.appendChild(td1);
        agregar.appendChild(td2);
        //agregar.appendChild(contenido);
        //agregar.innerHTML("<input type='radio' name='case' value='"+objeto['pk']+"'/> "+objeto['modelo']+"- S/. "+objeto['precio']);
        //console.log(agregar);
        var divi = $('#table'+posicion+'>tbody');
        $(agregar).appendTo(divi);
        //divi.appendChild(agregar);
        //$("<li class='elemento' draggable='true' id='"+posicion+"-"+objeto['pk']+"' ondragstart='return dragStart(event)' ondragend='return dragEnd(event)'><input type='radio' name='case' value='"+objeto['pk']+"'/> "+objeto['modelo']+"- S/. "+objeto['precio']+"</li>").appendTo('#'+seccion);
        // $("<li><input type='radio' name='"+seccion+"' value='"+objeto['pk']+"'/> "+objeto['modelo']+" - S/. "+objeto['precio']+"</li>")
        // .appendTo('#'+seccion);
    });
    // REDIFINIENDO EVENTOS START Y END
    var drags = document.querySelectorAll('tr');
    [].forEach.call(drags, function(drag) {
        drag.addEventListener('dragstart', dragStart, false);
        drag.addEventListener('dragend', dragEnd, false);
    });
    try {
       sorters[parseInt(posicion,10)-3].init();
    } catch (e) {}
}
function obtener_precio(){
    precio = 0.00;
    for(var i=0; i < localStorage.length; i++){
        var key_name = localStorage.key(i);
        item = localStorage.getItem(key_name);
        precio = parseFloat(precio) + parseFloat(item);
    }
    return precio;
}
// ------------------- FUNCIONES PARA EL DnD ---------------------
function dragEnter(e) {
    var idelt = e.dataTransfer.getData("Text");
    //e.target.classList.add('over');
    //console.log(this);
    var marcado = document.getElementById("contenedor");
    marcado.classList.add('over');
    return true;
}

function dragLeave(e) {
    // this.classList.remove('over');  // this / e.target is previous target element.
    var marcado = document.getElementById("contenedor");
    marcado.classList.remove('over');
}

function dragOver(e) {
    var idelt = e.dataTransfer.getData("Text");
    var id = e.target.getAttribute('id');
    e.dataTransfer.dropEffect = 'move';
    return false;
}

function dragDrop(e) {
    var idelt = e.dataTransfer.getData("Text");
    var url_img = "";
    var sw_img = false;
    datos = idelt.split("-");
    posicion = parseInt(datos[0],10);
    num_objeto = datos[0];
    id_componente = datos[1];
    lista_pos = [1, 6, 7, 8, 9, 10, 11, 12];
    nombres = ['Placa', 'Memoria RAM', 'Procesador', 'Disco Duro'];
    if ( lista_pos.indexOf(posicion)>=0 ){
        sw_img = true;
    }else{
        sw_img = false;
    }
    if (posicion == 10){
        if (datos[2]=='2'){
            num_objeto = 13;
        }
    }
    $.getJSON('/datos_objeto/'+id_componente+'/'+num_objeto+'/',function(data){
        $.each(data, function(index, objeto){
            add_valor = '';
            if (posicion == 10){
                if (datos[2]=='2'){
                    num_objeto = 10;
                }
                add_valor = "-"+datos[2];
            }
            precio = parseFloat(objeto["precio"].replace(",", ".")).toFixed(2);
            url_img = objeto['url_img'];
            localStorage.setItem(num_objeto, precio);
            $('#ele'+num_objeto).val(id_componente+add_valor);
            precio = obtener_precio();
            $('#precio_total').val(precio.toFixed(2));
            if (sw_img){
                var Img=document.createElement("img");
                Img.setAttribute('src', url_img);
                Img.setAttribute('id', 'img'+datos[0]);
                var imagen = document.getElementById('img'+datos[0]);
                divisor_padre = imagen.parentNode;
                divisor_padre.removeChild(imagen);
                divisor_padre.appendChild(Img);
            }else{
                var texto = document.createElement("p");
                var nodoTexto = document.createTextNode(nombres[num_objeto-2]+": "+objeto['modelo']);
                texto.setAttribute('id', 'elemento'+num_objeto);
                texto.appendChild(nodoTexto);
                var texto_ant = document.getElementById('elemento'+num_objeto);
                divisor_padre = texto_ant.parentNode;
                divisor_padre.removeChild(texto_ant);
                divisor_padre.appendChild(texto);
            }
        });
    });
    if (posicion == 2){
        $.getJSON('/datos_componentes/'+id_componente+'/',function(data){
            $.each(data, function(index, objeto){
                actualiza_componentes_li(objeto['procesadores']['datos'],4);
                actualiza_componentes_li(objeto['memorias']['datos'], 3);
                actualiza_componentes_li(objeto['discos']['datos'], 5);
            });
        });
    }
    e.stopPropagation();
    return false; // return false so the event will not be propagated to the browser
}

function dragStart(e) {
    e.dataTransfer.effectAllowed='move';
    //ev.dataTransfer.dropEffect='move';
    e.dataTransfer.setData("Text", this.getAttribute('id'));
    //console.log(e.target);
    //console.log(this);
    //e.dataTransfer.setDragImage(e.target,0,0);
    //console.log(this);
    this.style.opacity = '0.4';
    this.classList.add('over');
    return true;
}

function dragEnd(e) {
    e.dataTransfer.clearData("Text");
    this.style.opacity = '1';
    this.classList.remove('over');
    var marcado = document.getElementById("contenedor");
    marcado.classList.remove('over');
    return true;
}