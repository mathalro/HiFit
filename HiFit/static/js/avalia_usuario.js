//Tratamento do botão para quando o usuário avaliar uma recomendacao
function avaliarUsuario(usuario, valor_avaliacao) {
    $.ajax({
        url: '/usuario/perfil/'.concat('?usuario=').concat(usuario).concat('&page=1'),
        method: 'GET', // or another (GET), whatever you need
        data: {
            avaliado: usuario,
            nota: valor_avaliacao,
            avaliarUsuario: ""
        },
    });
}

$( document ).ajaxComplete(function(r) {
	location.reload();
});