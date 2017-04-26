
function excluirCadastro() {
    $.ajax({
        url: '/instrutor/meu_cadastro/',
        method: 'DELETE', // or another (GET), whatever you need        
        data: {
            click: 1,
            csrfmiddlewaretoken:'{{csrf_token}}'
        }
    });
}