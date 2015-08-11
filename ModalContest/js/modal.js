var count = 0;
var cookieName = "modalCount";
function updateCookie(key, value){
	var expiration = new Date();
	expiration.setFullYear(expiration.getFullYear()+1);
	cookieContent = key+"="+value+";expires="+expiration.toUTCString();
	document.cookie = cookieContent;
}
function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}
function openModal() {
	var myDiv = $("#myModal");
	myDiv.modal();
	count++
	updateCookie(cookieName, count);
}
function scrollTrigger(){
	var height = $('#about').height();
	if($(window).scrollTop() >= $(document).height() - $(window).height() - height) {
    	var cookie = getCookie(cookieName);
    	if(cookie != null && cookie == 0)
    		openModal();
    	count++;
	 }

}

//interval in ms (s * 1000 ms/ s)
var interval = 25000
$(document).ready(function(){ 
	setInterval(function(){
		var cookie = getCookie(cookieName);
	    if(cookie != null && cookie == 0)
			openModal();
	}, interval);
}, interval);
//scroll handler
$(window).scroll(function() {
	scrollTrigger();
});


