// Tina Wong, Ray Onishi
// SoftDev1 pd7
// K29 -- Sequential Progression
// 2018-12-19

var fibonacci = function(n) {
  if(n < 2) {
    return n; // base case
  }
  else {
    return fibonacci(n-1) + fibonacci(n-2); // recursive case
  }
}

var gcd = function(a,b) {
  if(b != 0) {
    return gcd(b, a % b); // recursive case
  }
  else {
    return a; // base case
  }
}

// helper function for randomStudent() generates a list of students when a length is given
var generateList = function(length) {
  var list = []
  for(i = 0; i < length; i++) {
    list.push("Student "+i) // append to list
  }
  return list;
}

var students = generateList(5); // call function generateList() and bind the value to students variable

var randomStudent = function() {
    var index = Math.floor(Math.random() * students.length); // get random index for list
    return students[index];
}

var displayFib = function(){
  console.log(fibonacci(10));
  document.getElementById("result").innerHTML = "Fibonacci: " + fibonacci(10);
}

var displayGcd = function(){
  console.log(gcd(100,30));
  document.getElementById("result").innerHTML = "GCD: " + gcd(100,30);
}

var displayStudent = function(){
  var selected_student = randomStudent();
  console.log(selected_student);
  document.getElementById("result").innerHTML = "Selected Random Student: " + selected_student;
}

var fib = document.getElementById('fib');
fib.addEventListener("click", displayFib);

var gcd_button = document.getElementById('gcd');
gcd_button.addEventListener("click", displayGcd);

var randomStudent_button = document.getElementById('randomStudent');
randomStudent_button.addEventListener('click', displayStudent);
