// const url = "{% url "images:like" %}"; // url of our view function for request and response using AJAX
    var options = {
    method: "POST",
    headers: {"X-CSRFToken": token},
    mode: 'same-origin', // it could also be another origin it means domain
    }
    window.alert("selected like button" + document.getElementById("like").toString())
    document.getElementById("like").addEventListener('click', function (e) {
    // select all <a>'s with class like and

    //add an event to them
    window.alert("click event recieved");
    e.preventDefault(); // prevent <a> from deafault action which is opening the url in a new page
    var likeButton = this; // create a likebutton object from <a> with id 'like'
    window.alert("action" + likeButton.dataset.action.toString())

    // making the request body
    var form = new FormData(); // a form
    form.append('id', likeButton.dataset.id); // add id field to the form; get it from likeButton var we have made
    form.append('action', likeButton.dataset.action); // add action field to the form
    options['body'] = form // add the form to the body of the options which is then sent to fetch fuction

    //send httpRequest
    fetch(url, options).then(response => response.json()).then(data => {
    if (data['status'] === 'ok') {
    var previous_action = likeButton.dataset.action
    window.alert("request was successful");

    // change the text of like button and its action
    var new_action = previous_action === "like" ? "like" : "unlike";
    window.alert(new_action.toString())
    likeButton.dataset.action =likeButton.innerHTML = new_action === "like" ? "unlike" : "like";
    window.alert("like button changed")
    // updating like count
    var like_count_element = document.getElementById("total"); // get the span whihc shows amount of likes
    var total_like = parseInt(like_count_element.innerText);
    window.alert("like amount changed ")
    if (new_action === "like") {
    like_count_element.innerHTML = total_like + 1;
    } else {
    like_count_element.innerHTML = total_like - 1;
    }
    }
    }) // for then(data) and if statement
    }); // for function(e)