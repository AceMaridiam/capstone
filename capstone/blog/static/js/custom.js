$(document).ready(function() {

	function isValidEmail(email)
	{
    	return /^[a-z0-9]+([-._][a-z0-9]+)*@([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,4}$/.test(email)
        && /^(?=.{1,64}@.{4,64}$)(?=.{6,100}$).*/.test(email);
	}

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

	// email validation
	// if($("input#email-address").getVerimailStatus() < 0){
	//     alert('Nope');
	// }else{
	//     alert('Yipee!!');
	// }

	// $("input").verimail({
	//     messageElement: "p#status-message"
	// });

	$('.subscribe .btn').click(function() {
		var email = $('.subscribe input').val();
		// console.log(isValidEmail(email));
		if (isValidEmail(email)) {
			console.log('Yipee!');
		}
		else {
			console.log('Nope');
		}
	})



	// hover info boxes for tool icons
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	})
	// hover info boxes text content
	$(".icon").mouseenter(function(){
		if($(this).hasClass('icon-technical-pen')) {
	    	$(this).attr('data-original-title', "Pen - 0.5 & 0.7 Micron");
	    }
	    if($(this).hasClass('icon-compass')) {
	    	$(this).attr('data-original-title', "Compass - An antique used to get highly accurate circles");
	    }
	    if($(this).hasClass('icon-pen')) {
	    	$(this).attr('data-original-title', "Dipping Pen - used with hand mixed ink(s)");
	    }
	    if($(this).hasClass('icon-lightbox')) {
	    	$(this).attr('data-original-title', "Lightbox - to help draw and transer shapes");
	    }
	    if($(this).hasClass('icon-airbrush')) {
	    	$(this).attr('data-original-title', "Airbrush - for smooth and elegant color transitions");
	    }
	});

	
	
	

});