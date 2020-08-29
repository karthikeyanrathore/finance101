function displayName(){

  var arr = window.location.search;
  var c = arr.split('=');
  var u = c[1].split('&');
  document.getElementById("heading1").innerHTML="Welcome"+" "+u[0];
}
