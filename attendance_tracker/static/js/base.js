document.getElementById('sidebarToggle').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('active');
    document.querySelector('.content').classList.toggle('active');
});
document.addEventListener('click', function(event) {
    var sidebar = document.querySelector('.sidebar');
    if (!sidebar.contains(event.target) && !event.target.matches('#sidebarToggle')) {
        sidebar.classList.remove('active');
        document.querySelector('.content').classList.remove('active');
    }
});