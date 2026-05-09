<?php
include 'db_connect.php';

$input = json_decode(file_get_contents('php://input'), true);

if (isset($input['id'])) {
    $id = intval($input['id']);
    $sql = "DELETE FROM students WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        echo json_encode(["status" => "success", "message" => "Record deleted successfully"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Error: " . $conn->error]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Missing required student ID"]);
}

$conn->close();
?>