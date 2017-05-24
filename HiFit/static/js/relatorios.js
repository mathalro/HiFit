$(document).ready(function() {
    // Adiciona máscaras aos campos
    $('.date').mask('00/00/0000')

    // Imprime o relatorio que esta no iframe
    if (!jQuery.isEmptyObject($("#salvar-iframe").attr('id'))) {
        window.frames["iframe-relatorios"].window.focus();
        window.frames["iframe-relatorios"].window.print();
    }
});