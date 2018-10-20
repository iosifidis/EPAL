<html>
 <head>
  <title> ΒΠ</title>
   <meta charset="utf-8">
 </head>
 <body bgcolor="lightgreen" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
 
 <table width="80%" align="center" border="1">
<?php
   $grammes=$_GET['grammes'];
   for ($k = 1; $k <= $grammes; $k++)
	 {
     print "<tr> <td> γραμμη νο $k </td>";
	 print "<td> ... </td>";
	 print "<td> ... </td>";
	 }
?>
 </table>
 </body>
</html>
