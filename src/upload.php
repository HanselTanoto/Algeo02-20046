<?php
if (isset($_POST['submit'])) {
    $file = $_FILES['uploadfile'];
    $filename = $_FILES['uploadfile']['name'];
    $filetmpname = $_FILES['uploadfile']['tmp_name'];
    $filesize = $_FILES['uploadfile']['size'];
    $fileerror = $_FILES['uploadfile']['error'];
    $filetype = $_FILES['uploadfile']['type'];
}
