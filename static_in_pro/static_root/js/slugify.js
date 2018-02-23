const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

// replace & with '-and-'
// replace spaces and non word chars and dashes with a single dash
const slugify = (val) => {
    return val.toString().toLowerCase().trim().replace(/&/g, '-and-').replace(/[\s\W-]+/g, '-')
};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});
