const b=document.querySelector(".mbtn"),m=document.querySelector(".menu");
if(b)b.onclick=()=>b.setAttribute("aria-expanded",m.classList.toggle("open"));
const q=document.getElementById("q"),cat=document.getElementById("cat"),list=document.getElementById("list");
if(q&&list){const rows=[...list.tBodies[0].rows],count=document.getElementById("count"),run=()=>{const t=q.value.toLowerCase().trim(),c=cat.value;let n=0;
rows.forEach(r=>{const ok=(c=="all"||r.dataset.c==c)&&(!t||r.cells[0].textContent.toLowerCase().includes(t));r.hidden=!ok;n+=ok});count.textContent=n+" cheat codes found"};
q.oninput=run;cat.onchange=run}
