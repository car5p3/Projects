document.getElementById('fetch-button').addEventListener('click', fetchGitHubProfile);

function fetchGitHubProfile() {
    const username = document.getElementById('username').value;
    if (username) {
        fetch(`https://api.github.com/users/${username}`)
            .then(response => response.json())
            .then(data => {
                if (data.message === "Not Found") {
                    document.getElementById('profile-container').innerHTML = 'User not found...';
                } else {
                    const profileHTML = `
                        <h2>${data.login}</h2>
                        <img src="${data.avatar_url}" alt="Avatar" style="width: 100px; border-radius: 50%;">
                        <p>Name: ${data.name}</p>
                        <p>Followers: ${data.followers}</p>
                        <p>Following: ${data.following}</p>
                        <p>Repositories: ${data.public_repos}</p>
                    `;
                    const profileLink = document.getElementById('profile-link');
                    profileLink.href = data.html_url;
                    profileLink.textContent = 'Visit GitHub Profile';
                    profileLink.style.display = 'block';
                    document.getElementById('profile-info').innerHTML = profileHTML;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}
