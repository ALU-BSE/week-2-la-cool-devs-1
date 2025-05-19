// Input validation
document.getElementById('filter-form')?.addEventListener('submit', function(e) {
  const filterBy = document.getElementById('filter_by').value;
  const input = document.getElementById('q');
  const regex = /^[A-Za-z\s.]+$/;
  if ((filterBy === 'author' || filterBy === 'title') && input && input.value && !regex.test(input.value)) {
    alert('Only alphabetic characters and spaces are allowed.');
    input.focus();
    e.preventDefault();
  }
});

// Dark mode toggle with icon
const toggleBtn = document.getElementById('toggle-dark-mode');
const darkIcon = document.getElementById('dark-icon');
const body = document.body;

function setDarkMode(enabled) {
  if (enabled) {
    body.classList.add('dark-mode');
    localStorage.setItem('dark-mode', 'enabled');
    darkIcon.textContent = '🌑';
  } else {
    body.classList.remove('dark-mode');
    localStorage.setItem('dark-mode', 'disabled');
    darkIcon.textContent = '🌙';
  }
}

// Initialize
setDarkMode(localStorage.getItem('dark-mode') === 'enabled');

// Toggle
toggleBtn?.addEventListener('click', () => {
  const isDark = body.classList.contains('dark-mode');
  setDarkMode(!isDark);
});
