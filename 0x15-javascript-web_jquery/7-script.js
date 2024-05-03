$(document).ready(function(){
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        dataType: 'json',
        success: function(data){
            const characterName = data.name;
            $('#character').text(characterName);
        },
        error: function() {
            console.error('Error fetching data from the API.');
        }
    });
});