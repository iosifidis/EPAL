<html>
 <head>
  <title> BP </title>
    <meta charset="utf-8">
 </head>
 <body bgcolor="lightgreen" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
 
<?php
  $gynaika=$_GET['fem'];
  $andras=$_GET['man'];
  $diafora=$andras-$gynaika;
  if ($andras-$gynaika>10)  
   {
	  print "Το ζευγαρι θεωρειται αταιριαστο διοτι η διαφορα ηλικιας τους ειναι $andras - $gynaika = $diafora, μεγαλυτερο των 10 ετων";
   }
  else
   {
	  print "Το ζευγαρι θεωρειται ταιριαστο διοτι η διαφορα ηλικιας τους ειναι $andras-$gynaika = $diafora, μικρότερο των 10 ετων";
   }

?>

 </body>
</html>
