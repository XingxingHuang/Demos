You can use chrome to test and play arround the javascript.

`View > Developer > Javascript Console`, OPTION + COMMAND + J

Open [google](https://www.google.com/) homepage, open the console, practice the following and check how the website changes. 


This may not work as the home page changes everyday.

```javascript
var logo = document.querySelector('#hplogo');
setInterval(function() {
    logo.width += 5;
}, 100)
```

```javascript
alert("Hello, World!")
```


Javascript Primitive data types

``` javacript
Null.
Undefined.
Boolean.
Number.
String.
Symbol (new in ECMAScript 6)
```
