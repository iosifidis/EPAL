<html>

 <head>
  <title> BP </title>
  <meta charset="utf-8">
<?php
date_default_timezone_set("Europe/Athens");
// echo date_default_timezone_get();
// echo "The time is " . date("h:i:sa");
?>
 </head>
 
 <body bgcolor="lightgreen" text="black">
  <font size="5">
  <br>
  <center><u>Υπολογισμός Μισθοδοσίας</u></CENTER>
  <br>

<?php
// ελεγχος δεδομένων
$lathos=0;

$fylo=$_POST['fylo'];
$eggamos=$_POST['eggamos'];
$asfal=$_POST['asfal'];

if (!IsSet($_POST['onoma']) or empty($_POST['onoma']))
  {	$lathos=1;
	print "Δεν έχει δοθει όνομα μισθοδοτουμένου !! <br><br>";  }
else
  {	$name=$_POST['onoma'];  }

if (!IsSet($_POST['afm']) or empty($_POST['afm']))
  {	$lathos=1;
	print "Δεν έχει δοθει ΑΦΜ μισθοδοτουμένου !! <br><br>";  }
else
  {	$afm=$_POST['afm'];  }

if (!IsSet($_POST['dief']))
  {	$dief="";  }
else
  {	$dief=$_POST['dief'];  }

if (!IsSet($_POST['kodikos']) or empty($_POST['kodikos']))
  {	$lathos=1;
	print "Δεν έχει δοθει Αριθμός Μητρώου μισθοδοτουμένου !! <br><br>";  }
else
  { $kodikos=$_POST['kodikos'];  }

if (!IsSet($_POST['bas']) or empty($_POST['bas']))
  {	$lathos=1;
	print "Δεν έχει δοθεί βασικό ημερομίσθιο μισθοδοτουμένου !! <br><br>";  } 
else
  { $bas=$_POST['bas']; 
  if ($bas<=0 or $bas>=100)
	{ print "Λάθος δεδομενα ημερομισθιου ( $bas ) ?? <br><br>";  }
  }

if (!IsSet($_POST['meres']))
  {	$tekna=0;}
else
  { $tekna=$_POST['tekna'];
  if ($tekna<0)
    { $lathos=1;
      print "Λάθος δεδομενα αριθμου τέκνων ( $tekna ) ?? <br><br>"; }
  }

if (!IsSet($_POST['meres']) or empty($_POST['meres']))
  {	$lathos=1;
	print "Δεν έχει δοθει αριθμός ημερομισθίων μισθοδοτουμένου !! <br><br>";  }
else
  { $meres=$_POST['meres'];
  if ($meres<0 or $bas>=27)
    { $lathos=1;
      print "Λάθος δεδομενα αριθμου ημερομισθιων ( $meres ) ?? <br><br>"; } 
  }

if (!IsSet($_POST['gamou']))
  {	$gamou=0;  }
else
  {	$gamou=0.1;  }

if (IsSet($_POST['gamou']) and ($eggamos !== "Ε"))
  {	$lathos=1;
    print "Λάθος δεδομενα - Επίδομα Γάμου ΚΑΙ μη Εγγαμος ?? <br><br>";  }

if (!IsSet($_POST['ter']))
  {	$epter=0;  }
else
  {	$epter=200;  }

if (!IsSet($_POST['enoik']))
  {	$epenoik=0;  }
else
  {	$epenoik=150;  }

if (!IsSet($_POST['sxolia']))
  {	$sxolia="";  }
else
  {	$sxolia=$_POST['sxolia'];  }

if ($lathos==1)
  {  print "Συνέχιση αδυνατη - Πατηστε ΕΠΙΣΤΡΟΦΗ <br><br> ";  }
else
  {
  $prosfonisi1="";
  $prosfonisi2="";
  if ($fylo=="Γ")
	{	$prosfonisi2="κα";	}
  else
    {	$prosfonisi2="κε";	}
  if (time() >= strtotime("12:00:00"))
	{    $prosfonisi1="Καλησπέρα";	}
  else
    {    $prosfonisi1="Καλημέρα";	}
  print "<center>$prosfonisi1 $prosfonisi2 $name</center> <br>";
  print "ΑΦΜ : $afm <br>";
  print "Διεύθυνση : $dief <br>";
  print "Αρ.τέκνων : $tekna <br>";
  print "Οικογ.κατάσταση : ";
  switch ($eggamos) {
    case "Ε":
        echo "Εγγαμος <br>";
        break;
    case "Χ":
        echo "Χήρος/α <br>";
        break;
    case "Δ":
        echo "Διαζευγμένος/η <br>";
        break;
    default:
        echo "Αγαμος/η <br>";
	}
  print "Φύλο : ";
  if ($fylo=="Α")
	{print "Ανδρας <br>";}
  else
   {print "Γυναίκα <br>";}

  $basikos=$bas*$meres;
  print "<br>Βασικες αποδοχές = $basikos <br><br>";
  
  $epgamou=$basikos*$gamou;
  print "Επιδομα Γάμου (10%) : $epgamou <br>";
  
  print "Επιδομα Θερμανσης : $epter <br>";

  print "Επιδομα Ενοικιου : $epenoik <br>";

  $miktes=$basikos+$epgamou+$epter+$epenoik;
  print "<br>Μικτές αποδοχές = $miktes <br><br>";
  
  switch ($asfal) {
    case "ika":
	    $kratiseis=$miktes*0.23;
        echo "Κρατησεις ΙΚΑ (23%) = $kratiseis <br>";
        break;
    case "tsa":
	    $kratiseis=$miktes*0.15;
        echo "Κρατησεις ΤΣΑ (15%) = $kratiseis <br>";
        break;
    case "nat":
	    $kratiseis=$miktes*0.05;
        echo "Κρατησεις ΝΑΤ (5%) = $kratiseis <br>";
        break;
    case "tebe":
	    $kratiseis=$miktes*0.33;
        echo "Κρατησεις ΤΕΒΕ (33%) = $kratiseis <br>";
        break;
    case "oga":
	    $kratiseis=$miktes*0.04;
        echo "Κρατησεις ΟΓΑ (4%) = $kratiseis <br>";
        break;
    case "dim":
	    $kratiseis=$miktes*0.35;
        echo "Κρατησεις Δημοσιου (35%) = $kratiseis <br>";
        break;
    case "nom":
	    $kratiseis=$miktes*0.40;
        echo "Κρατησεις Ταμ.Νομικων (40%) = $kratiseis <br>";
        break;
	}

  $forapodoxes=$miktes-$kratiseis;
  print "<br>Φορολογησιμες αποδοχές = $forapodoxes <br>";
  
  $foros=$forapodoxes*0.1;
  print "<br>Παρακρατηση Φορου 10% = $foros <br>";
  
  $pliroteo=$forapodoxes-$foros;
  print "<br>ΠΛΗΡΩΤΕΟ = $pliroteo <br><br>";
  
  }
	  
?>
  
 </body>
</html>


