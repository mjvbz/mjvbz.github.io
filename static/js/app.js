const image = document.querySelector('.image');
const hover = document.querySelector('.hover');
const modal = document.querySelector('.modal');
const close = document.querySelector('.close');

function show() {
     hover.classList.add('active');
     modal.classList.add('show');
}

function hide() {
     hover.classList.remove('active');
     modal.classList.remove('show');
}

image.addEventListener('click', show);
close.addEventListener('click', hide);

var chkbtn = document.getElementById("chkbtn");
const sidebar = document.getElementById('sidebar');

function toogle() {
     var chk = document.getElementById('check').checked;
     if (!chk) {
          sidebar.style.display = 'block';
     } else {
          sidebar.style.display = 'none';
     }
}

chkbtn.addEventListener('click', toogle);

const container = document.querySelector('#body');
const toggle = document.querySelector('.toggle-input');
const initialState = 'false';
toggle.checked = initialState;

toggle.addEventListener('change', function() {
  if (!toggle.checked) {
       container.className = 'light';
  }
  else {
       container.className = 'dark';
 }
});
