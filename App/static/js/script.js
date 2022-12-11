// Time running at real time (dynamic)
setInterval(() => {
    const date = new Date();
    const clock = document.getElementById('clock');
    clock.innerHTML = date.toLocaleTimeString();
}, 1000);