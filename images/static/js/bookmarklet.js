const siteUrl = '//www.mysite.com:8080/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 100;
const minHeight = 100;

// load CSS
var head = document.getElementsByTagName('head')[0];  // Get HTML head element
var link = document.createElement('link'); // Create new link Element
link.rel = 'stylesheet'; // set the attributes for link element
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999);
head.appendChild(link);  // Append link element to HTML head

// load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
  <div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div>
  </div>`;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images'); //??
    // window.alert("we are lauching.....")

    // clear images found
    imagesFound.innerHTML = '';
    // display bookmarklet
    bookmarklet.style.display = 'block';

    // close event
    bookmarklet.querySelector('#close')
        .addEventListener('click', function () {
            bookmarklet.style.display = 'none'
        });
    // find images in the DOM with the minimum dimensions
    window.alert("before for each")
    images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]'); //?
    images.forEach(image => {
        if (image.naturalWidth >= minWidth
            && image.naturalHeight >= minHeight) {
            var imageFound = document.createElement('img');
            imageFound.src = image.src;
            imagesFound.append(imageFound);
            // window.alert(imageFound.src)
        }
    })

    // select image event
    imagesFound.querySelectorAll('img').forEach(image => {
        image.addEventListener('click', function (event) {
            imageSelected = event.target;
            bookmarklet.style.display = 'none'; // turn off every thing using css
            window.open(siteUrl + 'images/create/?url=' + encodeURIComponent(imageSelected.src) + '&title=' + encodeURIComponent(document.title),
                '_blank'); // open it in a new page
        })
    })
}

// launch the bookmkarklet immediately
bookmarkletLaunch();
