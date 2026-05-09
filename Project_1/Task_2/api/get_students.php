<?php
include 'db_connect.php';

$sql = "SELECT * FROM students ORDER BY created_at DESC";
$result = $conn->query($sql);

$students = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $students[] = $row;
    }
}

echo json_encode($students);

$conn->close();
?>