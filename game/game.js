var
dom = document, win = window,
ww = win.innerWidth,
wh = win.innerHeight,
bgs = ["f00", "ff0", "0f0", "0ff", "00f"],
direction = "down", stepX = 0, stepY = 0,
currentScore = 0,
scoreboard = dom.querySelector("#scoreboard"),
game = dom.querySelector("#game"),
pg = dom.querySelector("#pg");
if(ww<=768) {
	fn = 5;
}
//Grid system
let hfq = wh/4;
let hlq = hfq*3;
let wfq = ww/4;
let wlq = wfq*3;
function move() {
	setInterval(function() {
		if (direction === "up") {
			pg.style.top = (stepY--)+"%";
			if (stepY <= 1) {
				stepY = 99;
			}
		}
		else if (direction === "down") {
			pg.style.top = (stepY++)+"%";
			if (stepY >= 99) {
				stepY = 1;
			}
		}
		else if (direction === "left") {
			pg.style.left = (stepX++)+"%";
			if (stepX >= 99) {
				stepX = 1;
			}
		}
		else if (direction === "right") {
			pg.style.left = (stepX--)+"%";
			if (stepX <= 1) {
				stepX = 99;
			}
		}
		//Get head current position
		var hposX = pg.style.left;
		var hposY = pg.style.top;
		var food = dom.querySelectorAll(".food");
		for (let e = 0;e<food.length;e++) {
			//Increment snake length and update score
			var fposX = food[e].style.left;
			var fposY = food[e].style.top;
			if (hposX === fposX && hposY === fposY) {
				currentScore += 20;
				//Add score animation
				scoreboard.classList.add("animate");
				dom.querySelector("#score").textContent = currentScore;
				game.removeChild(food[e]);
			}
		}
	}, speed*1000);
}
//Check scoreboard animation active
//Check eaten food
setInterval(function() {
	if (scoreboard.classList.contains("animate")) {
		setTimeout(function() {
			scoreboard.classList.remove("animate");
		}, 2000);
	}
	var food = dom.querySelectorAll(".food");
	if (food.length === 0) {
		generateFood();
	}
}, 0);
//Change direction
//Desktop mode
win.addEventListener("keydown", function(e) {
	if(e.key == "ArrowUp" || e.which == "38" || e.code == "ArrowUp") {
		direction = "up";
		dom.querySelector("#display").style.display = "none";
	}
	else if(e.key == "ArrowDown" || e.which == "40" || e.code == "ArrowDown") {
		direction = "down";
		dom.querySelector("#display").style.display = "none";
	}
	else if(e.key == "ArrowLeft" || e.which == "37" || e.code == "ArrowLeft") {
		direction = "right";
		dom.querySelector("#display").style.display = "none";
	}
	else if(e.key == "ArrowRight" || e.which == "39" || e.code == "ArrowRight") {
		direction = "left";
		dom.querySelector("#display").style.display = "none";
	}
	else if(e.key == "(Space character)" || e.which == "32" || e.code == "Space") {
		direction = "none";
		dom.querySelector("#display").style.display = "table";
	}
});
//Mobile mode
game.addEventListener("touchstart", function(e) {
	startFingerX = Math.round(e.touches[0].clientX);
	startFingerY = Math.round(e.touches[0].clientY);
	//Left
	if(startFingerX<(ww/2) && startFingerY>hfq && startFingerY<hlq) {
		startPoint = "l";
	}
	//Right
	else if(startFingerX>(ww/2) && startFingerY>hfq && startFingerY<hlq) {
		startPoint = "r";
	}
	//Top
	else if(startFingerY<(wh/2) && startFingerX>wfq && startFingerX<wlq) {
		startPoint = "t";
	}
	//Bot
	else if(startFingerY>(wh/2) && startFingerX>wfq && startFingerX<wlq) {
		startPoint = "b";
	}
	this.addEventListener("touchmove", ()=> {
		fingerX = Math.round(e.touches[0].clientX);
		fingerY = Math.round(e.touches[0].clientY);
		switch(startPoint) {
			case "l":
				direction = "left";
				break;
			case "r":
				direction = "right";
				break;
			case "t":
				direction = "down";
				break;
			case "b":
				direction = "up";
				break;
		}
	});
});
function generateFood() {
	for (let p = 0;p<=fn;p++) {
		var xPosition = Math.round(Math.random()*100);
		var yPosition = Math.round(Math.random()*100);
		var foodFrame = dom.createElement("div");
		if(xPosition<=1) {
			xPosition = 1;
		}
		if(yPosition<=1) {
			yPosition = 1;
		}
		if(xPosition>=99) {
			xPosition = 99;
		}
		if(yPosition>=99) {
			yPosition = 99;
		}
		var frameBackgroundColorIndex = Math.round(Math.random()*bgs.length);
		var frameBackgroundColor = bgs[frameBackgroundColorIndex];
		foodFrame.setAttribute("class", "food");
		foodFrame.setAttribute("style", `left:${xPosition}%;top:${yPosition}%;background-color:#${frameBackgroundColor};`);
		game.appendChild(foodFrame);
	}
}
//Start game
generateFood();
move(direction, speed);
