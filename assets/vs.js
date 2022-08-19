$(document).ready(function(){
 $.getJSON("/displayallcategoryjson",function(data){
   $.each(data,function(index,item){
      $('#cid').append($('<option>').text(item[1]).val(item[0]))

   })

 })

    $('#cid').change(function(){

      $('#sid').empty()
      $('#sid').append($('<option>').text("-Select Show-"))
      $.getJSON("/displayallshowjson",{cid:$('#cid').val()},function(data){
            alert(data)
          $.each(data,function(index,item){

          $('#sid').append($('<option>').text(item[2]).val(item[1]))

      })

 })

    })

 $('#search').keyup(function(){
       $.getJSON("/searching",{search:$('#search').val()},function(data){
       let htm="";

          $.each(data,function(index,item){
               htm+="<a href='#'><img  src='/static/"+item[11]+"' class='set zoom' /></a>"
      })

      $('#result').html(htm)
   })

   })
})