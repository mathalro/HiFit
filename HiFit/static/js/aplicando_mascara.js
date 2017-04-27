$('#id_tipo_identificacao').change(function() {
    var selected = $(':selected', this);
    console.log(selected)
}).trigger('change');