The HTML DOM Tree of Objects
![](pic_htmltree.gif)
When a web page is loaded, the browser creates a Document Object Model of the page. [w3schools](https://www.w3schools.com/js/js_htmldom.asp)

a simple example to change the website with javascript. You change the head `h1` with color "pink".

```javascript
var h1 = document.querySelector("h1");
h1.style.color = "pink";
```

Here is another example, but use a function instead.

``` javascript
var body = document.querySelector("body"); //SELECTvar isBlue = false;setInterval(
function(){ //MANIPULATE 
	if (isBlue) {		body.style.background = "white"; 
	} else {		body.style.background = "#3498db"; 
	}	isBlue = !isBlue; 
}, 1000);
```
Try the following
```javascript
document.URL;
document.head;
document.body;
document.links;
```