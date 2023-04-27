// fungsi untuk mendefinisian type input
function inputType() {
    // ambil tag input
    var input = document.getElementsByTagName('input');
    // looping tag input
    for (var i = 0; i < input.length; i++) {
        // ambil input yg memiliki id
        var input_id = document.getElementById(input[i].id);
        // jika ada input id
        if (input_id) {
            // hilangkan autocomplete
            input_id.setAttribute('autocomplete', 'off');
            // ambil input type
            var input_type = input_id.getAttribute('type');
            // type nominal
            if (input_type == 'nominal') {
                nominalDef(input_id);
            }
        }
    }
}

// fungsi untuk set function input nominal
function nominalDef(input_id) {
    // atribut onchange
    var onchange_default = 'numberFormat("' + input_id.id + '")' + ';';
    var onchange = input_id.getAttribute('onchange');
    if (!onchange) {
        onchange = '';
    }
    input_id.setAttribute('onchange', onchange_default + onchange);
    // atribut onkeyup
    var onkeyup_default = 'nominalInput("' + input_id.id + '")' + ';';
    var onkeyup = input_id.getAttribute('onkeyup');
    if (!onkeyup) {
        onkeyup = '';
    }
    input_id.setAttribute('onkeyup', onkeyup_default + onkeyup);
    // atribut onkeypress
    var onkeypress_default = onkeyup_default;
    input_id.setAttribute('onkeypress', onkeypress_default);
}

// fungsi untuk mengatur input nominal
function nominalInput(id) {
    var idinput = document.getElementById(id);
    var lastchar = idinput.value.charAt(idinput.selectionStart - 1);
    if (isNaN(lastchar) && lastchar !== ',' && lastchar !== '.') {
        idinput.value = idinput.value.replace(lastchar, '');
        nominalInput(id);
    }
}

// fungsi untuk mengubah format number
function numberFormat(id) {
    var idinput = document.getElementById(id);
    if (idinput.value) {
        var numberReplace = idinput.value.replaceAll(',', '');
        var numberInt = Number(numberReplace);
        idinput.value = numberInt.toLocaleString('en-US', { style: "decimal" });
    }
}