$(document).ready(function(){
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        dataType: 'json',
        success: function(data){
            data.results.forEach(function(movie) {
               $('#list_movies').append(movie.title); 
            });

        },
        error: function(){
            console.error('Error fetching data from the API.');
        }
    });
});
