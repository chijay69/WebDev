$(document).ready(function(){
    $('btn').click(function(){
	$ajax({
	    url: '',
	    type: 'get',
	    data: {
		btn_text: $(this).text()
	    },
	    success: function(response){
		$('.btn').text(response.seconds)
	    }
	});
    });
});
