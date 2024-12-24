async function postData(url = " ",data = {}) {
    const response = await fetch(url,{
        method:"Post",headers:{
            "content-type":"application/json",},
            body:JSON.stringify(data),
        });
    return response.json();
    }
    
    sendbutton.addEventListener("click", async ()=>{
        questionInput = document.getElementsByClassName("gender");
        document.getElementsByClassName("gender").value = "";
        questionInput1 = document.getElementsByClassName("occasion");
        document.getElementsByClassName("occassion").value = "";
        questionInput2 = document.getElementsByClassName("dress");
        document.getElementsByClassName("dress").value = "";
        questionInput3 = document.getElementsByClassName("image-upload");
        document.getElementsByClassName("image-upload").value = "";
        questionInput4 = document.getElementsByClassName("skin-tone");
        document.getElementsByClassName("skin-tone").value = "";
        const question = "Sugget me an outfit to wear in" + {questionInput1} 
        
       
    //get the ans and populate it
    let result = await postData("/api",{"question":question})
    solution.innerHTML = result.answer})