var NOME_CAMPOS = {
    ATIVIDADE: 0, RESTRICAO: 1, BENEFICIO: 2, MALEFICIO: 3, PONTUACAO: 4, ID: 5, SOLICITANTE: 7
};


// Seta os campos do modal de edicao de acordo com a regra a ser editada
function  setModalCampos(element) {
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


function  excluiRegra(element) {
    // Pega o número da linha da tabela a qual o botão pertence
    var n_linha = element.parentNode.parentNode.rowIndex;
    // Pega a linha da tabela
	var linha = document.getElementById("table-edit-minhas").rows[n_linha].cells;
    regra_id = linha[NOME_CAMPOS.ID].innerHTML
    dados = {regra_del_id: regra_id, excluirRegra: "excluirRegra"}

    $.ajax({ // create an AJAX call...
    data: dados,
    type: $(this).attr('GET'), // GET or POST
    url: $(this).attr('/instrutor/regras/'), // the file to call
    success: function(response) { // on success..
        //$('#DIV_CONTAINING_FORM).html(response); // update the DIV
    }
    });
}

function aceitarSolicitacao(element) {
    var campos = [];
    // Pega o número da linha da tabela a qual o botão pertence
    var n_linha = element.parentNode.parentNode.rowIndex;
    // Pega a linha da tabela
	var linha = document.getElementById("table-minhas_solicitacoes").rows[n_linha].cells;
	    regra_id = linha[NOME_CAMPOS.ID].innerHTML
    dados = {
        regra_sol_id: regra_id,
        solicitante_id: linha[NOME_CAMPOS.SOLICITANTE].innerHTML,
        aceitarSolicitacao: "aceitarSolicitacao"
     }

    $.ajax({ // create an AJAX call...
    data: dados,
    type: $(this).attr('GET'), // GET or POST
    url: $(this).attr('/instrutor/regras/'), // the file to call
    success: function(response) { // on success..
        //$('#DIV_CONTAINING_FORM).html(response); // update the DIV
    }
    });
}