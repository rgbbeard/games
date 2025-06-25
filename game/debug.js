/*
Debug tool v:2.0 16-03-2020
*/
var dom = document;
var debugActive = false;
var css = dom.createElement('style');
css.textContent = ".debug {outline:dashed 1px #0f0 !important;}";
dom.body.appendChild(css);
setInterval(function() {
    var t = dom.querySelectorAll("*");
    if(debugActive === true) {
        for(let x=0;x<t.length;x++) {
            t[x].classList.add("debug");
        }
    }
    else {
        for (let x = 0;x<t.length;x++) {
			t[x].classList.remove("debug");
		}
    }
}, 0);
