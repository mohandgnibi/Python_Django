// Check if there is already a value in local storage.
if (!localStorage.getItem('counter')) {

    // If not, set the value of counter to 0 in local storage.
    localStorage.setItem('counter', 0);
}

function count() {
    // Retrieve the current value of the counter from local storage.
    let counter = localStorage.getItem('counter');

    // Update the counter.
    counter++;
    document.querySelector('h1').innerHTML = counter;

    // Store the updated counter in local storage.
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() {
    // Set heading to the value of the counter in local storage.
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
});
