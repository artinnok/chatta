$(document).ready(function () {
    $(".chat__send").click(function () {
        var text = $(".chat__input").val();

        $.post(
            "/add",
            {
                "text": text
            },
            function (data) {
                var div = '<div class="chat__message">' + data['text'] + '</div>';
                $('.chat__history').append(div);
            }
        );
    });
});