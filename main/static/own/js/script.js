let d = document;
const social_icons = d.querySelectorAll('path.a'),
	  toogle_btn_parts = d.querySelectorAll('#toogle_btn div');

var background_color = 'var(--dark)',
	nav_color = 'var(--neon_violet)',
	nav_bgcolor = 'var(--dark)',
    darkmode = true;


window.addEventListener('scroll', function() {


	if (darkmode) {
		background_color = 'var(--dark)';
		counter_color = 'var(--neon_violet)';
		nav_color = 'var(--neon_violet)';
		nav_bgcolor = 'var(--dark)';
	}
	else {
		background_color = 'white';
		counter_color = 'var(--dark)';
		nav_color = 'white';
		nav_bgcolor = 'var(--dark)';
	}


	header.style.backgroundColor = background_color;
	about_us.style.backgroundColor = background_color;
	team_section.style.backgroundColor = background_color;
	last_work_section.style.backgroundColor = background_color;

	navbar.style.color = nav_color;
	navbar.style.backgroundColor = nav_bgcolor;



	for(var i = 0; i < social_icons.length; i++) {
		social_icons[i].style.fill = nav_color;
	}

	for(var i = 0; i < toogle_btn_parts.length; i++) {
		toogle_btn_parts[i].style.backgroundColor = nav_color;
	}



	//console.log(window.pageYOffset);
	//console.log('team: ' + team_section.offsetTop);


	if(window.pageYOffset > (team_member_last.offsetTop+team_member_last.offsetHeight/2)) {

		darkmode = false;

		last_work_heading.classList.add('active');
		last_work_block.classList.add('active');


		team_block.classList.remove('active');
		team_heading.classList.remove('active');

		if(window.pageYOffset > (team_member_last.offsetTop+team_member_last.offsetHeight)) {
			
		}
	}

	else if (window.pageYOffset > feature_item_last.offsetTop) {
		darkmode = true;

		last_work_block.classList.remove('active');
		last_work_heading.classList.remove('active');

		who_are_we_heading.classList.remove('active');		

		features_block.classList.remove('active');

		team_block.classList.add('active');
		team_heading.classList.add('active');
	} 

	

	else if(window.pageYOffset > header.offsetHeight / 2) {

		darkmode = false;

		navbar.style.padding = '1em 0';

		team_block.classList.remove('active');	
		team_heading.classList.remove('active');

		who_are_we_heading.classList.add('active');
		features_block.classList.add('active');

	} 

	else {
		darkmode = true;

		navbar.style.padding = '';	

		who_are_we_heading.classList.remove('active');		
		features_block.classList.remove('active');
	}





});



	 //TOOGLE BTN

var active = false;

toogle_btn.addEventListener('click', function() {
	if(active == false) {
		this.classList.add('active');
		header_menu.classList.add('mobile-active');
		active = true;
	}else {
		this.classList.remove('active');
		header_menu.classList.remove('mobile-active');
		active = false;
	}
});