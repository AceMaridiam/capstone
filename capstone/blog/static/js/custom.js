$(document).ready(function() {

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

});