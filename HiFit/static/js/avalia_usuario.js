//Tratamento do botão para quando o usuário avaliar uma recomendacao
function avaliarUsuario(usuario, valor_avaliacao) {
    $.ajax({
        url: '/usuario/perfil/'.concat('?usuario=').concat(usuario).concat('&page=1'),
        method: 'POST', // or another (GET), whatever you need
        data: {
            usuario: usuario,
            valor_avaliacao: valor_avaliacao,
            funcao: "avaliarRecomendacao"
        }
    });
}