<?php
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";  
  
function xor_encrypt_old($in) {  
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
    $text = $in;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
echo xor_encrypt_old(base64_decode($cookie));
echo "\n"; 
  
$data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");  
  
function xor_encrypt_new($in) {  
    $key = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq';  
    $text = $in;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
echo base64_encode(xor_encrypt_new(json_encode($data))); 

passthru('ls -la')
?>  
