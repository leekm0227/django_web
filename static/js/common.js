function ajaxError(request, status, error) {
    alert(request.responseText);
}

function loadingToggle() {
    let loading = $("#img_container");

    if (loading === undefined) {
        $('body').append('<div id="img_container" style="position:absolute; top:0px; left:0px; width:100%; height:100%; z-index:9999;">' +
            '<img src="/static/images/loading.gif" border="3px" style="position:absolute; top: 40%; left: ' + eval(($(window).width() / 2) - (100 / 2)) + 'px; width: 100px; height: 100px;">' +
            '</div>');
    } else {
        loading.remove();
    }
}

$(document).ajaxComplete(loadingToggle).ajaxSend(loadingToggle).ajaxError(ajaxError);
$(document).ready(function () {
    $(".btnLogin").on("click", function () {
        location.href = "/login/"
    });

    $(".btnJoin").on("click", function () {
        location.href = "/join/"
    });

    $(".btnLogout").on("click", function () {
        location.href = '/logout/';
    });

    $("input:file").on("change", function () {
        let viewId = $(this).attr("id") + "View";
        let file = $(this)[0].files[0];
        let reader = new FileReader();
        reader.readAsDataURL(file);

        reader.onload = function (e) {
            $('#' + viewId).html('<img src="' + e.target.result + '">');
        }
    });

    $("#tssr").on("click", function () {
        let img = $("#tssrImg");

        if (img.val() === "") {
            alert("img empty");
            img.focus();
            return false;
        }

        $.ajax({
            type: "POST",
            url: "/api/tssr/",
            dataType: "json",
            contentType: false,
            processData: false,
            data: new FormData(document.tssrFrm),
            success: function (json) {
                $("#tssrTxt").text(json.txt);
            }
        });
    });

    $("#login").on("click", function () {
        let email = $("#email");
        let pwd = $("#pwd");
        let frm = $("#frmLogin");

        if (email.val().length === 0) {
            alert("plz check email");
            email.focus();
            return false;
        }

        if (pwd.val().length === 0) {
            alert("plz check pwd");
            pwd.focus();
            return false;
        }

        loadingToggle();
        frm.attr("action", "/login/").attr("method", "POST").submit();
    });

    $("#join").on("click", function () {
        let email = $("#email");
        let name = $("#name");
        let pwd = $("#pwd1");
        let pwd1 = $("#pwd2");
        let frm = $("#frmJoin");

        if (email.val().length === 0) {
            alert("plz check email");
            email.focus();
            return false;
        }

        if (name.val().length === 0) {
            alert("plz check name");
            name.focus();
            return false;
        }

        if (pwd.val().length === 0) {
            alert("plz check pwd");
            pwd.focus();
            return false;
        }

        if (pwd.val() !== pwd1.val()) {
            alert("plz check pwd");
            pwd.focus();
            return false;
        }

        loadingToggle();
        frm.attr("action", "/join/").attr("method", "POST").submit();
    });
});