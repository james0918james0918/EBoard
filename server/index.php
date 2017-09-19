<?php
	$link = mysqli_connect("140.112.107.81:13306", "root" , "2016sdmtest" , "eboard");
	if (mysqli_connect_errno())
	  {
	  echo "Failed to connect to MySQL: " . mysqli_connect_error();
	  }
	mysqli_query($link, "set names utf8");
	session_start();
?>
<?php
	function printDiv($id, $link, $course_Info){
		echo '<div class="col-md-3 ser-left2" id="w'.$id.'">';
			$course_tName = mysqli_query($link, "select Web_name from website where Web_ID = '".$id."'");
			$course_Name = mysqli_fetch_row($course_tName);
			$tmp_course_name = $course_Name[0];
			echo '<button type="button" class="close btnx" aria-label="Close" value="'.$id.'" id="x'.$id.'">';
  				echo '<span aria-hidden="true">&times;</span>';
			echo '</button>';
			echo '<h3>'. $tmp_course_name .'</h3>';
			echo '<div id="myCarouselw'. $id .'" class="carousel slide">';
				$total_row = mysqli_num_rows($course_Info);
				$slide = (int)$total_row/3;
				echo '<ol class="carousel-indicators">';
				echo '<li data-target="#myCarouselw'. $id. '" data-slide-to="0" class="active"></li>';
				for($r=1; $r<$slide; $r++){
					echo '<li data-target="#myCarouselw'. $id .'" data-slide-to="'.$r.'"></li>';
				}
				echo '</ol>';
				echo '<div class="carousel-inner">';
	}

	function printINFO($course_Info, $id, $num){
		for($j=1; $j<=mysqli_num_rows($course_Info); $j+=3){
			if($j==1){
				echo '<div class="active item">';
				for($k=$j; $k<$j+3; $k++){
					if($k <=mysqli_num_rows($course_Info)){
						$rs = mysqli_fetch_row($course_Info);
						$information = $rs[6];
						$URL = $rs[5];
						$anouce_Date = $rs[3];
						$start_date = $rs[8];
						$end_date = $rs[9];
						if($URL == NULL){
							noURL($id, $num, $information, $k, $start_date, $end_date, $anouce_Date);
					    }else{
					     	yesURL($id, $num, $information, $k, $start_date, $end_date, $anouce_Date, $URL);
					    }
						$num++;
					}
				}
				echo '</div>';
			}
			if($j>3 && $j%3==1){
				echo '<div class="item">';
				for($k=$j; $k<$j+3; $k++){
					if($k <=mysqli_num_rows($course_Info)){
						$rs = mysqli_fetch_row($course_Info);
						$information = $rs[6];
						$URL = $rs[5];
						$anouce_Date = $rs[3];
						$start_date = $rs[8];
						$end_date = $rs[9];
						if($URL == NULL){
							noURL($id, $num, $information, $k, $start_date, $end_date, $anouce_Date);
					    }else{
					    	yesURL($id, $num, $information, $k, $start_date, $end_date, $anouce_Date, $URL);
					    }
					    $num++;
					}
				}
				echo '</div>';
			}
		}

					echo '</div>';
				echo '</div>';
			echo '</div>';
	}

	function noURL($id, $num, $information, $k, $start_date, $end_date, $anouce_Date){
		echo '<div class="accordion" id="accordion2">';
			echo '<div class="accordion-group">';
				echo '<div class="accordion-heading">';
					echo '<a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapse'.$id. $num .'">';
						anouce($k, $start_date, $end_date, $anouce_Date);
					echo '</a>';
				echo '</div>' ;
			echo '<div id="collapse'.$id. $num .'" class="accordion-body collapse in">';
		echo '<div class="accordion-inner">';
			echo $information;
			echo '</div>';
		echo '</div>';
	echo '</div>';
echo '</div>';
	}

	function yesURL($id, $num, $information, $k, $start_date, $end_date, $anouce_Date, $URL){
		echo '<div class="accordion" id="accordion2">';
			echo '<div class="accordion-group">';
				echo '<div class="accordion-heading">';
					echo '<a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapse'.$id. $num .'">';
				       anouce($k, $start_date, $end_date, $anouce_Date);
					echo '</a>';
				echo '</div>' ;
			echo '<div id="collapse'.$id. $num .'" class="accordion-body collapse in">';
		echo '<div class="accordion-inner">';
			echo '<a target="_blank" href="'. $URL . '">'. $information.'</a>';
			echo '</div>';
		echo '</div>';
	echo '</div>';
echo '</div>';
	}

	function anouce($k, $start_date, $end_date, $anouce_Date){
		if($start_date != null){
			echo $k.'. ['.$start_date.' ~ '. $end_date .'] ';
		}else if($anouce_Date !=null){
			echo $k.'. ['. $anouce_Date . '] ';
		}else if($anouce_Date == null && $start_date == null){
			echo $k.'. ';
		}
	}
