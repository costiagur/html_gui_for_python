myfunc = new Object();
//*********************************************************************************** */
myfunc.msg = function(title,msg_txt){
    document.getElementById("msg_title").innerHTML = title
    document.getElementById("msg_txt").innerHTML = msg_txt
    document.getElementById("msg_dg").showModal()
}
//********************************************************************************************* */
myfunc.response = function(inid,intxt){
    document.getElementById(inid + "_res").innerHTML = intxt
    document.getElementById("response_dg").showModal()
}
//********************************************************************************************* */
myfunc.resp_close = function(){
    document.getElementById("response_dg").close();
    
    resnames = document.getElementsByName("inres")
    
    for (resnm of resnames){
        resnm.innerHTML = ""
    }
}
//********************************************************************************************* */
myfunc.sendrequest = function(fdata){
    return new Promise((resolve) =>{    
        var xhr = new XMLHttpRequest();
        xhr.open('POST',"http://127.0.0.1:"+ui.port,true)
    
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

    arr = ["in1","in2","in3","doc1"]

    for (eacharr of arr){
        files = document.getElementById(eacharr).files
        
        if(files != null){
            if (files.length > 0){
                var fdata = new FormData();
                fdata.append("request",eacharr)
                fdata.append(eacharr,document.getElementById(eacharr).files[0]);
            }
        }
        else{
            if (document.getElementById(eacharr).value != ""){
                var fdata = new FormData();
                fdata.append("request",eacharr)
                fdata.append(eacharr,document.getElementById(eacharr).value);;    
                
            }
        }
    
        const resobj = await myfunc.sendrequest(fdata)
        if (resobj[0] == "Error"){
            myfunc.msg(resobj[0], resobj[1])
       }
       else{
           if (resobj[0].slice(0,2) == "in"){
               myfunc.response(resobj[0], resobj[1])
           }
           else {
               myfunc.download(resobj[0], resobj[1])
           }
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
