$(document).ready(function() {
    $('form').submit(function (e) {
        
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(),
            success: function (data) {
                console.log(data)
                document.getElementById('confirmationid').innerHTML = data.status

                document.getElementById('name').value = ""
                document.getElementById('email').value = ""
                document.getElementById('subject').value = ""
                document.getElementById('message').value = ""
            }
        });
        e.preventDefault();
    });

    // Inject CSRF token into AJAX request.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
            }
        }
    })
});