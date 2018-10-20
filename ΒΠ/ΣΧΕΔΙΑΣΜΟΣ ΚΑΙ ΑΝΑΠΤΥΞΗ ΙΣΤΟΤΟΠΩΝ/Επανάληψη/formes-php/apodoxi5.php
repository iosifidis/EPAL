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
   $stiles=$_GET['stiles'];
   for ($k = 1; $k <= $grammes; $k++)
	 {
		 print "<tr>";
		 for ($m = 1; $m <= $stiles; $m++)
		 {
        	 print "<td> ... </td>";
		 }
		 print "</tr>";
	 }
?>
 </table>
 </body>
</html>
