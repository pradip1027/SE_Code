<?php
header('Content-Type: application/json');

$host = "localhost";
$username = "root";
$password = "Pradip@1211";
$dbname = "student_management";

// Create connection
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die(json_encode(["status" => "error", "message" => "Connection failed: " . $conn->connect_error]));
}
?>