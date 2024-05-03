$(document).ready(function() {
    $('#btn_translate').click(function() {
        const language_code = $('#language_code').val();
        $.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
            function (data) {
                $('#hello').text(data.hello);
            }
        ); 
    });
});