<?php
	session_start();
	$_SESSION["grid_enabled"] == "true" ?
		$display = "block":
		$display = "none";
?>
<!doctype html>
<html>
	<head>
		<title>Game.js</title>
		<link href="game.css" rel="stylesheet">
		<style>
			#x1, #x2, #x3,
			#y1, #y2, #y3 {
				display: <?php echo $display;?>;
				position:fixed;
				background-color:#f90;
				-webkit-user-select:none;
				-moz-user-select:none;
			}
		</style>
	</head>
	<body>
		<!-- X -->
		<div id="x1"></div>
		<div id="x2"></div>
		<div id="x3"></div>
		<!-- Y -->
		<div id="y1"></div>
		<div id="y2"></div>
		<div id="y3"></div>
		<div id="display"><p>Pausa</p></div>
		<div id="scoreboard"><p>Punteggio: <span id="score">0</span></p></div>
		<div id="game">
			<div id="pg"></div>
		</div>
	</body>
</html>
<script>
	<?php
	echo 'var ';
	switch($_SESSION["points"]) {
		case "5":
			echo 'fn = 5;';
			break;
		case "10":
			echo 'fn = 10;';
			break;
		case "15":
			echo 'fn = 15;';
			break;
		case "20":
			echo 'fn = 20;';
			break;
	}
	echo 'var ';
	switch($_SESSION["difficulty"]) {
		case "easy":
			echo 'speed = 0.5';
			break;
		case "medium":
			echo 'speed = 0.4';
			break;
		case "hard":
			echo 'speed = 0.3';
			break;
		case "extreme":
			echo 'speed = 0.05';
			break;
	}
	?>
</script>
<script type="application/x-javascript" src="game.js"></script>
<script type="application/x-javascript" src="debug.js"></script>
