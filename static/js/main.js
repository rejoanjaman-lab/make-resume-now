// Optional: show a simple confirmation before navigating away if form is dirty
(function(){
  const form = document.getElementById('resume-form');
  if(!form) return;
  let dirty = false;
  form.addEventListener('input', ()=> dirty = true);
  window.addEventListener('beforeunload', (e)=>{
    if(!dirty) return;
    e.preventDefault();
    e.returnValue = '';
  });
})();
