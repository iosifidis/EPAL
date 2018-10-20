<!DOCTYPE html>
<html>
 <head>
  <title> php 13 </title>
  <meta charset="utf-8">
 </head>
 <body bgcolor="beige" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
ΕΠΑΝΑΛΗΨΕΙΣ - Εντολή FOR
<br><br>

<table border="1">
 <tr>
<?php
$arxh=1;
$telos=20;
for ($metritis = $arxh; $metritis <= $telos; $metritis++)
  {
  print"<td> $metritis </td>";
  }
?>
 </tr>
</table>

<br><br>εδω τελειωνει το 1o παραδειγμα<hr><br><br>


<table border="1">
<?php
$arxh=1;
$telos=150;
print "<tr>";
 for ($metritis = $arxh; $metritis <= $telos; $metritis++)
  {
	if ($metritis%4==0)
	 {
	   print"<td bgcolor=\"lightgreen\"> $metritis </td>";
	 }
	else
	 {
       print"<td> $metritis </td>";
	 }
    if ($metritis%10==0) 
     {
       print"</tr><tr>";
     }
  }
print"</tr>";
?>
</table>

<br><br>εδω τελειωνει το 2o παραδειγμα<hr><br><br>

  </font>
 </body>
</html> 