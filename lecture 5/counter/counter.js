/* if local storage of counter does not exist
   => set value of counter = 0
*/
if (!localStorage.getItem('counter')){
    localStorage.setItem('counter',0);
}      

/* count()
 * get the current value of counter in local storage and increment it by 1
 * update the changes to h1
 * update the changes to counter variable
 */
function count(){
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);
}

//-----EVENT LISTENER-------
document.addEventListener('DOMContentLoaded', function(){
    //when refresh the page, update information from the local storage and apply to h1
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    //event handler: set the value of button to count function
    document.querySelector('button').onclick = count;
});
           