?>
<!DOCTYPE HTML>
<html>
<head>
<title>Home</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Thronged Responsive web template, Bootstrap Web Templates, Flat Web Templates, Andriod Compatible web template,
Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyErricsson, Motorola web design" />
<script type="applijewelleryion/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<link href="css/bootstrap.css" rel='stylesheet' type='text/css' />
<!-- Custom Theme files -->
<link href="css/style.css" rel='stylesheet' type='text/css' />
<script src="js/jquery-1.11.1.min.js"></script>
<!--webfonts-->
<link href='https://fonts.googleapis.com/css?family=Antic' rel='stylesheet' type='text/css' />
<link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,400,300,600,700|Six+Caps' rel='stylesheet' type='text/css' />
   <!--//webfonts-->
<script type="text/javascript" src="js/bootstrap.js"></script>
<!------ Light Box ------>
<link rel="stylesheet" href="css/swipebox.css">
    <script src="js/jquery.swipebox.min.js"></script>
    <script type="text/javascript">
		jQuery(function($) {
			$(".swipebox").swipebox();
		});
	</script>
    <!------ Eng Light Box ------>
<script type="text/javascript" src="js/move-top.js"></script>
<script type="text/javascript" src="js/easing.js"></script>
<script type="text/javascript">
$(document).ready(function($) {
	$().UItoTop({ easingType: 'easeOutQuart' });

	$(".scroll").click(function(event){
		event.preventDefault();
		$('html,body').animate({scrollTop:$(this.hash).offset().top},1200);
	});

	getCeiba();
});

function getCeiba(){
	$.ajax({
		async : true,
		url: "getCeiba.php",
		type: "POST",
		dataType: "json",

		success: function(result){
			console.log(result);
			if(result != "not login yet"){
				var i = 1;
				$.each(result, function(key, value){
					showCeiba(key, value, i);
					i++;
				});
			}
		}
	});
}

function showCeiba(name, contents, num){
	console.log("aaa" + name + "bbb" + contents);
	var target = $("#services .container");
	var display = "";

	display += '<div class="col-md-3 ser-left2">'
	display += '	<h3>' + name + '</h3>'
	display += '	<div id="myCarouselCeiba' + num + '" class="carousel slide">'
	display += '		<ol class="carousel-indicators">'
	display += '			<!-- 印 (總訊息數/3) 個li -->'
	display += '			<li data-target="#myCarouselCeiba" data-slide-to="0" class="active"></li>'

	for (var i = 1; i < (contents.length / 3); i++){
		display += '			<li data-target="#myCarouselCeiba" data-slide-to="' + i + '"></li>**'
	}

	display += '		</ol>'
	display += '		<div class="carousel-inner"><!-- 以下的編號&訊息號為全域變數且遞增 -->'

	for (var i = 0; i < contents.length; i++){
		var content = contents[i];
		if(i == 0){
			display += '			<div class="active item"><!--訊息號==1的時候印此div -->'
		}

		if((i % 3) == 0 && i != 0){
			display += '			<div class="item"><!--訊息號==4、7、10…的時候印此div -->'
		}

		display += '				<div class="accordion" id="accordion2"><!-- 12行到28行最多3個訊息 -->'
		display += '					<div class="accordion-group">'
		display += '						<div class="accordion-heading">'
		display += '							<a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseCeiba' + num + '' + (i+1) + '">'
		display += '								' + (i+1) + ' [' + content[0] + '] <!-- 舉例：1. [12/29] -->'
		display += '							</a>'
		display += '						</div>'
		display += '						<div id="collapseCeiba' + num + ''  + (i+1) + '" class="accordion-body collapse in">'
		display += '							<div class="accordion-inner">'
		display += '								' + content[1]
		display += '							</div>'
		display += '						</div>'
		display += '					</div>'
		display += '				</div>'

		if((i % 3) == 0){
			display += '			</div>'
		}
	}
	target.append(display);

}

</script>

