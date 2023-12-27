fetch('http://127.0.0.1:5000/Scientist', {
    method: "get"
})

.then(response => response.json())
    .then(res => {
        console.log('response', res);

    const data = document.getElementById('data');
    data.innerHTML = JSON.stringify(res);
    })
    .catch(error => {
   console.error('Error', error);
     });