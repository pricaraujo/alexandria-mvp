fetch("/api/challenge")

.then(r=>r.json())

.then(challenge=>{

document

.getElementById("challenge")

.innerHTML=

challenge.title+

"<br><br><b>+"+

challenge.xp+

" XP</b>";

});

fetch("/api/badges")

.then(r=>r.json())

.then(badges=>{

let html="";

badges.forEach(b=>{

html+=`

<div class="badge-card">

<h1>${b.icon}</h1>

<h3>${b.name}</h3>

<p>${b.description}</p>

</div>

`;

});

document

.getElementById("badges")

.innerHTML=html;

});

function reward(xp){

let popup=

document.getElementById("reward");

popup.innerHTML=

"+"+xp+" XP 🎉";

popup.style.display="block";

setTimeout(()=>{

popup.style.display="none";

},2500);

}