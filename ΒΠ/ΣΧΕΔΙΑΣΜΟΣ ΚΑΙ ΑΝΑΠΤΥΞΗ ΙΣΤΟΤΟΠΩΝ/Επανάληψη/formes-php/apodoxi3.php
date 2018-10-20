<html>
 <head>
  <title> ΒΠ</title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="lightgreen" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
 
<?php
   $omada1=$_GET['omada1'];
   $omada2=$_GET['omada2'];
   $foreskal=$_GET['foreskal'];
   $foresxeir=$_GET['foresxeir'];
   for ($k = 1; $k <= $foreskal; $k++)
	 {
	 echo $k, ' ', $omada1;
	 echo "<br>";
	 }
   echo '<br><br>';
   for ($k = 1; $k <= $foresxeir; $k++)
	 {
	 print "$k $omada2 <br>";
	 }
   echo '<br><br>';
?>

 </body>
</html>
