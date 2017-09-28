$(document).ready(function () {
    $(".chat__send").click(function () {
        var text = $(".chat__input").val();
        console.log(text);
        $.post(
            "/add",
            {
                "text": text
            },
            function (data) {
                console.log(data);
            }
        );
    });
});