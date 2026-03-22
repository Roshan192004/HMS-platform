// small helper (delete confirmation handled by Django generic views/forms)
document.addEventListener('DOMContentLoaded', function(){
  document.querySelectorAll('.btn-danger').forEach(function(el){
    el.addEventListener('click', function(e){
      // links with danger class that are not form buttons should be allowed to navigate
      // no-op here — keep for future enhancements
    })
  })
})