</head>
<body>
<!-- banner -->
	<div class="banner" id="banner">
		<div class="container">
			<div class="header-bottom">
		<div class="container">
			<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
				<div class="navbar-left">
					<h1><a href="index.php">E-board</a></h1>
				</div>
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
				</div>
				<!--/.navbar-header-->
				<div class="collapse navbar-collapse navbar-right" id="bs-example-navbar-collapse-1">
					<ul class="nav navbar-nav">
						<li><a href="#banner" class="scroll">Home</a></li>
						<li><a href="#about" class="scroll">Activity</a></li>
						<li><a href="#case" class="scroll">Admin</a></li>
						<li><a href="#services" class="scroll">Courses</a></li>
						<li><a href="./login/index.php" class="login">Login</a></li>
						<li><a href="index.php" class="logout">Logout</a></li>
						<li><a href="index_CH.php">中文</a></li>
					</ul>
				</div>
				<!--/.navbar-collapse-->
			</nav>
		</div>
	</div>
			<div class="banner-info">
				<h2>Provide everything you want!</h2>
			</div>
			<div class="sayHI">
				<?php
					echo '<h3>Hello, ' . $_SESSION['userName'].'</h3>';
				?>
			</div>
		</div>
	</div>
<!-- banner -->

<!-- project -->
	<div class="project" id="about">
		<div class="container">
		<div class="title">
			<div class="col-md-4"></div>
			<div class="col-md-4">
				<div class="col-md-3"></div>
				<div class="col-md-4">
					<h2>Activity</h2>
				</div>
				<div class="col-md-4">
					<div class="dropdown">
								<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true">
								    <span class="caret"></span>
								</button>
								<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
									<li role="presentation" class="dropdown-header"><a>Choose your activity</a></li>
									<?php
										$course_name = mysqli_query($link, "select * from website where Web_type<>'課程' and Web_type<>'系所' order by web_id");
										$course_ID = mysqli_query($link, "select * from website where Web_type<>'課程' and Web_type<>'系所' order by web_id");
										for($i=1; $i<=mysqli_num_rows($course_name); $i++){
											$id = mysqli_fetch_row($course_ID);
											$rs = mysqli_fetch_row($course_name);
											$query = "select Web_name, Web_ID from website where Web_ID ='" .$rs[0]."'" ;
											$course_tName = mysqli_query($link, $query);
											$course_Name = mysqli_fetch_row($course_tName);
											if($course_Name[1] == 002) continue;
											echo '<li role="presentation"><a class="btnb" value="'.$id[0].'" id="b'. $id[0] .'">'. $course_Name[0] .'</a></li>';
										}
									?>
								</ul>
					</div>
				</div>
			</div>
		</div>
			<div class="project-top">
				<div class="col-md-6 project-right">
					<img src="images/acti.jpg" alt=" " class="img-responsive">
				</div>
				<div class="col-md-6 project-left">
						        <h3>Open Time</h3>
						    <table class="table table-condensed">
						    	<tr><td></td><td>Library</td><td>Sports Center</td></tr>
								<tr><td>Sunday</td><td>8:00 ~ 17:30</td><td>9:00 ~18:00</td></tr>
								<tr><td>Monday</td><td>8:00 ~ 22:30</td><td>6:00 ~ 22:00</td></tr>
								<tr><td>Tuesday</td><td>8:00 ~ 22:30</td><td>6:00 ~ 22:00</td></tr>
								<tr><td>Wednesday</td><td>8:00 ~ 22:30</td><td>6:00 ~ 22:00</td></tr>
								<tr><td>Thursday</td><td>8:00 ~ 22:30</td><td>6:00 ~ 22:00</td></tr>
								<tr><td>Friday</td><td>8:00 ~ 22:30</td><td>6:00 ~ 22:00</td></tr>
								<tr><td>Saturday</td><td>8:00 ~ 22:30</td><td>9:00 ~ 22:00</td></tr>
							</table>
				</div>
					<div class="clearfix"></div>
			</div>
			<!-- application -->
	<div class="application">

<?php
	$course_ID = mysqli_query($link, "select * from website where Web_type<>'課程' and Web_type<>'系所' order by web_id");
	for($i=1; $i<=mysqli_num_rows($course_ID); $i++){
		$num = $i;
		$id = mysqli_fetch_row($course_ID);
		if($id[0] == 002) continue;
		$q_id = "select * from web_public_information where web_id ='" . $id[0] ."'order by Announcement_Date DESC";
		$course_Info = mysqli_query($link, $q_id);

		printDiv($id[0], $link, $course_Info);
		printINFO($course_Info, $id[0], $num);
	}
?>
	</div>
