<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<link href="Style/Styles.css" rel="stylesheet" type="text/css"/>
		<title></title>
	</head>
	<body>
		<div id="container">  
			<div id="head"><?php include 'version.php'; echo $title ?></div> 
			<div id="body" style = "height: 630px;">
				<div class="bodyContent1">
				
				<form action="Connect_to_commands.php" method="POST">
					<h4>КОМАНДИ ЗА СОЛАРНА СИСТЕМА: </h4>
					<?php include_once 'config.inc.php';   
						$db=new Connect_MySql();
						$sql="SELECT * FROM `commands`ORDER BY id DESC LIMIT 1";
						$result=$db->execute($sql);
						$row=$db->fetch_row($result);?>
					<?php if($row['Set_S6_PumpStatus']==2){?>
					Помпа : <input type='radio' name='Set_S6_PumpStatus' size='1' maxlength='1' value="2"checked > AUTO  <?php }else { ?>   
					Помпа : <input type='radio' name='Set_S6_PumpStatus' size='1' maxlength='1' value="2" > AUTO <?php }?> 
					<?php if($row['Set_S6_PumpStatus']==1){?>    
							<input type='radio' name='Set_S6_PumpStatus' size='1' maxlength='1' value="1" checked > ON  <?php }else { ?>
							<input type='radio' name='Set_S6_PumpStatus' size='1' maxlength='1' value="1"> ON <?php }?>
					<?php if($row['Set_S6_PumpStatus']==0){?> 
							<input type='radio' name='Set_S6_PumpStatus' size='1' maxlength='1' value="0" checked > OFF<br><?php }else { ?>
							<input type='radio' name='Set_S6_PumpStatus' size='1' maxlength='1' value="0" > OFF<br> <?php }?>

					<?php if($row['Set_S5_BoilerStatus']==2){?>
					Бойлер: <input type='radio' name='Set_S5_BoilerStatus' size='1' maxlength='1' value="2"checked > AUTO  <?php }else { ?>   
					Бойлер: <input type='radio' name='Set_S5_BoilerStatus' size='1' maxlength='1' value="2" > AUTO <?php }?> 
					<?php if($row['Set_S5_BoilerStatus']==1){?>    
							<input type='radio' name='Set_S5_BoilerStatus' size='1' maxlength='1' value="1" checked > ON  <?php }else { ?>
							<input type='radio' name='Set_S5_BoilerStatus' size='1' maxlength='1' value="1"> ON <?php }?>
					<?php if($row['Set_S5_BoilerStatus']==0){?> 
							<input type='radio' name='Set_S5_BoilerStatus' size='1' maxlength='1' value="0" checked > OFF<br><?php }else { ?>
							<input type='radio' name='Set_S5_BoilerStatus' size='1' maxlength='1' value="0" > OFF<br> <?php }?>
				-------------------------------------------------------<br>
					<h4>КОМАНДИ ЗА КОТЕЛНО: </h4>
					<?php if($row['Set_K6_PumpStatus']==2){?>
					Помпа : <input type='radio' name='Set_K6_PumpStatus' size='1' maxlength='1' value="2"checked > AUTO  <?php }else { ?>   
					Помпа : <input type='radio' name='Set_K6_PumpStatus' size='1' maxlength='1' value="2" > AUTO <?php }?> 
					<?php if($row['Set_K6_PumpStatus']==1){?>    
							<input type='radio' name='Set_K6_PumpStatus' size='1' maxlength='1' value="1" checked > ON  <?php }else { ?>
							<input type='radio' name='Set_K6_PumpStatus' size='1' maxlength='1' value="1"> ON <?php }?>
					<?php if($row['Set_K6_PumpStatus']==0){?> 
							<input type='radio' name='Set_K6_PumpStatus' size='1' maxlength='1' value="0" checked > OFF<br><?php }else { ?>
							<input type='radio' name='Set_K6_PumpStatus' size='1' maxlength='1' value="0" > OFF<br> <?php }?>

					<?php if($row['Set_K5_BoilerStatus']==2){?>
					Бойлер: <input type='radio' name='Set_K5_BoilerStatus' size='1' maxlength='1' value="2"checked > AUTO  <?php }else { ?>   
					Бойлер: <input type='radio' name='Set_K5_BoilerStatus' size='1' maxlength='1' value="2" > AUTO <?php }?> 
					<?php if($row['Set_K5_BoilerStatus']==1){?>    
							<input type='radio' name='Set_K5_BoilerStatus' size='1' maxlength='1' value="1" checked > ON  <?php }else { ?>
							<input type='radio' name='Set_K5_BoilerStatus' size='1' maxlength='1' value="1"> ON <?php }?>
					<?php if($row['Set_K5_BoilerStatus']==0){?> 
							<input type='radio' name='Set_K5_BoilerStatus' size='1' maxlength='1' value="0" checked > OFF<br><?php }else { ?>
							<input type='radio' name='Set_K5_BoilerStatus' size='1' maxlength='1' value="0" > OFF<br> <?php }?>

							<input name="button" value="    Ok    " type="submit"> <br><br>
				=================================<br>   
				</form>
			
				
				<form action="Connect_to_set_valves.php" method="POST">
					<h4>КОМАНДИ ЗА НАПОИТЕЛНА СИСТЕМА</h4>
				   
					<?php include_once 'config.inc.php';   
					$db=new Connect_MySql();
					$sql="SELECT * FROM `set_valves`ORDER BY id DESC LIMIT 1";
					$result=$db->execute($sql);
					$row=$db->fetch_row($result);?>

					<?php if($row['Set_Valve1']==2){?>	
					КРЪГ 1: <input type='radio' name='Set_Valve1' size='1' maxlength='1' value="2" checked >AUTO <?php }else { ?> 
					КРЪГ 1: <input type='radio' name='Set_Valve1' size='1' maxlength='1' value="2"  >AUTO <?php }?> 
					<?php if($row['Set_Valve1']==1){?>     
							<input type='radio' name='Set_Valve1' size='1' maxlength='1' value="1" checked >ON <?php }else { ?>
							<input type='radio' name='Set_Valve1' size='1' maxlength='1' value="1"  >ON <?php }?> 
					<?php if($row['Set_Valve1']==0){?>          
							<input type='radio' name='Set_Valve1' size='1' maxlength='1' value="0" checked >OFF<br> <?php }else { ?> 
							<input type='radio' name='Set_Valve1' size='1' maxlength='1' value="0">OFF<br> <?php }?>

					<?php if($row['Set_Valve2']==2){?>	
					КРЪГ 2: <input type='radio' name='Set_Valve2' size='1' maxlength='1' value="2" checked >AUTO <?php }else { ?> 
					КРЪГ 2: <input type='radio' name='Set_Valve2' size='1' maxlength='1' value="2"  >AUTO <?php }?> 
					<?php if($row['Set_Valve2']==1){?>     
							<input type='radio' name='Set_Valve2' size='1' maxlength='1' value="1" checked >ON <?php }else { ?>
							<input type='radio' name='Set_Valve2' size='1' maxlength='1' value="1"  >ON <?php }?> 
					<?php if($row['Set_Valve2']==0){?>          
							<input type='radio' name='Set_Valve2' size='1' maxlength='1' value="0" checked >OFF<br> <?php }else { ?> 
							<input type='radio' name='Set_Valve2' size='1' maxlength='1' value="0">OFF<br> <?php }?>

					<?php if($row['Set_Valve3']==2){?>	
					КРЪГ 3: <input type='radio' name='Set_Valve3' size='1' maxlength='1' value="2" checked >AUTO <?php }else { ?> 
					КРЪГ 3: <input type='radio' name='Set_Valve3' size='1' maxlength='1' value="2"  >AUTO <?php }?> 
					<?php if($row['Set_Valve3']==1){?>     
							<input type='radio' name='Set_Valve3' size='1' maxlength='1' value="1" checked >ON <?php }else { ?>
							<input type='radio' name='Set_Valve3' size='1' maxlength='1' value="1"  >ON <?php }?> 
					<?php if($row['Set_Valve3']==0){?>          
							<input type='radio' name='Set_Valve3' size='1' maxlength='1' value="0" checked >OFF<br> <?php }else { ?> 
							<input type='radio' name='Set_Valve3' size='1' maxlength='1' value="0">OFF<br> <?php }?>

					<?php if($row['Set_Valve4']==2){?>	
					КРЪГ 4: <input type='radio' name='Set_Valve4' size='1' maxlength='1' value="2" checked >AUTO <?php }else { ?> 
					КРЪГ 4: <input type='radio' name='Set_Valve4' size='1' maxlength='1' value="2"  >AUTO <?php }?> 
					<?php if($row['Set_Valve4']==1){?>     
							<input type='radio' name='Set_Valve4' size='1' maxlength='1' value="1" checked >ON <?php }else { ?>
							<input type='radio' name='Set_Valve4' size='1' maxlength='1' value="1"  >ON <?php }?> 
					<?php if($row['Set_Valve4']==0){?>          
							<input type='radio' name='Set_Valve4' size='1' maxlength='1' value="0" checked >OFF<br> <?php }else { ?> 
							<input type='radio' name='Set_Valve4' size='1' maxlength='1' value="0">OFF<br> <?php }?>
							================================<br><br><br>
							<b>Въведи час за начало на поливане</b><br>(слято напр. 2005 е двадесет часа и пет минути)
							<input type='text' name='starttime_v1' size='4' maxlength='5' value = '<?php echo $row['starttime_v1']; ?>'> <br>
							
							<br><b>Въведи продължителност на поливането за всеки един кръг в минути</b>
							<input type='text' name='histeresis' size='2' maxlength='5' value = '<?php echo $row['histeresis']; ?>'> <br> <br>                       
							<input name="button" value="    Ok    " type="submit"> <br><br>
					</form>
				</div>
				<div class="bodyContent2">
					<form action="query.php" method="post">
						<h3>ПРОВЕРКА НА ЗАПИСИТЕ</h3>
						=================================<br><br><br>  
						<h4>Изберете желаната информация в клетките и натиснете "Start" бутонa</h4>
						<h4>"Обхват" - Броят на записаните данни в базата</h4>
						<h4>"Колона" - Името на колоната с данни за температури; <br> 
						Ако е избрано "*" се показват всички колони, както следват:</h4>
						<h4>Пореден номер и дата: <br>"id", "Datetime" <br><br>
						Данни за соларната система: <br>"S1_BoilerInput", "S2_BoilerOutput", "S3_BoilerTop", "S4_BoilerBottom", "S5_BoilerStatus", "S6_PumpStatus", "S0_PumpStatus" <br><br>
						Данни за отоплителна система: <br>"K1_KotelOutput, К2_BoilerInput", "К3_BoilerTop", "К4_BoilerBottom", "К5_BoilerStatus", "К6_PumpStatus" <br><br>
						<h4> <br>   
						Обхват : <input type='text' name='range' size='3' maxlength='250' value="100"> реда<br>
						Колона: <input type='text' name='coll' size='3' maxlength='25' value="*"><br><br>
						<input name="button" value="Start" type="submit"> <br><br>
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
				<div id="footer"><?php include 'version.php'; echo $version?></div>
			</div>
			
		</div> <!--<div style="clear: both;"></div>-->
	</body>
</html>
