//Tratamento do botão para quando o usuário solicita uma alteração de regra
$('.botaoSolicitacao').click(function() {    
    $.ajax({
        url: '/instrutor/regras/',
        method: 'GET', // or another (GET), whatever you need        
        data: {
            regra_solicitada: $('.botaoSolicitacao').val(), // data you need to pass to your function
            click: 1
        },
        dataType: 'json',
        success: function (data) {
            $("#"+ data.value).attr('class','btn btn-danger');
            $("#"+ data.value).html("Alteração já solicitada");
            $("#"+ data.value).attr('disabled',true);         
        }
    });
});