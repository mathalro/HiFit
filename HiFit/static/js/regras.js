// Enum de campos da linha da tabela
var NOME_CAMPOS = {
    ATIVIDADE: 0, RESTRICAO: 1, BENEFICIO: 2, MALEFICIO: 3, PONTUACAO: 4, ID: 5, SOLICITANTE: 7
};


//Tratamento do botão para quando o usuário solicita uma alteração de regra
function solicitarAlteracao(element) {    
    $.ajax({
        url: '/instrutor/regras/',
        method: 'GET', // or another (GET), whatever you need        
        data: {
            regra_solicitada: $("#"+element).val(), // data you need to pass to your function
            click: 1
        },
        dataType: 'json',
        success: function (data) {
            $("#"+ data.value).attr('class','btn btn-danger');
            $("#"+ data.value).html("Alteração já solicitada");
            $("#"+ data.value).attr('disabled',true);         
        }
    });
}


// Seta os campos do modal de edicao de acordo com a regra a ser editada
function  setModalEditar(element) {
    var campos = [];
    // Pega o número da linha da tabela a qual o botão pertence
    var n_linha = element.parentNode.parentNode.rowIndex;
    // Pega a linha da tabela
	var linha = document.getElementById("table-edit-minhas").rows[n_linha].cells;
    for (var i = 0; i <= 5; i++) {
        if (linha[i].innerHTML == "None")
            campos[i] = "";
        else
            campos[i] = linha[i].innerHTML;
    }
    // Seta o valor dos selects do modal
	document.getElementById('sel_edit_atividade').value = campos[NOME_CAMPOS.ATIVIDADE];
	document.getElementById('sel_edit_restricao').value = campos[NOME_CAMPOS.RESTRICAO];
	document.getElementById('sel_edit_beneficio').value = campos[NOME_CAMPOS.BENEFICIO];
	document.getElementById('sel_edit_maleficio').value = campos[NOME_CAMPOS.MALEFICIO];
	document.getElementById('in_edit_pontuacao').value = campos[NOME_CAMPOS.PONTUACAO];
	document.getElementById('in_edit_id').value = campos[NOME_CAMPOS.ID];
}

function setModalExcluir(id) {
    document.getElementById("excluirRegra").value = id;
}

function setModalExcluirCaracteristica(id) {
    document.getElementById("excluir").value = id;
}

function setModalExcluirComentario(id) {
    document.getElementById("excluirComentario").value = id;
}

function setModalEditaPost(id, conteudo, privacidade) {
    document.getElementById("edita-conteudo").value = conteudo;
    document.getElementById("edita-privacidade").value = privacidade;
    document.getElementById("atualiza-post").value = id;
}
