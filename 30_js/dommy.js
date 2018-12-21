// Ray Onishi & Maggie Zhao
// SoftDev1 pd7
// K#30 -- Sequential Progression III: Season of the Witch
// 2018-12-20


// Global variable for number of times the fibonacci button is clicked
var fibclick = 0;

var fibonacci = function(n) {
  'Find the nth Fibonacci number'
  //base case 1: the number is 0 -> return 0
	if ( n < 2 ) {
    return n;
	}
  //use recursion: find the n-1th and n-2th Fibonacci numbers and add them
	else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
};

// Creates an object filled with objects with the "li" tag
var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++) {
  // When the mouse moves over an item in the lis object, it will change the heading to what is displayed in the list item
  lis[i].addEventListener('mouseover', function() {
    changeHeading(this.innerHTML);
    });
  // When the mouse moves out of the list item, it will display "Hello World!"
  lis[i].addEventListener('mouseout', function(){
    changeHeading("Hello World!");
  });
  // When the list item is clicked, it will remove the item.
  lis[i].addEventListener('click', function(){
    removeItem(this);
  });
}

// add all EventListeners to newly added items
var addItem = function() {
  'Adds element to the existing list'

  // Finds the elment with the ID 'thelist'- the ordered list
  var list = document.getElementById("thelist");
  // Creates a new <li> element
  var newItem = document.createElement("li");
  // Set the new item's HTML value to WORD
  newItem.innerHTML = "WORD";
  // Appends the new <li> to the <ol>
  list.appendChild(newItem);

  // Adds all Event Listeners to the new Item
  newItem.addEventListener('mouseover', function() {
    changeHeading(this.innerHTML);
    });
  newItem.addEventListener('mouseout', function(){
    changeHeading("Hello World!");
  });
  newItem.addEventListener('click', function(){
    removeItem(this);
  });
};

var changeHeading = function(e) {
  'Change the heading.'
  // Get the element with the "h" id- the header at the top
  var header = document.getElementById("h");
  // Change the element's HTML value to what is given to the function
  header.innerHTML = e;
  //console.log(e);
};

var removeItem = function(e){
  'Removes the item specified.'
  e.remove();
};

//=========================================================//
// Button Event Listener for first list
var but1 = document.getElementById("b");
var result1 = b.addEventListener('click', addItem);

 //=========================================================//
var addFib = function() {
  'Adds element to the fibonacci list.'
  // Get the fibonacci list
  var list = document.getElementById("fiblist");
  // Creates a new <li> element
  var newItem = document.createElement("li");
  // Set the new item's value to fibclick'th fibonacci number
    // If you have not clicked yet, the first click will give you 0, the second click 1, the third click 1, etc.
  newItem.innerHTML = fibonacci(fibclick);
  // Adds last click to the total fibclick
  fibclick += 1;
  // Appends the new <li> to the <ol>
  list.appendChild(newItem);
}

var addFib2 = function(e) {
  'Adds element to the fibonacci list with dynamic programming.'
  //console.log(e);
  // Get the fibonacci list
  var ol = document.getElementById("fiblist");
  // From the fibonacci list, get the individual list items
  var flist = ol.getElementsByTagName("li");
  // Length of the fibonacci list
  var len = flist.length;

  // Creates a new <li> element
  var newItem = document.createElement("li");

  // If there are less than two items in the fibonacci list
  if (len <= 1) {
    // Set the new item's value to the length (0 or 1)
    newItem.innerHTML = len;
  }
  else {
    // The new item's value is the sum of the two values before it in the fibonacci list
    newItem.innerHTML = parseInt(flist[len - 1].innerHTML) + parseInt(flist[len - 2].innerHTML)
  }

  // Appends the new <li> to the <ol>
  ol.appendChild(newItem);

}
//=========================================================//

//Button Event Listener for fibonacci list
var but2 = document.getElementById("fb");
var result2 = fb.addEventListener('click', addFib2);
