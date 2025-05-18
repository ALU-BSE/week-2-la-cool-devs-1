    document.getElementById('filter-form')?.addEventListener('submit', function(e) {
      const filterBy = document.getElementById('filter_by').value;
      const input = document.getElementById('q');
      const regex = /^[A-Za-z\s\.]+$/;
      if ((filterBy === 'author' || filterBy === 'title') && input && input.value && !regex.test(input.value)) {
        alert('Only alphabetic characters and spaces are allowed.');
        input.focus();
        e.preventDefault();
      }
    });