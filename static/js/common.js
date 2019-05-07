function ajaxError(request, status, error) {
    alert(request.responseText);
}

function ajaxBeforeSend() {
    let left = 0;
    let top = 0;
    width = $(window).width();
    height = $(window).height();

    $('body').append('<div id="img_container" style="position:absolute; top:' + top + 'px; left:' + left + 'px; width:' + width + 'px; height:' + height + 'px; z-index:9999; filter:alpha(opacity=50); opacity:alpha*0.5; margin:auto; padding:0; "><img src="/static/images/loading.gif" border="3px" style="width: 100px; height: 100px;"></div>');
}

function ajaxComplete() {
    $("#img_container").remove();
}

$(document).ajaxComplete(ajaxComplete).ajaxSend(ajaxBeforeSend).ajaxError(ajaxError);

$(document).ready(function () {
    $("#btnLogin").on("click", function () {
        let id = $("#id");
        let pwd = $("#pwd");
        let frm = $("#frmLogin");

        if (id.val().length === 0) {
            alert("id empty");
            id.focus();
            return false;
        }

        if (pwd.val().length === 0) {
            alert("id empty");
            pwd.focus();
            return false;
        }

        frm.attr("action", "/login/").attr("method", "POST").submit();
    });
});