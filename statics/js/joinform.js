$(function(){
	$('#email').change(function(){
			console.log('changed!!!');
			$('#btn-emailchk').show();
			$('#img-emailchk').hide();
	});
	$('#btn-emailchk').click(function(){
	email = $('#email').val();
	if(email == ''){
		return;
	}
		$.ajax({
			url : '/user/checkemail?email=' + email,
			type : 'get',
			data : '',
			dataType : 'json',
			success: function(response){
			if(response.result == false){
			alert('존재하는 이메일입니다. 다른 주소를 입력해주세요.');
			$('#email').val('').focus();
			return;
			}
			$('#btn-emailchk').hide();
			$('#img-emailchk').show();
			}
		});
	});
});