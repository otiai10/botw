(function(){
  var trs = document.getElementsByTagName('tr');
  for(var i=0;i<trs.length;i++)
    if(trs[i].className == 'command-exp')
      trs[i].addEventListener('click',function(){window.open(this.getAttribute('url'),null)});
})();
