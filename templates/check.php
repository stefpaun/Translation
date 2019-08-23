< ?php
if (isset($_GET["count"])) {
    $sub = $_GET["count"];

    if (isset($sub["count"])) {
        
		header("Location: {% url 'count' %}");
    } elseif (isset($sub["about"])) {
        // header("Location: {% url 'about' %}");
    }
}
?>