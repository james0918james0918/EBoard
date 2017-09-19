<?php
$link = mysqli_connect("140.112.107.81:13306", "root" , "2016sdmtest" , "eboard");
	if (mysqli_connect_errno())
	  {
	  echo "Failed to connect to MySQL: " . mysqli_connect_error();
	  }
	mysqli_query($link, "set names utf8");
session_start();

$userName = $_SESSION['userName'];
$option = $_POST['option'];
$web_id = $_POST['web_id'];
if($option == true){
	$sql = "insert into selection values('".$userName."','".$web_id."','')" ;
	// echo $sql;
}
else{
	$sql = "delete from selection where member_id = '".$userName."' and web_id = '".$web_id."'" ;
	// echo $sql;
}

mysqli_query($link, $sql);

?>