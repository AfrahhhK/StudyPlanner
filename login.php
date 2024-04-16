<!-- index.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="icon.png">
    <title>Login Page</title>

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
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        #loginBox {
            background-color: #3d5a80;
            color: #ffff;
            padding: 20px;
            border: none;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            box-sizing: border-box;
        }

        button {
            background-color: #98c1d9;
            color: #3d5a80;
            font-size: 15px;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 15px;
        }
    </style>
</head>

<body>

    <div id="loginBox">
        <h2>Login</h2>
        <form id="loginForm">
            <input type="text" id="username" name="username" placeholder="Username" required>
            <br>
            <input type="password" id="password" name="password" placeholder="Password" required>
            <br>
            <button type="submit" onclick="validateLogin()">Login</button>
            <div class="signup">
                <div>
                    <p style="padding-top:15px;">Don't have an account? <a onclick=" signup() " id=" signup" style="
                        padding:5px;color: white;" href="signup.php">
                        Sign up</a>
                    </p>
                </div>
        </form>
    </div>

    <script>
        function validateLogin() {
            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;

            // Basic validation - Check if username and password are not empty
            if (username === '' || password === '') {
                alert('Please enter both username and password.');
                return;
            }

            // Simulate authentication (replace this with server-side validation)
            if (username === 'a' && password === '1') {
                // Redirect to another page after successful login
                window.location.href = 'main.html';
            } else {
                alert('Invalid username or password. Please try again.');
            }
        }
        function signup() {
            if (signup) {
                window.location.href = "signup.php"
            }
        }
    </script>

</body>

</html>