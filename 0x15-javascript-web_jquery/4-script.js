$(document).ready(function(){
    const currentClass = $('header');
    $('#toggle_header').click(function(){
        currentClass.removeClass('green').addClass('red');
    });
    
});