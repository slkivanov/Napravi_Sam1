<?php include_once 'config.inc.php'; ?>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251" />
 
	<form action="commands.php" > 
		<button type="submit" formaction="commands.php">Back</button><br><br>
	</form> 
<?php
//connecting to DB------------------------------------------
    $db=new Connect_MySql();
        $sql="select*from set_valves";
        $que=$db->execute($sql);

//INSERT DATA INTO DB----------------------------------------
    $Datetime= date("Y-m-d H:i:s");
    $Set_Valve1=$_POST['Set_Valve1']; 
    $Set_Valve2=$_POST['Set_Valve2']; 
    $Set_Valve3=$_POST['Set_Valve3']; 
    $Set_Valve4=$_POST['Set_Valve4']; 
	$starttime_v1=$_POST['starttime_v1']; 
	$histeresis=$_POST['histeresis']; 
	
	$num = $db->get_num_rows();
    echo "$num Records <br>";
    
    $sql="INSERT INTO set_valves (Set_Valve1,Set_Valve2,Set_Valve3,Set_Valve4,Datetime,starttime_v1,histeresis) VALUES ('$Set_Valve1','$Set_Valve2','$Set_Valve3','$Set_Valve4','$Datetime','$starttime_v1','$histeresis')";
    $save = $db->execute($sql); 
    if($save){ 
        echo "<b>Data was written to table \"set_valves\"</b><br>"; 
    }
    else{
        echo "<b>Data wasn't written to table \"set_valves\"</b><br>"; 
    }
	$num=$num+1; 
    $sql="SELECT * FROM `set_valves` ORDER BY id DESC LIMIT 1";
    $que=$db->execute($sql); 
//PRINTING DATA --------------------------------------------- 
   while ($row=$db->fetch_row($que)){
    $num=$num-1;
    echo "Id".$row['Id']."<br> Datetime: " .$row['Datetime']. ";<br> Set_Valve1: " .$row['Set_Valve1']. ";<br> Set_Valve2: " . $row['Set_Valve2']. ";<br>  Set_Valve3: " . $row['Set_Valve3']. ";<br>  Set_Valve4: " . $row['Set_Valve4'].";<br>  starttime_v1: " . $row['starttime_v1'].";<br>  histeresis: " . $row['histeresis']."<br>"; 
    } 
