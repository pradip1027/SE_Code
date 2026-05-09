<?php
include 'db_connect.php';

$input = json_decode(file_get_contents('php://input'), true);

if (isset($input['id'], $input['enrolment_no'], $input['name'], $input['branch'], $input['sem'], $input['cgpa'])) {
    $id = intval($input['id']);
    $enrolment_no = $conn->real_escape_string($input['enrolment_no']);
    $name = $conn->real_escape_string($input['name']);
    $branch = $conn->real_escape_string($input['branch']);
    $sem = intval($input['sem']);
    $cgpa = floatval($input['cgpa']);

    $sql = "UPDATE students SET enrolment_no='$enrolment_no', name='$name', branch='$branch', sem=$sem, cgpa=$cgpa WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        echo json_encode(["status" => "success", "message" => "Record updated successfully"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Error: " . $conn->error]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Missing required fields: id, enrolment_no, name, branch, sem, or cgpa"]);
}

$conn->close();
?>