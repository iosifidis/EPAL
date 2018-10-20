<html>
 <head>
  <title> ΒΠ</title>
 </head>
 <body bgcolor="lightgreen" text="black">

  <font size="5">
  <center><u>ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΦΑΡΜΟΓΗΣ PHP</u></CENTER>
 <br><br>
 
 
 <?php
   $onoma=$_GET['onoma'];
   $afm=$_GET['afm'];
   $dief=$_GET['dief'];
   $tekna=$_GET['tekna'];
   $kodikos=$_GET['kodikos'];
   $eggamos=$_GET['eggamos']; 
   $fylo=$_GET['fylo'];
   $gamou=$_GET['gamou'];
   $term=$_GET['term'];
   $enoik=$_GET['enoik'];
   $asfal=$_GET['asfal'];
   $bas=$_GET['bas'];
   $meres=$_GET['meres'];
   $sxolia=$_GET['sxolia'];
   if ($fylo=="Α")
   { print "καλημερα κε $onoma";   }
   else
   {print "καλημερα κα $onoma";}
   print
   print $dief;
   
  ?>

 </body>
</html>
