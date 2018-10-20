<html>

 <head> 
  <title> selfcall </title>
  <meta charset="utf-8">
<?php
if  (IsSet($_POST['Ar1']) || IsSet($_POST['Ar2']))
// αρχικοποιηση μεταβλητων
  {
  $Athrisma = $_POST['Ar1'] + $_POST['Ar2'];
  $Diafora = $_POST['Ar1'] - $_POST['Ar2'];
  $Ginomeno = $_POST['Ar1'] * $_POST['Ar2'];
  if ($_POST['Ar2'] != 0)
    {
	$Piliko = $_POST['Ar1'] / $_POST['Ar2'];
    }
  else
    {
    $Piliko = "";
	}
  }
else
  {
  $_POST['Ar1'] = "";
//  $_POST['Ar2'] = "";
  $Athrisma = "";
  $Diafora = "";
  $Ginomeno = "";
  $Piliko = "";
  }
?>
</head>

<BODY>

<FORM METHOD="POST"  ACTION="<?php echo $_SERVER['PHP_SELF']; ?>" >

  <p> <u>Πράξεις με δύο αριθμούς</u>
  <br><br>
  Δώσε τον 1ο αριθμό : 
  <input type="text" size=5 name="Ar1" value=
  "<?php echo $_POST['Ar1']; ?>" >
  <br>
  Δώσε τον 2ο αριθμό : 
  <input type="text" size=5 name="Ar2" value=
  "<?php
  if (IsSet($_POST['Ar2']))
    {  
    echo $_POST['Ar2']; 
    }
  ?>" >
  
  <BR><BR>

  <INPUT TYPE="Submit" value="ΥΠΟΛΟΓΙΣΜΟΣ">
</FORM>

<?php
  echo 'Αθροισμα = ' . $Athrisma . '<br>';
  echo 'Διαφορά  = ' . $Diafora . '<br>';
  echo 'Γινόμενο = ' . $Ginomeno . '<br>';
  if (IsSet($_POST['Ar2']))
    {
	if ($Piliko == 0)
	  {
      echo 'Πηλίκο   = ' . 'Διαίρεση αδύνατη !!' . '<br>';
      }
	else
	  {
      echo 'Πηλίκο   = ' . $Piliko . '<br>';
      }
	}
  else
    { 
    echo 'Πηλίκο   = ' . '<br>';
	$_POST['Ar2'] = "";
	}
?>
<br>


</BODY>

</HTML>
