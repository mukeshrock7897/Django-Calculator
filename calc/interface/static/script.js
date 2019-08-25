function process_expression(expression, callback) {
	console.log('Process expression: ' + expression);

	$ajax({
		url: '/processor/compute',
		type: 'POST',
		data: {data: expression},

		success: function(response) {
			if (response.answer) {
				callback(response.answer);
			} else {
				console.log('ERROR:', response.error);
			}
		},
		error: function(xhr, errormsg, err) {
			console.log(errormsg);
		}
	});
}

function clear_field(field) {
	field.value = '0';
}


$(document).ready(function() {
	let field = document.getElementById('input-field');

	$('.btn').on('click', function(event) {
		event.preventDefault();

		let symbol = event.target.innerHTML;

		console.log('symbol: ' + symbol);
			
		if (symbol === '=') {
			process_expression(field.value, function(answer) {
				field.value = answer;
			});
		} else if (symbol === 'AC') {
			clear_field(field);
			
			} else {
				if (field.value === '0') {
					field.value = symbol;
				} else {
					field.value = field.value + symbol;
				}
		}
	});
});
