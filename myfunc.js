myfunc = new Object();
//*********************************************************************************** */
myfunc.msg = function(title,msg_txt){
    document.getElementById("msg_title").innerHTML = title
    document.getElementById("msg_txt").innerHTML = msg_txt
    document.getElementById("msg_dg").showModal()
}
//********************************************************************************************* */
myfunc.sendrequest = function(fdata){
    return new Promise((resolve) =>{    
        var xhr = new XMLHttpRequest();
        xhr.open('POST',"http://localhost:"+ui.port,true)
    
        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {   
                console.log(this.responseText)
    
                resobj = JSON.parse(this.responseText);
                resolve(resobj)    
     
            }
            else if (this.readyState == 4 && this.status != 200){
                resolve(["Error",this.responseText])

            }
        }
    
        xhr.send(fdata);   
    })
}

//*********************************************************************************** */
myfunc.submit = async function(){ //request can be insert or update
    var fdata = new FormData();

    request = "file1"

    fdata.append("request",request)

    fdata.append("in1",document.getElementById("in1").value);

    fdata.append("in2",document.getElementById("in2").value);

    fdata.append("doc1",document.getElementById("doc1").files[0]);

    fdata.append("doc2",document.getElementById("doc2").files[0]);

    fdata.append("doc3",document.getElementById("doc3").files[0]);

    const resobj = await myfunc.sendrequest(fdata)
    
    if ( resobj[0] == "Error"){
        myfunc.msg( resobj[0], resobj[1])
   }
   else{
       if (request == "num1"){
           myfunc.msg( resobj[0], resobj[1])
       }
       else if (request == "file1"){
           myfunc.download( resobj[0], resobj[1])
       }
   }      
    
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
