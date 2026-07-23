fetch("/api/daily-tip")

.then(response => response.json())

.then(data=>{

document
.getElementById("daily-tip")
.innerHTML=data.tip;

});