$(document).ready(function() {
    function fetchTranslation() {
        const language_code = $('#language_code').val();
        $.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
            function (data) {
                $('#hello').text(data.hello);
            }
        ); 
    }
    $('#btn_translate').click(function() {
        fetchTranslation();
    });
    $('#language_code').click(function(e) {
        if (e.wich == 13) {
            fetchTranslation();
        }
    });
});