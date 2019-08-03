$(document).ready(function(){
  count = 1

  function getCookie(c_name)
  {
      if (document.cookie.length > 0)
      {
          c_start = document.cookie.indexOf(c_name + "=");
          if (c_start != -1)
          {
              c_start = c_start + c_name.length + 1;
              c_end = document.cookie.indexOf(";", c_start);
              if (c_end == -1) c_end = document.cookie.length;
              return unescape(document.cookie.substring(c_start,c_end));
          }
      }
      return "";
   }

   $('#full-name').change(function(e) {
       e.preventDefault();
       selectedName = $(this).children("option:selected").val();
       
       req =	$.ajax({
           
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        type: 'POST',
        url : '/payroll/employee_salary/new/',
        data:{
            'select_name': selectedName
        },
        dataType: 'json'
    })
    .done(function done(data){
        console.log(data.row)
        $('#employee-id').val(data.row);
        console.log($('#full-name'))
    })
   })


});