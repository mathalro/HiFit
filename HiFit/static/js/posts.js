function setModalExcluirPost(id) {
    document.getElementById("excluirPost").value = id;
}

function setModalExcluirComentario(id) {
    document.getElementById("excluirComentario").value = id;
}

function setModalEditaPost(id, conteudo, privacidade) {
    document.getElementById("edita-conteudo").value = conteudo;
    document.getElementById("edita-privacidade").value = privacidade;
    document.getElementById("atualiza-post").value = id;
}

function avaliarPost(id, valor_avaliacao) {
    $.ajax({
        url: '#',
        method: 'GET', // or another (GET), whatever you need
        data: {
            post_avaliado: id,
            valor_avaliacao: valor_avaliacao,
            funcao: "avaliarPost"
        }
    });
}