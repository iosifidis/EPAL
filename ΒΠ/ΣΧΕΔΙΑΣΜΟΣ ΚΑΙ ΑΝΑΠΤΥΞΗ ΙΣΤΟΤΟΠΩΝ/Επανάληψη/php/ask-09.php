<!DOCTYPE html>
<html>
 <head>
  <title> php 9 </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="beige" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
<?php
echo "ΔΙΑΚΛΑΔΩΣΗ - Εντολή IF...ELSE...";
echo "<br><br>";
$maria=42;
$tasos=42;
?>

<br><hr><br>

<?php
if ($maria < $tasos)
 {
 print "Η Μαρία είναι μικρότερη από τον Τάσο";
 print " αρα είναι ταιριαστό ζευγάρι";
 }
else
 {
 if ($maria == $tasos)
  {
  print "Η Μαρία εχει ιδια ηλικία με τον Τάσο";
  print " αρα είναι ταιριαστό ζευγάρι";
  }
 else
  {
  print "Η Μαρία είναι μεγαλύτερη από τον Τάσο";
  print " αρα δεν είναι ταιριαστό ζευγάρι";
  }
 }
print "<br><br><hr>εδω τελειωνει το παραδειγμα"; 
?>

  </font>
 </body>
</html> 