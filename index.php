<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planner</title>
    <link rel="stylesheet" href="style.css">

    <link rel="icon" href="icon.png" type="image/png">

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">

    <!-- Include Bootstrap JavaScript and Popper.js -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"></script>
</head>

<body>
    <!--Sidebar Navigation-->
    <header>
<!-- hamburger btn -->
        <button id="toggleButton"> <img src="bar.png"  style="height: 24px; padding: 2px;" alt=""></button>

<!-- Sidebar -->
        <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white"> 
<!-- sidebar options -->

<!--questionnaire  -->
            <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                    <a href="#" id="questionnaireLink" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
                        <i class="fas fa-tachometer-alt fa-fw me-3"></i><span>Questionnaire</span>
                    </a>
                    
<!-- to-do -->
                    <a href="toDoList.html" class="list-group-item list-group-item-action py-2 ripple"><i
                            class="fas fa-lock fa-fw me-3"></i><span>To-do list</span></a>    
<!-- time table -->
                    <a href="timeTableInputs.html" class="list-group-item list-group-item-action py-2 ripple"><i
                            class="fas fa-chart-bar fa-fw me-3"></i><span>Time table</span></a>
<!-- Calendar -->
                    <a href="https://www.google.com/" class="list-group-item list-group-item-action py-2 ripple"><i
                            class="fas fa-globe fa-fw me-3"></i><span>Calendar</span></a>
<!-- Pomodoro-->
                    <a href="pomodoro.html" class="list-group-item list-group-item-action py-2 ripple"><i
                            class="fas fa-building fa-fw me-3"></i><span>Pomodoro</span></a>
<!--Affirmations  -->
                    <a href=# class="list-group-item list-group-item-action py-2 ripple"><i
                            class="fas fa-calendar fa-fw me-3"></i><span>Affirmations</span></a>
<!-- Add time table -->
                    <a href="https://www.google.com/" class="list-group-item list-group-item-action py-2 ripple"><i
                            class="fas fa-users fa-fw me-3"></i><span>Add timetable</span></a>
                    
                </div>
            </div>            
        </nav>
      
<!--Main Navigation***********************-->
    <div class="container col-6">
        <div class="row">
            <h2>Enter details</h2>
            <form action=" " method="get">
<!-- name -->
                <div class="question" id="question1" name="name">
                    <label for="fname1">What is your name?</label><br>
                    <input type="text" id="fname1" name="fname1">
                </div>
<!-- sleep -->
                <div class="question" id="question2" name="sleep" style="display: none;">
                    <label for="sleep">How many hours do you sleep for?</label><br>
                    <input type="number" id="sleep" name="sleep">
                </div>
<!-- course -->
                <div class="question" id="question3" name="course" style="display: none;">
                    <label for="fname2">Course/ Major </label><br>
                    <div class="radio-group">
   
                        <input type="radio" id="Bussiness" name="Bussiness" value="Bussiness">
                        <label for="18-22">Bussiness</label><br>

                        <input type="radio" id="Art and Design" name="Art" value="Art and Design">
                        <label for="Art and Design">Art and Design</label><br>  
                                    
                        <input type="radio" id="Computing (CS or Computer Engineering)" name="CS" value="Computing (CS or Computer Engineering)">
                        <label for="Computing (CS or Computer Engineering)">Computing (CS or Computer Engineering)</label><br> 

                        <input type="radio" id="Law/ Legal Studes" name="Law" value="Law/ Legal Studes">
                        <label for="Law/ Legal Studes">Law/ Legal Studies</label><br>  

                        <input type="radio" id="Science and Engineering" name="Science" value="Science and Engineering">
                        <label for="Science and Engineering">Science and Engineering</label><br>  

                        <input type="radio" id="Social Sciences and Humanities" name="Socialscience" value="Social Sciences and Humanities">
                        <label for="Social Sciences and Humanities">Social Sciences and Humanities</label><br>                         

                        <input type="radio" id="Media and Communications" name="Media" value="Media and Communications">
                        <label for="Media and Communications">Media and communications</label><br> 
                    </div>

                </div>
<!-- gpa -->
                <div class="question" id="question4" style="display: none;">
                    <label for="gpa">Academic GPA</label><br>
                    <input type="text" id="sleep" name="gpa">
                </div>
<!-- attendance -->
                <div class="question" id="question5" name="attendance" style="display: none;">
                    <label for="attendance">Attendance (0 means the most attendance, the level of stage will be upgraded by every 3-4 absence, and 4 means the least attendance)</label>
                    <div class="radio-group">
                        <input type="radio" name="attendance" value="0">
                        <label for="attendance">0</label>
                        <input type="radio" name="attendance" value="1">
                        <label for="attendance"> 1</label>
                        <input type="radio" name="attendance" value="2">
                        <label for="attendance"> 2</label>
                        <input type="radio" name="attendance" value="3">
                        <label for="attendance"> 3</label>
                        <input type="radio" name="attendance" value="4">
                        <label for="attendance">4</label>   
                    </div>         
                </div>

