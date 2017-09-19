<?php
session_start();

$userName = "";
$password = "";

if(isset($_SESSION['userName'])){
  $userName = $_SESSION['userName'];
}
if(isset($_SESSION['password'])){
  $password = $_SESSION['password'];
}

if(($userName === "") || ($password === "")){
  echo "not login yet";
} else {
  $url =  "http://140.112.107.81:5000/ceiba";
  $data = array('acc' => $userName, 'pwd' => $password);

  // use key 'http' even if you send the request to https://..
  $options = array(
      'http' => array(
          'header'  => "Content-type: application/x-www-form-urlencoded",
          'method'  => 'POST',
          'content' => http_build_query($data)
      )
  );
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);

  echo $result;
}

?>
