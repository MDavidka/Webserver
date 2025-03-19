document.getElementById('login-btn').addEventListener('click', () => {
    window.location.href = '/auth/login';
});

async function fetchLeaderboard() {
    const response = await fetch('/leaderboard');
    const data = await response.json();
    const leaderboard = document.getElementById('leaderboard');
    leaderboard.innerHTML = data.top_users.map(user => `<li>${user.username}: ${user.minutes} mins</li>`).join('');
}