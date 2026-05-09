$(document).ready(function () {
    loadStudents();

    // Handle form submission
    $('#student-form').on('submit', function (e) {
        e.preventDefault();

        const id = $('#student-id').val();
        const studentData = {
            enrolment_no: $('#enrolment_no').val(),
            name: $('#name').val(),
            branch: $('#branch').val(),
            sem: $('#sem').val(),
            cgpa: $('#cgpa').val()
        };

        if (id) {
            // Update existing student
            studentData.id = id;
            updateStudent(studentData);
        } else {
            // Add new student
            addStudent(studentData);
        }
    });

    // Handle Cancel button
    $('#cancel-btn').on('click', function () {
        resetForm();
    });

    // Handle Edit button
    $(document).on('click', '.btn-edit', function () {
        const student = $(this).data('student');
        $('#student-id').val(student.id);
        $('#enrolment_no').val(student.enrolment_no);
        $('#name').val(student.name);
        $('#branch').val(student.branch);
        $('#sem').val(student.sem);
        $('#cgpa').val(student.cgpa);

        $('#submit-btn').text('Update Student');
        $('#cancel-btn').show();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Handle Delete button
    $(document).on('click', '.btn-delete', function () {
        const id = $(this).data('id');
        if (confirm('Are you sure you want to delete this record?')) {
            deleteStudent(id);
        }
    });

    function loadStudents() {
        $.ajax({
            url: 'api/get_students.php',
            dataType: 'json',
            success: function (data) {
                const tbody = $('#student-table tbody');
                tbody.empty();

                if (!Array.isArray(data) || data.length === 0) {
                    tbody.append('<tr><td colspan="6" style="text-align:center;">No records found</td></tr>');
                    return;
                }

                data.forEach(student => {
                    const row = `
                        <tr>
                            <td>${student.enrolment_no}</td>
                            <td>${student.name}</td>
                            <td>${student.branch}</td>
                            <td>${student.sem}</td>
                            <td>${student.cgpa}</td>
                            <td>
                                <button class="btn btn-small btn-edit" data-student='${JSON.stringify(student)}'>Edit</button>
                                <button class="btn btn-small btn-delete" data-id="${student.id}">Delete</button>
                            </td>
                        </tr>
                    `;
                    tbody.append(row);
                });
            },
            error: function () {
                alert('Error loading student records.');
            }
        });
    }

    function addStudent(data) {
        $.ajax({
            url: 'api/add_student.php',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            dataType: 'json',
            success: function (response) {
                if (response.status === 'success') {
                    alert(response.message);
                    resetForm();
                    loadStudents();
                } else {
                    alert('Error: ' + (response.message || response.error || 'Unknown error occurred'));
                }
            },
            error: function (xhr) {
                let errorMsg = 'Error adding student.';
                if (xhr.responseJSON && xhr.responseJSON.message) {
                    errorMsg = xhr.responseJSON.message;
                }
                alert(errorMsg);
            }
        });
    }

    function updateStudent(data) {
        $.ajax({
            url: 'api/update_student.php',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            dataType: 'json',
            success: function (response) {
                if (response.status === 'success') {
                    alert(response.message);
                    resetForm();
                    loadStudents();
                } else {
                    alert('Error: ' + (response.message || response.error || 'Unknown error occurred'));
                }
            },
            error: function (xhr) {
                let errorMsg = 'Error updating student.';
                if (xhr.responseJSON && xhr.responseJSON.message) {
                    errorMsg = xhr.responseJSON.message;
                }
                alert(errorMsg);
            }
        });
    }

    function deleteStudent(id) {
        $.ajax({
            url: 'api/delete_student.php',
            type: 'POST',
            data: JSON.stringify({ id: id }),
            contentType: 'application/json',
            dataType: 'json',
            success: function (response) {
                if (response.status === 'success') {
                    alert(response.message);
                    loadStudents();
                } else {
                    alert('Error: ' + (response.message || response.error || 'Unknown error occurred'));
                }
            },
            error: function (xhr) {
                let errorMsg = 'Error deleting student.';
                if (xhr.responseJSON && xhr.responseJSON.message) {
                    errorMsg = xhr.responseJSON.message;
                }
                alert(errorMsg);
            }
        });
    }

    function resetForm() {
        $('#student-id').val('');
        $('#student-form')[0].reset();
        $('#submit-btn').text('Add Student');
        $('#cancel-btn').hide();
    }
});
