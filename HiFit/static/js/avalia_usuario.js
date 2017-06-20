//Tratamento do botão para quando o usuário avaliar uma recomendacao
function avaliarRecomendacao(recomendacao_avaliada, valor_avaliacao) {
    $.ajax({
        url: '/usuario/perfil',
        method: 'POST', // or another (GET), whatever you need
        data: {
            recomendacao_avaliada: recomendacao_avaliada,
            valor_avaliacao: valor_avaliacao,
            funcao: "avaliarRecomendacao"
        }
    });
}