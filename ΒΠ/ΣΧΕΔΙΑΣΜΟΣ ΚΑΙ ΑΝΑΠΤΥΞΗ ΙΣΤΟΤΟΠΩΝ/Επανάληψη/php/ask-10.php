<!DOCTYPE html>
<html>
 <head>
  <title> php 10 </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="beige" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
<?php
echo "ΔΙΑΚΛΑΔΩΣΗ - Εντολή IF...ELSE...";
echo "<br><br>";

$maria=39;
$tasos=42;
$diafora= $tasos - $maria;

if (($diafora >= 0) and ($diafora < 6) and ($maria > 18) and ($tasos < 80))
 {
 print "Η Μαρία  και ο Τάσος είναι ταιριαστό ζευγάρι";
 }
else
 {
 print "Η Μαρία  και ο Τάσος δεν είναι ταιριαστό ζευγάρι";
 }
 
print "<br><br><hr>εδω τελειωνει το παραδειγμα"; 
?>

  </font>
 </body>
</html> 