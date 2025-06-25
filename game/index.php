<?php
	session_start();
?>
<!doctype html>
<html>
	<head>
		<title>Game.js</title>
		<link href="game.css" rel="stylesheet">
		<style>

		</style>
	</head>
	<body>
		<form method="post">
			<h4>Scegli la modalità da giocare</h4>
			<div class="select">
				<input type="hidden" name="difficulty">
				<input class="fakeSelect" type="text" placeholder="Seleziona un'opzione" readonly>
				<ul class="selectItems">
					<li data-value="easy">Facile</li>
					<li data-value="medium">Media</li>
					<li data-value="hard">Difficile</li>
					<li data-value="extreme">Estrema</li>
				</ul>
			</div>
			<hr>
			<h4>Numero di punti per livello: <span style="display:inline-block;width:20px;height:20px;background-color:#ff0;vertical-align:bottom;border:solid 1px #000;border-radius:3px;"></span></h4>
			<div class="select">
				<input type="hidden" name="points">
				<input class="fakeSelect" type="text" placeholder="Seleziona un'opzione" readonly>
				<ul class="selectItems">
					<li data-value="5">5</li>
					<li data-value="10">10</li>
					<li data-value="15">15</li>
					<li data-value="20">20</li>
				</ul>
			</div>
			<hr>
			<div class="switchbox">
				<h4>Mostra quadranti di tocco <span class="helpBtn"><i>?</i><div class="helpBox">Mostra la griglia di tocco per le direzioni del personaggio.<br>Raccomandato se è la tua prima esperienza qui.</div></span></h4>
				<input id="grid_enabler" type="checkbox" name="grid_enabler">
				<label for="grid_enabler"></label>
			</div>
			<input class="btn-custom" type="submit" name="start" value="Inizia!">
			<?php
				if(isset($_POST["start"])) {
					isset($_POST["grid_enabler"]) ?
						$_SESSION["grid_enabled"] = true:
						$_SESSION["grid_enabled"] = false;
					empty($_POST["difficulty"]) ?
						$_SESSION["difficulty"] = "easy":
						$_SESSION["difficulty"] = $_POST["difficulty"];
					empty($_POST["points"]) ?
						$_SESSION["points"] = 10:
						$_SESSION["points"] = $_POST["points"];
					header("location: game.php");
				}
			?>
		</form>
	</body>
</html>
<script>
	var dom = document, win = window;
	win.onload = function() {
		var select = dom.querySelectorAll(".select");
		for(let x = 0;x<select.length;x++) {
			var input = select[x].querySelector(".fakeSelect");
			var itemContainer = select[x].querySelector("ul");
			itemContainer.style.display = "none";
			var item = select[x].querySelectorAll(".selectItems li");
			input.onclick = function() {
				this.parentNode.querySelector("ul").style.display === "none" ?
					this.parentNode.querySelector("ul").style.display = "block":
					this.parentNode.querySelector("ul").style.display = "none";
			};
			for(let y = 0;y<item.length;y++) {
				item[y].onclick = function() {
					var realInput = this.parentNode.parentNode.querySelector('input[type="hidden"]');
					var input = this.parentNode.parentNode.querySelector(".fakeSelect");
					//Remove selected items
					var selected = dom.querySelectorAll(".selectedItem");
					for(let s = 0;s<selected.length;s++) {
						selected[s].classList.remove("selectedItem");
					}
					this.classList.add("selectedItem");
					this.parentNode.style.display = "none";
					var newValue = this.dataset.value;
					var newContent = this.textContent;
					input.value = newContent;
					realInput.value = newValue;
				}
			}
		}
	};
</script>
<script type="application/x-javascript" src="debug.js"></script>