<!-- /application -->
		</div>
	</div>
	<!-- admin -->
	<div class="case" id="case">
		<div class="container">
		<div class="title">
			<div class="col-md-4"></div>
			<div class="col-md-4">
				<div class="col-md-3"></div>
				<div class="col-md-4">
					<h2>Admin</h2>
				</div>
				<div class="col-md-4">
					<div class="dropdown">
						<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true">
						    <span class="caret"></span>
						</button>
						<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
							<li role="presentation" class="dropdown-header"><a>Choose your admin</a></li>
							<?php
								$course_name = mysqli_query($link, "select * from website where Web_type='系所' order by web_id");
								$course_ID = mysqli_query($link, "select * from website where Web_type='系所' order by web_id");
								for($i=1; $i<=mysqli_num_rows($course_name); $i++){
									$id = mysqli_fetch_row($course_ID);
									$rs = mysqli_fetch_row($course_name);
									$query = "select Web_name, Web_ID from website where Web_ID ='" .$rs[0]."'" ;
									$course_tName = mysqli_query($link, $query);
									$course_Name = mysqli_fetch_row($course_tName);
									if($course_Name[1] == 002) continue;
									echo '<li role="presentation"><a class="btnb" value="'.$id[0].'" id="b'. $id[0] .'">'. $course_Name[0] .'</a></li>';
								}
							?>

						</ul>
					</div>
				</div>
			</div>
		</div>
			<!-- <div class="ser-top"> -->

	<?php
		$course_ID = mysqli_query($link, "select * from website where Web_type='系所' order by web_id");
		for($i=1; $i<=mysqli_num_rows($course_ID); $i++){
			$num = $i;
			$id = mysqli_fetch_row($course_ID);
			if($id[0] == 002) continue;
			$q_id = "select * from web_public_information where web_id ='" . $id[0] ."'order by Announcement_Date DESC";
			$course_Info = mysqli_query($link, $q_id);

			printDiv($id[0], $link, $course_Info);
			printINFO($course_Info, $id[0], $num);
		}
	?>
			<!-- </div> -->
		</div>
	</div>
<!-- /case -->

	<!-- course -->
	<div class="services" id="services">
		<div class="container">
		<div class="title">
			<div class="col-md-4"></div>
			<div class="col-md-4">
				<div class="col-md-3"></div>
				<div class="col-md-4">
					<h2>Courses</h2>
				</div>
				<div class="col-md-4">
					<div class="dropdown">
						<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true">
						    <span class="caret"></span>
						</button>
						<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
							<li role="presentation" class="dropdown-header"><a>Choose your class</a></li>
							<?php
								$course_name = mysqli_query($link, "select * from website where Web_type='課程' order by web_id");
								$course_ID = mysqli_query($link, "select * from website where Web_type='課程' order by web_id");

								for($i=1; $i<=mysqli_num_rows($course_name); $i++){
									 $rs = mysqli_fetch_row($course_name);
									 $id = mysqli_fetch_row($course_ID);
									 $query = "select Web_name from website where Web_ID ='" .$rs[0]."'" ;
									 $course_tName = mysqli_query($link, $query);
									 $course_Name = mysqli_fetch_row($course_tName);
									 echo '<li role="presentation"><a class="btnb" value="'.$id[0].'" id="b'. $id[0] .'">'. $course_Name[0] .'</a></li>';
								}
							?>
						</ul>
					</div>
				</div>
			</div>
		</div>
			<!-- <div class="ser-top"> -->

	<?php //爬蟲課程
		$course_ID = mysqli_query($link, "select * from website where Web_type='課程' order by web_id");
		for($i=1; $i<=mysqli_num_rows($course_ID); $i++){
			$num = $i;
			$id = mysqli_fetch_row($course_ID);
			$q_id = "select * from web_course_information where web_id ='" . $id[0] ."'order by Announcement_Date DESC";
			$course_Info = mysqli_query($link, $q_id);
				printDiv($id[0], $link, $course_Info);
				printINFO($course_Info, $id[0], $num);
		}
	?>
			<!-- </div> -->
		</div>
	</div>
<!-- /services -->
</body>
</html>

<?php //顯示user name
	if($_SESSION){
		echo '<script>';
			echo '$(".logout, .sayHI").css("display" , "block");';
			echo '$(".login").css("display" , "none");';
		echo '</script>';
	}
?>

<?php //顯示user上次的內容

	echo '<script>';
	//各訊息區塊消失
		  for($i=1; $i<=9; $i++){
		    echo '$("#w00'.$i.'").css("display", "none");';
		  }
		  for($j=10; $j<=99; $j++){
		   echo '$("#w0'.$j.'").css("display", "none");';
		  }
	echo '</script>';

	if($_SESSION){
		$member_id = $_SESSION['userName'];//這邊要改去接Id
		$sql = "SELECT * FROM website where web_id in ( SELECT Web_ID from selection where Member_ID = '".$member_id."') ";
		$user_table = mysqli_query($link, $sql);
		echo '<script>';
		for($i=1; $i<=mysqli_num_rows($user_table); $i++){
			$user_want_to_see = mysqli_fetch_row($user_table);
			echo '$("#w'.$user_want_to_see[0].'").css("display" , "block");';
			echo '$("#b'.$user_want_to_see[0].'").css("display", "none");';
		}
		echo '</script>';
	}
?>
