<?php include_once 'config.inc.php'; ?>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251" /> 

	<form action="settings.php" > 
		<button type="submit" formaction="settings.php">Back</button><br><br>
	</form>
<?php
	//Connecting to DB------------------------------------------
		$db=new Connect_MySql();
			$sql='SELECT * FROM settings'; 
			$result=$db->execute($sql);
	//INSERTING DATA INTO DB----------------------------------------
		$Datetime= date("Y-m-d H:i:s");   
		$temp1=$_POST['temp1']; 
	//Checking for summer  or winter time---------------------------------------
		$Date= date("md");
		echo "Date: ", "$Date <br>";
    if ($Date > 325 and $Date < 1029){
		$StartTime = 700;
		$EndTime = 2300;
		echo "StartTime: ", $StartTime, "<br>", "End Time: ", $EndTime, "<br>";
	}
    else{
		$StartTime = 600;
		$EndTime = 2200;
		echo "StartTime: ", $StartTime, "<br>", "End Time: ", $EndTime, "<br>";
    }
    $temp2=$_POST['temp2']; 
    $Time3=$StartTime; 
    $Time4=$_POST['Time4']; 
	
	$temp3=$_POST['temp3'];
	$temp4=$_POST['temp4']; 
	$temp5=$_POST['temp2']; //temp5=temp2
	$Time5=$_POST['Time4']; //Time5=Time4
		
	$temp6=$_POST['temp6'];
	$temp7=$_POST['temp7'];  
    $Time6=$StartTime; 
    $Time7=$EndTime;
    
    $temp8=$_POST['temp8'];
	$Time8=$StartTime;
    $Time9=$EndTime;
    
    $temp9=$_POST['temp8']+2; //temp9=temp8
	$Time10=$StartTime;
	
		
    $num = $db->get_num_rows();
    echo "Records: ", $num,  "<br><br>";
    
    $sql="INSERT INTO settings (temp1,StartTime,EndTime,temp2,Time3,Time4,temp3,temp4,temp5,Time5,temp6,temp7,Time6,Time7,temp8,Time8,Time9,temp9,Time10,Datetime) 
    VALUES ('$temp1','$StartTime','$EndTime','$temp2','$Time3','$Time4','$temp3','$temp4','$temp5','$Time5','$temp6','$temp7','$Time6','$Time7','$temp8','$Time8','$Time9','$temp9','$Time10','$Datetime')";
    $save = $db->execute($sql); 
    if($save){ 
        echo "<b>Data was written to table \"settings\"</b><br>"; 
    }
    else{
        echo "<b>Data wasn't written to table \"settings\"</b><br>"; 
    }

    $num=$num+1; 
    $sql='SELECT * FROM `settings` ORDER BY id DESC LIMIT 1';
    $result=$db->execute($sql); 
//PRINTING DATA --------------------------------------------- 
	while ($row=$db->fetch_row($result)){
		$num=$num-1;
		echo "temp1: " .$row['temp1']."; StartTime: " .$row['StartTime']. "; EndTime: " .$row['EndTime']."<br>";
		echo "temp2: " .$row['temp2']."; Time3: " .$row['Time3']. "; Time4: " .$row['Time4']."<br>";
		echo "temp3: " .$row['temp3']."; temp4: " .$row['temp4']. "; temp5: " .$row['temp5']. "; Time5: " .$row['Time5'] ."<br>";
		echo "temp6: " .$row['temp6']."; temp7: " .$row['temp7']. "; Time6: " .$row['Time6']. "; Time7: " .$row['Time7'] ."; temp8: " .$row['temp8'] . "<br>";
		echo "Time8: " .$row['Time8']."; Time9: " .$row['Time9']. "; temp9: " .$row['temp9']. "; Time10: " .$row['Time10'] ."<br>";
		}

