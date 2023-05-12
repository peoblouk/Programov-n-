// (c) 2000-2007 by Gemius SA

function gemius_parameters() {
	var d=document;
	var href=new String(d.location.href);
	var ref;
	if (d.referrer) { ref = new String(d.referrer); } else { ref = ""; }
	var t=typeof Error;
	if(t!='undefined') {
		eval("try { if (typeof(top.document.referrer)=='string') { ref = top.document.referrer } } catch(gemius_ex) { }")
	}
	var url='&tz='+(new Date()).getTimezoneOffset()+'&href='+escape(href.substring(0,299))+'&ref='+escape(ref.substring(0,299));
	if (screen) {
		var s=screen;
		if (s.width) url+='&screen='+s.width+'x'+s.height;
		if (s.colorDepth) url+='&col='+s.colorDepth;
	}
	return url;
}

if (typeof gemius_identifier != 'undefined') {
	var gemius_proto;
	if(document.location && document.location.protocol)
		gemius_proto = 'http'+((document.location.protocol=='https:')?'s':'')+':';
	else
		gemius_proto = 'http:';
	var gemius_url = gemius_proto+'//cz.hit.gemius.pl/_'+(new Date()).getTime()+'/redot.gif?l=11&id='+gemius_identifier+gemius_parameters();
	if (typeof window.gemius_images == 'undefined') {
	        window.gemius_images = new Array();
	}
	var gemius_l = window.gemius_images.length;
	if (typeof gemius_sem == 'undefined') {
	        gemius_sem=0;
	}
	if (gemius_l<=gemius_sem) {
	        window.gemius_images[gemius_l]=new Image();
	        window.gemius_images[gemius_l].src = gemius_url;
	}
	gemius_sem++;
}