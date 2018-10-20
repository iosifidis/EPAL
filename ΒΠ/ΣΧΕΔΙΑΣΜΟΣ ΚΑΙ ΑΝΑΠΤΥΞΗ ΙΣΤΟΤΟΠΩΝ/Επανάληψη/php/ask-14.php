<!DOCTYPE html>
<html>
 <head>
  <title> php 14 </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="beige" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 

ΕΠΑΝΑΛΗΨΕΙΣ - Εντολή 2-FOR
<br><br>

<?php
print "<u>ολοι οι μοναδικοι συνδυασμοι αριθμών απο το 01 μεχρι και το 99 </u><br><br>";

  for ($i = 0; $i < 10; $i++)
   {
    for ($k = $i; $k < 10; $k++)
	 {
      echo $i . $k . '&nbsp';
	 }
	echo '<br><br>';
   }
echo '<br><br>';
?>

<?php
print "<u>η προπαίδεια (1-10)</u><br><br>";

  for ($i = 1; $i <= 10; $i++)
   {
    for ($k = 1; $k <= 10; $k++)
	 {
      echo $i * $k . '&nbsp';
	 }
	echo '<br><br>';
   }
?>

  </font>
 </body>
</html> 