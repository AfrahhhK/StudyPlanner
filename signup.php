<?php
include 'partials/_dbconnect.php';
$showAlert = false;

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $name = $_POST["name"];
    $dob = $_POST["dob"];
    $mobile = $_POST["mobile"];
    $age = $_POST["age"];
    $gender = $_POST["gender"];
    $status = $_POST["status"];
    $course = $_POST["course"];
    $exists = false;
    if($exists == false){
        $sql = "INSERT INTO `signup` (`name`, `dob`, `mobile`, `age`, `gender`, `status`, `course`) VALUES ('$name', '$dob', '$mobile', '$age', '$gender', '$status', '$course');";
        $result = mysqli_query($conn, $sql);
        if ($result){
            $showAlert = true;
        }
    }
}
?>

<!-- signup.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="icon.png">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <title>Sign Up Page</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');

        * {

            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #add8e6;
            /* background-color: #98c1d9; */
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        #signupForm {
            background-color: #3d5a80;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
            width: 100%;
            color: white;
            font-family: "Poppins", sans-serif;
        }

        input,
        select {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            box-sizing: border-box;
        }

        button {
            background-color: #98c1d9;
            color: #3d5a80;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full viewport height */
        }
    </style>
</head>

<body>
    
    <div class="center-container">

        <div class="container">
    <!-- success alert -->
    <?php
    if ($showAlert){
        echo '<div class="row">
                <div class="col-md-12">
                    <div class="alert alert-warning alert-dismissible fade show" role="alert">
                        <strong>Success!</strong> Your account has now been created and you can login.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                </div>
            </div>';
        }
    ?>

        <!-- signup form -->
            <div id="signupForm">
                <h2>Sign Up</h2>
                <form action="signup.php" method="post">
                    <input type="text" id="name" name="name" placeholder="Full Name" required>
                    <br>
                    <input type="date" id="dob" name="dob" required>
                    <br>
                    <input type="tel" id="mobile" name="mobile" placeholder="Mobile Number" required>
                    <br>            
                    <input type="number" id="course" name="age" placeholder="Enter age" required>
                    <br>            
                    <label for="status">Gender:</label>
                    <select id="gender" name="gender">
                        <option value="working">Male</option>
                        <option value="student">Female</option>
                        <option value="both">Other</option>
                    </select>
                    <br>
                    <label for="status">Status:</label>
                    <select id="status" name="status">
                        <option value="working">Working</option>
                        <option value="student">Student</option>
                        <option value="both">Both</option>
                    </select>
                    <label for="status">Course:</label>
                    <select id="course" name="course">
                        <option value="working">Bussiness</option>
                        <option value="student">Art and Design</option>
                        <option value="both">Computer Science</option>
                        <option value="both">Law/ Legal Studies</option>
                        <option value="both">Media and Communications</option>
                        <option value="working">Other</option>
                    </select>
                    <br>
                    <button type="submit" value="Submit" onclick="submitForm(event)">Submit</button>
                </form>
            </div>
        </div>
       </div>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    <script>
        function submitForm() {
            var name = document.getElementById('name').value;
            var dob = document.getElementById('dob').value;
            var mobile = document.getElementById('mobile').value;
            var course = document.getElementById('course').value;
            var status = document.getElementById('status').value;


            // Basic validation - Check if required fields are not empty
            if (name === '' || dob === '' || mobile === '' || age === '' || gender === '' ||status === ''||course === '') {
                alert('Please fill in all the required fields.');
                return;
            }

            // Process the form data (you can send it to a server or perform further actions)
            // In this example, let's just display an alert with the collected information
            var message = `Name: ${name}\nDate of Birth: ${dob}\nMobile Number: ${mobile}\nCourse: ${course}\nStatus: ${status}`;
            alert(message);
            $.ajax({
                url: 'cred.php',
                type: 'POST',
                // data: {
                //     username: username,
                //     password: password
                // },
                success: function(response) {
                    console.log(response);
                    // Handle the response from PHP here
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    </script>

</body>

</html>