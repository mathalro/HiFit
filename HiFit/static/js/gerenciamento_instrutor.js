function excluirCadastro() {
    $.ajax({
        url: '/instrutor/meu_cadastro/',
        method: 'GET', // or another (GET), whatever you need        
        data: {
            click: 1,
        }
    });
}