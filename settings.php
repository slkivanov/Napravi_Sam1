<!DOCTYPE html>
<html> 
	<head>
		<meta charset="UTF-8">
		<link href="Style/Styles.css" rel="stylesheet" type="text/css"/>
		<title></title>
	</head> 
	<body>
		<div id="container"> 
			<div id="head"> <?php include 'version.php'; echo $title; ?> </div>
			<div id="body" style = "height: 630px;">     
				<div class="bodyContent">
				<form action="Connect_to_settings.php" method="post">
					<h3>НАСТРОЙКИ ЗА НАГРЕВАТЕЛИ И ПОМПИ</h3>
					<b>----  ЦИРКУЛ. ПОМПА МЕЖДУ Бойлер_Солар И Бойлер_Котел---- </b><br><br>
				<?php include_once 'config.inc.php';  
				$db=new Connect_MySql();
				$sql="SELECT * FROM `settings`ORDER BY id DESC LIMIT 1";
				$result=$db->execute($sql);
				$row=$db->fetch_row($result);?>
				<!--  Switching PUMP_ON_OFF-------------------------------------------------
					Data from table "correction"--------------------------------------------
						if  Set_S6_PumpStatus == 1 and (S3_BoilerTop >= 40 and (Time > 700 and Time <= 2300)):-->
						<b>Включи ръчно</b>  помпата ако t* Бойлер_Солар > 
								<input type='text' name='temp1' size='2' maxlength='5' value = '<?php echo $row['temp1']; ?>' > С* 
						в интервала: > <input type='text' name='StartTime' size='3' maxlength='5' value = '<?php echo $row['StartTime']; ?>' > ч.
								<= <input type='text' name='EndTime' size='4' maxlength='5' value = '<?php echo $row['EndTime']; ?>' > ч.<br>
						
				<!--Data from Pico IP--------------------------------------------------------   
					   elif S3_BoilerTop >= 55.0 and (Time > 1000 and Time <= 1200) 
							or (K3_BoilerTop >= 40.0 and K3_BoilerTop - S3_BoilerTop > 5.0) 
							and S5_BoilerStatus == 0.0:-->
						<b>Включи автом.</b> помпата ако t* Бойлер_Солар  >
								<input type='text' name='temp2' size='2' maxlength='5' value = '<?php echo $row['temp2']; ?>' > С*
						в интервала: > <input type='text' name='Time3' size='3' maxlength='5' disabled value = '<?php echo $row['Time3']; ?>' > ч.
								<= <input type='text' name='Time4' size='4' maxlength='5' value = '<?php echo $row['Time4']; ?>' > ч.<br>
						
						<b>или</b> ако t* Бойлер_Котел >= 
								<input type='text' name='temp3'    size='2' maxlength='5' value = '<?php echo $row['temp3']; ?>' > С* 
						и разликата между t* Бойлер_Котел и t* Бойлер_Солар > 
								<input type='text' name='temp4'    size='2' maxlength='5' value = '<?php echo $row['temp4']; ?>' > С*<br>
						и t* Котел >= t* Бойлер_Котел<br>
						 -------------------------------------------------------<br>
						<!-- elif S6_PumpStatus == 1.0 and (S3_BoilerTop <= 50.0 or Time > 1300):-->
						<b>Изключи автоматично</b> помпата ако t* Бойлер_Солар <= 
								<input type='text' name='temp5'    size='2' maxlength='5' disabled value = '<?php echo $row['temp5']; ?> '> С* 
						<b>или</b> часа е след: >
								<input type='text' name='Time5' size='4' maxlength='5' disabled value = '<?php echo $row['Time5']; ?>' > ч.<br>
						==================================================================<br>
						  
						<b>----  НАГРЕВАТЕЛИ НА КОТЕЛЕН И СОЛАРЕН БОЙЛЕР---- </b><br><br>
				<!-- Switching Boiler_ON_OFF--------------------------------------
					Data from table "correction"-------------------------------------- 
						if  Set_S5_BoilerStatus == 1 and (S3_BoilerTop < 50 and (S3_BoilerTop-S4_BoilerBottom >3.0) and (Time > 700 and Time <= 2300))
						and K1_KotelOutput >= K3_BoilerTop-->
						<b>Включи ръчно</b> бойлера ако t* Бойлер < 
								<input type='text' name='temp6' size='2' maxlength='5' value = '<?php echo $row['temp6']; ?>' > С* <br>
						<b>или</b> t* Бойлер_Връх - t* Бойлер–Дъно > 
								<input type='text' name='temp7'    size='1' maxlength='5' value = '<?php echo $row['temp7']; ?>' > С* 
						интервал: > <input type='text' name='Time6' size='3' maxlength='5' disabled value = '<?php echo $row['Time6']; ?>' > ч.
								<= <input type='text' name='Time7' size='4' maxlength='5'  disabled value = '<?php echo $row['Time7']; ?>' > ч. <br>
						------------------------------------------------------------------------------------------------<br>
				<!--Data from Pico IP-------------------------------------------------------- 
						elif S3_BoilerTop <= 39.0 and (Time < 700 or Time >= 2300) and S6_PumpStatus == 0.0:-->
						<b>Включи автом. </b>бойлера, ако t* Бойлер <= 
								<input type='text' name='temp8' size='2' maxlength='5' value = '<?php echo $row['temp8']; ?>' > С*
						интервал: < <input type='text' name='Time8' size='3' maxlength='5'disabled value = '<?php echo $row['Time8']; ?>' > ч.
								>= <input type='text' name='Time9' size='4' maxlength='5' disabled value = '<?php echo $row['Time9']; ?>' > ч.<br>
					<!--elif S5_BoilerStatus == 1.0 and (S3_BoilerTop > 40.0 or Time >= 700):-->
						<b>Изключи автоматично </b>бойлера, ако t* Бойлер >  
								<input type='text' name='temp9'    size='2' maxlength='5' disabled value = '<?php echo $row['temp9']; ?> '> С* 
						<b>или</b> часа е след : >=
								<input type='text' name='Time10' size='4' maxlength='5' disabled value = '<?php echo $row['Time10']; ?>' > ч.<br>
						==================================================================<br>
			   
						<input name="button" value="    Ok    " type="submit"> <br><br>
					</form>
				</div>
			</div>
			
			<div id="menu" style="height: 110px;">
				<div class="menuHorizontal">
					 <ul>
						<li><a href="index.html" title="Начало" target="_self">Начало</a></li>
						<li><a href="scheme.php" title="Схема" target="_self">Схема</a></li>
						<li><a href="graph_solar.php" title="Соларна с-ма" target="_self">Соларна с-ма</a></li>
						<li><a href="graph_kotel.php" title="Отоплителна с-ма" target="_self">Отоплителна с-ма</a></li>
						<li><a href="graph_water.php" title="Разход на вода" target="_self">Разход на вода</a></li>
						<li><a href="commands.php" title="Команди" target="_self">Команди</a></li>
						<li><a href="settings.php" title="Настройки" target="_self">Настройки</a></li>
						 <!-- <li><a href="weather.php" title="Времето" target="_self">Времето</a></li> -->
					</ul>
				</div>
				<div id = "footer"> <?php include 'version.php'; echo $version; ?> </div>
			</div>
			
		</div> <!--<div style="clear: both;"></div>-->
	</body>
</html>
