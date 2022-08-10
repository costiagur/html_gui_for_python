myfunc = new Object();

//*********************************************************************************** */
myfunc.submit = function(){ //request can be insert or update
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("in1",document.getElementById("in1").value);

    fdata.append("in2",document.getElementById("in2").value);

    fdata.append("doc1",document.getElementById("doc1").files[0]);

    fdata.append("doc2",document.getElementById("doc2").files[0]);

    fdata.append("doc3",document.getElementById("doc3").files[0]);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                alert(resobj[1])
            }
            else{
                myfunc.download(resobj[0],resobj[1])
            }
        }
    }

    xhr.send(fdata);     
}


//********************************************************************************************* */
myfunc.download = function(filename, filetext){

    var a = document.createElement("a");

    document.body.appendChild(a);

    a.style = "display: none";

    a.href = 'data:application/octet-stream;base64,' + filetext;

    a.download = filename;

    a.click();

    document.body.removeChild(a);

}
