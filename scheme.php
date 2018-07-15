<html>
   <!-- 08.07.2018_ Inserted leading zeros to water meter and format "$water" with 3 digits after decimal point -->
   
   <?php include_once 'config.inc.php'; ?>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
    <link rel="stylesheet" type="text/css" href="Style/Animation_solar.css" media="screen" />
    
<body>
        <div id="container">
            
            <?php
            header("refresh: 30;");
                $db=new Connect_MySql();
				$sql='SELECT * FROM `temp`ORDER BY id DESC LIMIT 1';
				$result=$db->execute($sql);
				$row=$db->fetch_row($result);
			    mysqli_free_result($result);
            ?>
			<div id="body">
				<div id="head"><?php include 'version.php'; echo $title?></div>	
				<div  class="positioning">
					<div style="position: absolute; color:#ff0000;top: 20px; left:218px;";>
						<?php echo $row['Datetime']; ?>
					</div>
					<div style="position: absolute; color:#ff0000; top: 230px; left: 360px;";>
						<?php echo $row['S1_BoilerInput'] . "C˚"; ?>
					</div>
					<div style="position: absolute; top: 290px; left: 360px;";>
						<?php echo $row['S2_BoilerOutput']."C˚"; ?>
					</div>
					<div style="position: absolute; color:#ff0000; top: 150px; left: 455px;";>
						<?php echo $row['S3_BoilerTop']. "C˚"; ?>
					</div>
					<div style="position: absolute; top: 310px; left: 455px;";>
						<?php echo $row['S4_BoilerBottom']. "C˚"; ?>
					</div>
					
					
					
					<div style="position: absolute; color:#ff0000; top: 145px; left: 1125px;";>
						<?php echo $row['K1_KotelOutput']. "C˚"; ?>
					</div>
					<div style="position: absolute; color:#ff0000; top: 230px; left: 1045px;";>
						<?php echo $row['K2_BoilerInput'] . "C˚"; ?>
					</div>
					<div style="position: absolute; color:#ff0000; top: 150px; left: 930px;";>
						<?php echo $row['K3_BoilerTop']. "C˚"; ?>
					</div>
					 <div style="position: absolute; top: 310px; left: 932px;";>
						<?php echo $row['K4_BoilerBottom']. "C˚"; ?>
					</div>
			<!-- Animation for Solar Pump ===========================-->
					<div style="position: absolute; color:#ff0000; top: 0px; left: 0px;";>
						<?php
							$S0_PumpStatus = $row['S0_PumpStatus'];
							#$S0_PumpStatus = 0;
							
							if ($S0_PumpStatus > 0) {
								echo "<div style=\"position: absolute; top: 325px; left: 293px;"
								. "color:#ff0000;  z-index: 1;\">ON</div>";
								echo "<div1 style=\"position: absolute; z-index: 1;\"></div1>";
								echo "<div2 style=\"position: absolute; z-index: 1;\"></div2>";
								echo "<div3 style=\"position: absolute; z-index: 1;\"></div3>";
								echo "<div4 style=\"position: absolute; z-index: 1;\"></div4>";
								echo "<div_rotator style=\"position: absolute; top: 277px; left: 280px; z-index: 1;\"></div_rotator>";
							} else {
								echo "<div style=\"position: absolute; top: 325px; left: 293px;"
								. "color: blue; z-index: 1;\">OFF</div>";  
							}
						?>
					</div>
			<!-- Kotel Heater =======================================-->
					<div style="position: absolute;";>
						<?php
							$K5_BoilerStatus = $row['K5_BoilerStatus'];
							#$K5_BoilerStatus = 1;
							#$K5_BoilerStatus = 1;
							if ($K5_BoilerStatus > 0) {
								echo "<div style=\"position: absolute; top: 340px; left: 935px;"
								. "color:#ff0000;  z-index: 1;\">ON</div>";
							} else {
								echo "<div style=\"position: absolute; top: 340px;"
								. " left: 935px; color: blue; z-index: 1;\">OFF</div>"; 
							}
						?>
					</div>
			
			<!-- Animation for Kotel Pump ===========================-->
					<div style="position: absolute;";>
						<?php
							$K6_PumpStatus = $row['K6_PumpStatus'];
							#$K6_PumpStatus = 1;
							#$K6_PumpStatus = 1;
							if ($K6_PumpStatus > 0) {
								echo "<div style=\"position: absolute; top: 330px; left: 1095px;"
								. "color:#ff0000;  z-index: 1;\">ON</div>";
								echo "<div5 style=\"position: absolute; z-index: 1;\"></div5>";
								echo "<div6 style=\"position: absolute; z-index: 1;\"></div6>";
								echo "<div7 style=\"position: absolute; z-index: 1;\"></div7>";
								echo "<div8 style=\"position: absolute; z-index: 1;\"></div8>";
								echo "<div_rotator style=\"position: absolute; top: 281px; left: 1081px; z-index: 1;\"></div_rotator>";
							} else {
								echo "<div style=\"position: absolute; top: 330px; left: 1095px;"
								. "color: blue; z-index: 1;\">OFF</div>";  
							}
						?>
					</div>
			<!-- Solar Heater =======================================-->
					<div style="position: absolute;";>
						<?php
							$S5_BoilerStatus = $row['S5_BoilerStatus'];
							#$S5_BoilerStatus = 1;
							#$S5_BoilerStatus = 1;
							if ($S5_BoilerStatus > 0) {
								echo "<div style=\"position: absolute; top: 340px; left: 460px;"
								. "color:#ff0000;  z-index: 1;\">ON</div>";
							} else {
								echo "<div style=\"position: absolute; top: 340px;"
								. " left: 460px; color: blue; z-index: 1;\">OFF</div>"; 
							}
						?>
					</div>
			<!-- Animation for Circulation Pump =======================-->
					<div style="position: absolute;";>
						<?php
							$S6_PumpStatus = $row['S6_PumpStatus'];
							#$S6_PumpStatus = 1; 
							#$S6_PumpStatus = 1;            
							if ($S6_PumpStatus > 0) {
								echo "<div style=\"position: absolute; top: 485px; left: 565px;"
								. "color:#ff0000;  z-index: 1;\">ON</div>";
								echo "<div9 style=\"position: absolute; z-index: 1;\"></div9>";
								echo "<div10 style=\"position: absolute; z-index: 1;\"></div10>";
								echo "<div11 style=\"position: absolute; z-index: 1;\"></div11>";
								echo "<div12 style=\"position: absolute; z-index: 1;\"></div12>";
								echo "<div13 style=\"position: absolute; z-index: 1;\"></div13>";
								echo "<div14 style=\"position: absolute; z-index: 1;\"></div14>";
								echo "<div_rotator style=\"position: absolute; top: 436px; left: 550px; z-index: 1;\"></div_rotator>";
							} else {
								echo "<div style=\"position: absolute; top: 485px; left: 560px;"
								. "color: blue; z-index: 1;\">OFF</div>";  
							}
							
							$sql='SELECT * FROM `water`ORDER BY id DESC LIMIT 1';
							$result=$db->execute($sql);
							$row=$db->fetch_row($result);
							mysqli_free_result($result);
							
							$water = $row['water_data'];
							$water = number_format($water,3,",","");
							$water = str_pad($water , 10, '0', STR_PAD_LEFT);
							echo "<div style=\"position: absolute; top: 535px; left: 225px;"
								. "color:#ff0000;  z-index: 1;\">$water/m3 </div>";
							
						?>
					</div>
				</div>
			</div>	
				<div id="menu">
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
				
		</div>
	</body>
	<!--<div style="clear:both;"> </div>-->
</html>
