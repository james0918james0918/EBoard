<?php
session_start();
$userName = $_POST['userName'];
$password = $_POST['password'];

$url =  "http://140.112.107.81:5000/login";
$data = array('acc' => $userName, 'pwd' => $password);

// use key 'http' even if you send the request to https://..
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
$result = trim($result);

if (strcmp($result, "\"successful\"") == 0) {
  $_SESSION['userName'] = $userName;
  $_SESSION['password'] = $password;
  echo "login";
} else{
  echo "fail";
}

?>
