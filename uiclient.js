ui = new Object();

ui.host = 'http://localhost:50602'
ui.queryobj = 

//********************************************************************************** */
window.addEventListener('beforeunload',function(event){ //when closing browser, close python
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request",'close'); //prepare files

    xhr.open('POST',ui.host, true);

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(xhr.responseText);
        }
    };
    
    xhr.send(fdata);
    
})

//******************************************************************************************** */

window.addEventListener('onload',function(event){

    for(key of Object.keys(ui.queryobj)){

        if (document.getElementById(key)){ //if such id doesn't exists, than object will return null which is false

            document.getElementById(key).value = ui.queryobj[key];
        }
    }

    ui.submit();

})
//*********************************************************************************** */
ui.submit = function(){ //request can be insert or update
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("in1",document.getElementById("in1").value);

    fdata.append("in2",document.getElementById("in2").value);

    fdata.append("doc1",document.getElementById("doc1").files[0]);

    fdata.append("doc2",document.getElementById("doc2").files[0]);

    fdata.append("doc3",document.getElementById("doc3").files[0]);

    xhr.open('POST',ui.host,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)
            
            alert(this.responseText)

            resobj = JSON.parse(this.responseText);

            ui.download(resobj[0],resobj[1])
        }
    }

    xhr.send(fdata);     
}


//********************************************************************************************* */
ui.download = function(filename, filetext){

    var a = document.createElement("a");

    document.body.appendChild(a);

    a.style = "display: none";

    a.href = 'data:application/octet-stream;base64,' + filetext;

    a.download = filename;

    a.click();

    document.body.removeChild(a);

}


