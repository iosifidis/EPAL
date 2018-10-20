<!DOCTYPE html>
<html>
 <head>
  <title> php 3 </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="beige" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
  <br><br>
 
<?php

echo "Mεταβλητες on the fly";
echo "<br><br>";

$txt="Γειά σου" . " κοσμε!";
$x= 3 + 5 * 2;
$y=10.5;
$sofia=$x * $y;

echo $txt;
echo "<br>";
echo $x;
echo "<br>";
echo $y;
echo "<br>";
echo $sofia;

// σκοπιμο λαθος παρακατω echo $Sofia;
?> 

<hr>

<?php
// παρακατω ειναι ορισμος προσωρινής ανωνυμης μεταβλητης την στιγμη της εμφανισης (στο φτερο)
echo $sofia * $x;
?> 

  </font>
 </body>
</html> 