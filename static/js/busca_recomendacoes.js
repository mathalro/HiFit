//Tratamento do botão para quando o usuário avaliar uma recomendacao
function avaliarRecomendacao(recomendacao_avaliada, valor_avaliacao) {
    $.ajax({
        url: '#',
        method: 'GET', // or another (GET), whatever you need
        data: {
            recomendacao_avaliada: recomendacao_avaliada,
            valor_avaliacao: valor_avaliacao,
            funcao: "avaliarRecomendacao"
        }
    });
}


//Tratamento do botão para quando o usuário aceitar uma recomendacao
function aceitarRecomendacao(element) {
    $.ajax({
        url: '/aluno/buscar-recomendacoes/',
        method: 'GET', // or another (GET), whatever you need
        data: {
            recomendacao_aceita: $(element).val(), // data you need to pass to your function
            funcao: "aceitarRecomendacao"
        },
        dataType: 'json',
        success: function (data) {
            $("#"+ data.value).attr('class','btn btn-success');
            $("#"+ data.value).html("Recomendação aceita");
            $("#"+ data.value).attr('disabled',true);
        }
    });
}