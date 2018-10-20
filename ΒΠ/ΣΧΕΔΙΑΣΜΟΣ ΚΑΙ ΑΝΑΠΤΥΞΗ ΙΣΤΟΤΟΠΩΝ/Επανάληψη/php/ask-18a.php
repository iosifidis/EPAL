<html>
 <head>
  <title> php 18a </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="lightgreen" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
 <u>Αποτελέσματα πραξεων (χωρις ελεγχο διαιρεσης με 0):</u> <br><br>
 
<?php

 $athroisma = $_GET['ar1'] + $_GET['ar2'];
 print "$_GET[ar1] συν $_GET[ar2] = $athroisma";
 echo "<br><br>";

 $diafora = $_GET['ar1'] - $_GET['ar2'];
 print "$_GET[ar1] μειον $_GET[ar2] = $diafora";
 echo "<br><br>";

 $ginomeno = $_GET['ar1'] * $_GET['ar2'];
 print "$_GET[ar1] επι $_GET[ar2] = $ginomeno";
 echo "<br><br>";

 $piliko = $_GET['ar1'] / $_GET['ar2'];
 print "$_GET[ar1] δια $_GET[ar2] = $piliko";
 echo "<br><br>";

 $ypoloipod = $_GET['ar1'] % $_GET['ar2'];
 print "$_GET[ar1]  ακεραιο υπολοιπο διαιρεσης δια $_GET[ar2] = $ypoloipod";
 echo "<br><br>";

 $r1=$_GET['ar1'];
 $r2=$_GET['ar2'];
 $dynamis = exp($r2*log($r1));
 print "$_GET[ar1] εις την $_GET[ar2] = $dynamis";
 echo "<br><br>";
 /* απο την εκδοση 5.6 και μετα χρησιμοποιω το ** */
  
?>
  </font>
 </body>
</html>
