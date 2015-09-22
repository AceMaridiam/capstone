$(document).ready(function() {

	// modal
	$('.pop').on('click', function() {
		$('.imagepreview').attr('src', $(this).find('img').attr('src'));
		$('#imagemodal').modal('show');   
	});		


	// Stores page count in localStorage
	if (localStorage.pagecount) {
		localStorage.pagecount=Number(localStorage.pagecount) +1;
	} else {
		localStorage.pagecount=1;
	}
	var Views = ("Views: " + localStorage.pagecount);
	// Sends Views varible to div with class pageViews 
	$('.pageViews').text(Views);


	// Fades out squirrel on click
	$('.icon-squirrel').on('click', function() {
		$('.login').fadeOut("slow");
	})


	$(".subscribe").delay(2000).animate({left: "-200px"}, {duration: 1000});
	$(".subscribe").mouseenter(function() {
		$(this).animate({left: "0px"}, {duration: 500});
	}).mouseleave(function() {
		$(this).animate({left: "-200px"}, {duration: 500});
	})

	// var icon = $('.icon');
	// for(i=0; i<icon.length; i++) {
	// 	icon.classList.add('me');
	// }
	
	

});