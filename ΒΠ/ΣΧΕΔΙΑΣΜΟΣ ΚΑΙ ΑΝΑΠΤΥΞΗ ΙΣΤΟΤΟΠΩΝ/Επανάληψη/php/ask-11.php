<!DOCTYPE html>
<html>
 <head>
  <title> php 11 </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="beige" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
<?php
echo "ΔΙΑΚΛΑΔΩΣΗ - Εντολή SWITCH";
echo "<br><br>";

$tyxeros_arithmos = 552;
$ar = 51;
$arr = 52;

switch($tyxeros_arithmos)
 {
 case ($ar):
  print "ο τυχερος σου αριθμος<br>";
  print "ειναι το $ar";
  break;
 case ($arr):
  print "ο τυχερος σου αριθμος<br>";
  print "ειναι το $arr";
  break;
 case 3:
  print "ο τυχερος σου αριθμος<br>";
  print "ειναι το 3";
  break;
 default:
  print "ο τυχερος σου αριθμος<br>";
  print "ειναι μάλλον ο $tyxeros_arithmos";
  break;
  }
?>

  <br><br><hr>εδω τελειωνει το παραδειγμα

  </font>
 </body>
</html> 