<?php
session_start();
?>

<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Animated Login Form</title>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">

  <link rel='stylesheet prefetch' href='http://fonts.googleapis.com/css?family=Roboto+Slab'>

<style>
      /* NOTE: The styles were added inline because Prefixfree needs access to your styles and they must be inlined if they are on local disk! */
      * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
  background-color: #F15A5C;
  font-family: "Roboto Slab", serif;
  color: white;
}

.preload * {
  transition: none !important;
}

label {
  display: block;
  font-weight: bold;
  font-size: small;
  text-transform: uppercase;
  font-size: 0.7em;
  margin-bottom: 0.35em;
}

input[type="text"], input[type="password"] {
  width: 100%;
  border: none;
  padding: 0.5em;
  border-radius: 2px;
  margin-bottom: 0.5em;
  color: #333;
}
input[type="text"]:focus, input[type="password"]:focus {
  outline: none;
  box-shadow: inset -1px -1px 3px rgba(0, 0, 0, 0.3);
}

button {
  padding-left: 1.5em;
  padding-right: 1.5em;
  padding-bottom: 0.5em;
  padding-top: 0.5em;
  border: none;
  border-radius: 2px;
  background-color: #7E5AF1;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.25);
  color: white;
  box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.45);
}

small {
  font-size: 1em;
}

.login--login-submit {
  float: right;
}

.login--container {
  width: 600px;
  background-color: #F15A5C;
  margin: 0 auto;
  position: relative;
  top: 25%;
}

.login--toggle-container {
  position: absolute;
  background-color: #F15A5C;
  right: 0;
  line-height: 2.5em;
  width: 50%;
  height: 120px;
  text-align: right;
  cursor: pointer;
  transform: perspective(1000px) translateZ(1px);
  transform-origin: 0% 0%;
  transition: all 1s cubic-bezier(0.06, 0.63, 0, 1);
  backface-visibility: hidden;
}
.login--toggle-container .js-toggle-login {
  font-size: 4em;
  text-decoration: underline;
}
.login--active .login--toggle-container {
  transform: perspective(1000px) rotateY(180deg);
  background-color: #bc1012;
}

.login--username-container, .login--password-container {
  float: left;
  background-color: #F15A5C;
  width: 50%;
  height: 120px;
  padding: 0.5em;
}

.login--username-container {
  transform-origin: 100% 0%;
  transform: perspective(1000px) rotateY(180deg);
  transition: all 1s cubic-bezier(0.06, 0.63, 0, 1);
  background-color: #bc1012;
  backface-visibility: hidden;
}
.login--active .login--username-container {
  transform: perspective(1000px) rotateY(0deg);
  background-color: #F15A5C;
}

footer {
  position: absolute;
  bottom: 12px;
  left: 20px;
}

.loader {
    position: absolute;
    top: 150px;
    left: 800px;
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 300px;
    height: 300px;
    animation: spin 2s linear infinite;
    z-index: 500:
}

.mask {
  color: #FFFFFF;
  background-color: #FFFFFF;
  opacity: 0.5;
  width:100%;
  height: 100%;
  z-index: 499;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js"></script>
<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src="js/index.js"></script>
<script type="text/javascript">
  $(document).ready(function() {
    $("#login").click(function(){
      login();
    });

    $(document).keypress(function(e) {
        if(e.which == 13) {
            login();
        }
    });

  });
  function anti_a(ii){
       var pattern = new RegExp("[~'!@#$%^&*()-+_=:];?></\\}{|\",.`");
        if(ii != "" && ii != null){  
                  if(pattern.test(ii)){  
                      return true;  
                  }
                  else if(ii.length != 9){
                      return true;
                  }
                  else{
                      return false;
                  }
        }
        
  }
  function anti_p(ii){
    var pattern = new RegExp("[~'!@#$%^&*()-+_=:];?></\\}{|\",.`");
        if(ii != "" && ii != null){  
                  if(pattern.test(ii)){  
                    return true;  
                  }
                  else if(ii.length <8 || ii.length >24){
                    return true;
                  }
                  else{
                    return false;  
                  }
        }
  }
  function login(){
    if(anti_a( $("#userName").val())||anti_p( $("#password").val())){  //帳密格式檢驗
      alert("invalid format, please enter the account and password of Ceiba");
      return;
  } 
    $(".loader, .mask").show();
    $("#login").attr("disabled", "disabled");
    var data = new Object();
    data.userName = $("#userName").val();
    data.password = $("#password").val();
    $.ajax({
      async : true,
      url: "login.php",
      data: data,
      type: "POST",

      success: function(result){
        $(".loader, .mask").hide();
        $("#login").removeAttr("disabled");
        if(result == "login"){
          //導回主頁
          window.location.replace("../index.php")
        } else {
          alert("failed login");
        }
    }});
  }

</script>
</head>

<body>
  <div class='preload login--container'>
  <div class='login--form'>
    <div class='login--username-container'>
      <label>Username</label>
      <input autofocus placeholder='Username' type='text' id="userName">
    </div>
    <div class='login--password-container'>
      <label>Password</label>
      <input placeholder='Password' type='password' id="password">
      <button class='js-toggle-login login--login-submit' id="login">Login</button>
    </div>
  </div>

  <div class='login--toggle-container'>
    <small>Hi,</small>
    <div class='js-toggle-login'>Login</div>
    <small>wait please</small>
  </div>
</div>

<div class="mask" style="display:none"></div>
<div class="loader" style="display:none"></div>

<!-- <footer>
  <script>
  !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}
  (document, 'script', 'twitter-wjs');
  </script>
</footer> -->

</body>
</html>
