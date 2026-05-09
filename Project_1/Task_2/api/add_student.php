<?php
include 'db_connect.php';

$input = json_decode(file_get_contents('php://input'), true);

if (isset($input['enrolment_no'], $input['name'], $input['branch'], $input['sem'], $input['cgpa'])) {
    $enrolment_no = $conn->real_escape_string($input['enrolment_no']);
    $name = $conn->real_escape_string($input['name']);
    $branch = $conn->real_escape_string($input['branch']);
    $sem = intval($input['sem']);
    $cgpa = floatval($input['cgpa']);

    $sql = "INSERT INTO students (enrolment_no, name, branch, sem, cgpa) VALUES ('$enrolment_no', '$name', '$branch', $sem, $cgpa)";

    if ($conn->query($sql) === TRUE) {
        echo json_encode(["status" => "success", "message" => "Record added successfully"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Error: " . $conn->error]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Missing required fields: enrolment_no, name, branch, sem, or cgpa"]);
}

$conn->close();
?>