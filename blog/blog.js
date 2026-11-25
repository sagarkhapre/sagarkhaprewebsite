(function(){
 var cats = window.BLOG_CATEGORIES || [], posts = window.BLOG_POSTS || [], cur = window.BLOG_CURRENT || "all";
 function catOf(slug){ for (var i=0;i<cats.length;i++) if (cats[i].slug===slug) return cats[i]; return {slug:slug,name:slug,cl:"c1"}; }
 function fmt(d){ try { return new Date(d+"T00:00:00").toLocaleDateString("en-IN",{day:"numeric",month:"short",year:"numeric"}); } catch(e){ return d; } }
 function cover(p, cls){ var c=catOf(p.cat); return '<div class="cover '+c.cl+'"><div class="big">'+p.big+'</div><div class="small">'+p.small+'</div>'+(cls?'<img class="lg" src="/img/logo.jpg" alt="">':'')+'</div>'; }
 function card(p){ var c=catOf(p.cat); return '<a class="card" href="/blog/'+p.slug+'/">'+cover(p,false)+'<div class="body"><span class="cat">'+c.name.replace(/&/g,"&amp;")+'</span><h3>'+p.title+'</h3><p class="ex">'+p.excerpt+'</p><div class="by">'+fmt(p.date)+' &middot; '+(p.read||"")+'</div></div></a>'; }
 var tabs = '<a class="tab'+(cur==="all"?" on":"")+'" href="/blog/">All</a>' + cats.map(function(c){ return '<a class="tab'+(cur===c.slug?" on":"")+'" href="/blog/category/'+c.slug+'/">'+c.name.replace(/&/g,"&amp;")+'</a>'; }).join("");
 document.getElementById("tabs").innerHTML = tabs;
 var list = posts.filter(function(p){ return cur==="all" || p.cat===cur; });
 if (list.length) {
  var f = list[0], fc = catOf(f.cat);
  document.getElementById("feat").innerHTML = '<a class="feat" href="/blog/'+f.slug+'/">'+cover(f,true)+'<div class="body"><span class="cat">'+fc.name.replace(/&/g,"&amp;")+'</span> <span class="cat alt">Latest</span><h2>'+f.title+'</h2><p class="ex">'+f.excerpt+'</p><div class="by">'+fmt(f.date)+' &middot; '+(f.read||"")+'</div><span class="read">Read the full post &rarr;</span></div></a>';
  document.getElementById("grid").innerHTML = list.slice(1).map(card).join("");
 } else {
  document.getElementById("empty").style.display = "block";
 }
})();
