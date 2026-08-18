document.querySelector('.toggleSide').addEventListener('click', () => {
    document.querySelector('main').classList.toggle('sidebar-hidden');
})
function renderPosts() {
    const posts = JSON.parse(localStorage.getItem('posts') || '[]');
    const postArea = document.querySelector('.post-area');
    postArea.innerHTML = '';

    posts.forEach(post => {
        const postEl = document.createElement('div');
        postEl.className = 'post';
        postEl.innerHTML = `
            <a class="post-title" href="">${post.title}</a>
            <p class="post-info">Posted by: ${post.author} — ${post.date}</p>
            <div class="post-content">
                <p>${post.description}</p>
            </div>
            <hr>
        `;
        postArea.appendChild(postEl);
    });
}

renderPosts();