<!--things don't matter -->
                <div class="question" id="question6" name="lastMin" style="display: none;">
                    <label for="matter">You often feel that your life is aimless, with no definite purpose</label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="matter" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="matter" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="matter" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="matter" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="matter" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>     
                    </div>      
                </div>
<!--lastMin-->
                <div class="question" id="question7" style="display: none;">
                    <label for="lastMin">You tend to leave things to the last minute?
                    </label><br>
                    <div class="radio-group">    
                        <input type="radio" id="Strongly agree" name="lastMin" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="lastMin" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="lastMin" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="lastMin" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="lastMin" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>  
                    </div>         
                </div>
<!--change aimlessly-->
                <div class="question" id="question8" style="display: none;">
                    <label for="aimlessly">You tend to change rather aimlessly from one activity to another during the day
                    </label><br>    
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="aimlessly" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="aimlessly" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="aimlessly" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="aimlessly" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="aimlessly" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>   
                    </div>        
                </div>
                </div>
<!--give up coz of friend-->
                <div class="question" id="question9" style="display: none;">
                    <label for="giveUp">You give up the things that you planning to do just because your friend says no
                    </label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="giveUp" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="giveUp" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="giveUp" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="giveUp" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="giveUp" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>  
                    </div>         
                </div>
<!--bored of day to day activities-->
                <div class="question" id="question10" style="display: none;">
                    <label for="bored">You are easy to get bored with your day-today activities.
                    </label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="bored" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="bored" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="bored" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="bored" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="bored" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>     
                    </div>      
                </div>
<!--interest changes frequently-->
                <div class="question" id="question11" style="display: none;">
                    <label for="interests">The important interests/activities in your life tend to change frequently
                    </label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="interests" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="interests" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="interests" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="interests" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="interests" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>  
                    </div>         
                </div>                
<!--trouble organizing-->
                <div class="question" id="question12" style="display: none;">
                    <label for="organizing">You never have trouble organizing the things you have to do?
                    <div class="radio-group">
                        </label><br>
                        <input type="radio" id="Strongly agree" name="organizing" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="organizing" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="organizing" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="organizing" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="organizing" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>   
                </div>        
                </div>                
<!--complete activity-->
                <div class="question" id="question13" style="display: none;">
                    <label for="complete">Once you've started an activity, you persist at it until you've completed it
                    </label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="complete" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="complete" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="complete" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="complete" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="complete" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>  
                    </div>         
                </div>                
<!--plan daily activity-->
                <div class="question" id="question14" style="display: none;">
                    <label for="plan">You will plan your activities from day to day.</label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="plan" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="plan" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="plan" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="plan" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="plan" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>    
                    </div>       
                </div>                
<!--You think you do enough with your time-->
                <div class="question" id="question15" style="display: none;">
                    <label for="enough">You think you do enough with your time.</label><br>
                        <div class="radio-group">
                            <input type="radio" id="Strongly agree" name="enough" value="Strongly agree">
                            <label for="Strongly agree">Strongly agree</label><br>

                            <input type="radio" id="Agree" name="complete" value="Agree">
                            <label for="Agree">Agree</label><br>                                               
                            <input type="radio" id="Neither Agree nor Disagree" name="enough" value="Neither Agree nor Disagree">
                            <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                            <input type="radio" id="Disagree" name="enough" value="Disagree">
                            <label for="Disagree">Disagree</label><br>   

                            <input type="radio" id="Strongly disagree" name="enough" value="Strongly disagree">
                            <label for="Strongly disagree">Strongly disagree</label><br>   
                        </div>        
                </div>                
<!--time on homework-->
                <div class="question" id="question16" style="display: none;">
                    <label for="homework">You know how much time you spend on each of the homework you do.</label><br>
                    <div class="radio-group">
                        <input type="radio" id="Strongly agree" name="homework" value="Strongly agree">
                        <label for="Strongly agree">Strongly agree</label><br>

                        <input type="radio" id="Agree" name="homework" value="Agree">
                        <label for="Agree">Agree</label><br>                                               
                        <input type="radio" id="Neither Agree nor Disagree" name="homework" value="Neither Agree nor Disagree">
                        <label for="Neither Agree nor Disagree">Neither Agree nor Disagree</label><br>  

                        <input type="radio" id="Disagree" name="homework" value="Disagree">
                        <label for="Disagree">Disagree</label><br>   

                        <input type="radio" id="Strongly disagree" name="homework" value="Strongly disagree">
                        <label for="Strongly disagree">Strongly disagree</label><br>   
                    </div>        
                </div>                


</form>
    <!-- buttons - prev, next -->
            <div class="d-flex justify-content-between">        
                <button class="btn" id="prev-button" style="float: right;">Previous</button>
                <button class="btn" id="next-button" style="float: right;">Next</button>
            </div>
        </div>
        
    </div>
    <script src="script.js"></script>
</body>

</html>

