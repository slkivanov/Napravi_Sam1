<?php include_once 'config.inc.php'; ?>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251" /> 
	
	<form action="graph.php" > 
		<button type="submit" formaction="commands.php">Back</button><br><br>
	</form> 
<?php
//Connecting to DB------------------------------------------
	$db=new Connect_MySql();
		$sql='SELECT * FROM commands';
		$result=$db->execute($sql);
//INSERTING DATA INTO DB----------------------------------------
	$Datetime= date("Y-m-d H:i:s");
	$Set_S6_PumpStatus=$_POST['Set_S6_PumpStatus']; 
	$Set_S5_BoilerStatus=$_POST['Set_S5_BoilerStatus']; 
	$Set_K6_PumpStatus=$_POST['Set_K6_PumpStatus']; 
	$Set_K5_BoilerStatus=$_POST['Set_K5_BoilerStatus']; 
	   
	$num = $db->get_num_rows();
	echo "$num Records <br>";
	
	$sql="INSERT INTO commands (Set_S6_PumpStatus,Set_S5_BoilerStatus,Set_K6_PumpStatus,Set_K5_BoilerStatus,Datetime) 
	VALUES ('$Set_S6_PumpStatus','$Set_S5_BoilerStatus','$Set_K6_PumpStatus','$Set_K5_BoilerStatus','$Datetime')";
	$save = $db->execute($sql); 
    if($save){ 
        echo "<b>Data was written to table \"commands\"</b><br>"; 
    }
    else{
        echo "<b>Data wasn't written to table \"commands\"</b><br>"; 
    }

    $num=$num+1; 
    $sql='SELECT * FROM `commands` ORDER BY id DESC LIMIT 1';
    $result=$db->execute($sql); 
//PRINTING DATA --------------------------------------------- 
	while ($row=$db->fetch_row($result)){
		$num=$num-1;
		echo "Id".$row['Id'].";<br> DateTime: " .$row['Datetime']. ";<br> Set_S6_PumpStatus: " .$row['Set_S6_PumpStatus']. ";<br> Set_S5_BoilerStatus: " . $row['Set_S5_BoilerStatus']. ";<br> Set_K6_PumpStatus: " . $row['Set_K6_PumpStatus']. ";<br> Set_K5_BoilerStatus: " . $row['Set_K5_BoilerStatus']."<br>";
		} 


