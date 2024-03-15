$(document).ready(function() {
	$('img').click(function() {
		var largeImage = $(this).data('large');
		$('.overlay-image').attr('src', largeImage);
		$(this).parent().next().fadeIn();
	});

	$(".overlay").click(function() {
		
		$(this).fadeOut();
	});
});