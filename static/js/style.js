const inp = document.getElementsByTagName("input");
const btn = document.getElementById("reg_btn");
for(let i=0; i < inp.length; i++)
{
    const d=inp[i];
    d.addEventListener("focus",function(){
        d.style.fontSize = "60px";
        d.style.backgroundColor = "red";
        d.style.boxShadow = "30px 30px 10px aliceblue";
        d.style.transition = "0.5s";
    })
    d.addEventListener("blur",function(){
        d.style.fontSize = "";
        d.style.backgroundColor = "";
        d.style.boxShadow = "";
        d.style.transition = "";
    })
}
btn.addEventListener("click",function(){
    btn.style.backgroundColor = "green";
    alert('Registered Successfully :))');
})