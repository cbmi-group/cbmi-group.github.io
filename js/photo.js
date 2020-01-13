var OneLinks = new Array(2);
OneLinks[0] = "images/2020.jpg";
OneLinks[1] = "images/labphoto1.jpg";
OneLinks[2] = "images/labphoto2.jpg";
var id = function(el) {           
return document.getElementById(el);      
 };
c = id('photo-list');
ul = id('scroll');
var i=0;
if(c){  marquee = function() {   
    var j = i % 3;
    ul.getElementsByTagName('img')[0].src = OneLinks[j];
     i++;
}; 
  speed = 3000;
  var timer = setInterval(marquee, speed); 
}