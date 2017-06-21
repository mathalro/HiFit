function filtroPorCaracteristica(element) {    
    $.ajax({
        url: '/aluno/historico_recomendacoes/',
        method: 'GET', // or another (GET), whatever you need        
        data: {
            click: 1
        },
        dataType: 'json'
    });
}