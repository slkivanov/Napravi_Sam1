<!DOCTYPE HTML>
<?php include_once 'config.inc.php'; ?>

<html>
    <head>
<!--   <META HTTP-EQUIV="refresh" CONTENT="15"> -->
    </head>
    <body>
        <div style="background-color: #ccc;";>
    <form> 
        <button type="submit" formaction="commands.php">Back</button><br><br>
    </form> 
		  <?php
            /*-- header("refresh: 30;");*/
                $db=new Connect_MySql();
				$sql='SELECT * FROM temp ';
				$result=$db->execute($sql);
				$num_rows=$db->get_num_rows($result);
				$range=$_POST['range']; 
       
       /* fetch last row in reverse order-------------------------------------- */
			for ($i = $num_rows-1; $i >= $num_rows-1; $i--) {
				if (!mysqli_data_seek($result, $i)) {
					echo "Cannot seek to row $i: " . mysqli_error() . "\n";
					continue;
				}

				if (!($row=$db->fetch_assoc($result))) {
					continue;
				}


				

				$date = substr($row['Datetime'], 0, 10);
				$time = substr($row['Datetime'], 11, 9);

				echo "<table border=5px border-color= blue style= width:50% cellpadding=10>";
				echo "<tr>
						<th> date </th> <th> time </th><th> S1 </th><th> S2 </th> <th> S3 </th> <th> S4 </th> <th> Heat  </th> <th> Pump </th>
						<th> K1 </th> <th> K2 </th> <th> K3 </th> <th> K4 </th> <th> Heat  </th> <th> Pump  </th>";
				echo "<tr>
						<td> $date </td>  <td> $time </td> <td> $row[S1_BoilerInput] </td><td> $row[S2_BoilerOutput] </td>
						<td> $row[S3_BoilerTop] </td><td> $row[S4_BoilerBottom] </td><td> $row[S5_BoilerStatus] </td><td> $row[S6_PumpStatus] </td>
						
						<td> $row[K1_KotelOutput] </td><td> $row[K2_BoilerInput] </td> <td> $row[K3_BoilerTop] </td> 
						<td> $row[K4_BoilerBottom] </td><td> $row[K5_BoilerStatus] </td><td> $row[K6_PumpStatus] </td>
					</tr>";
				echo "</table><br />\n";
			} 

		/* fetch all rows in reverse order----------------------------------------------- */ 
			#echo " ____________________________________________________________________________________ <br/>";  
			#echo " |___date___|__time__|__S1__|_S2__|__S3_|_S4_|Heat|Pump | | |___K1_|__K2_|__K3_|_K4_|Heat|Pump| <br/>";
			for ($i = $num_rows - 1; $i >= $num_rows-$range; $i--) {
				if (!mysqli_data_seek($result, $i)) {
					echo "Cannot seek to row $i: " . mysqli_error() . "\n";
					continue;
				}

				if (!($row = mysqli_fetch_assoc($result))) {
					continue;
				}

				echo "". $row['Datetime']." - ". $row['S1_BoilerInput']." - " . $row['S2_BoilerOutput'].
					" - " . $row['S3_BoilerTop']. " - " . $row['S4_BoilerBottom']." - " . $row['S5_BoilerStatus'].
					" - " . $row['S6_PumpStatus']." - "." ||"." - ". $row['K1_KotelOutput']. 
					" - " . $row['K2_BoilerInput']." - " . $row['K3_BoilerTop'].
					" - " . $row['K4_BoilerBottom']." - " . $row['K5_BoilerStatus'].
					" - " . $row['K6_PumpStatus']."<br />\n";
			}

			mysqli_free_result($result);
		?>
    </body>
</html> 
