const pwEl = document.getElementById('pw');
const copyEl = document.getElementById('copy');
const lengthEl = document.getElementById('length');
const upperEl = document.getElementById('upper');
const lowerEl = document.getElementById('lower');
const numberEl = document.getElementById('number');
const symbolEl = document.getElementById('special');
const generateEl = document.getElementById('generate');

const upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const lowerLetters = 'abcdefghijklmnopqrstuvwxyz';
const numbers = '0123456789'
const symbols = '!@#$%¨&*()-_+=`´{}[]:;/.,<>'

//upperLetters[];
function upperCase() {
    return upperLetters[Math.floor(Math.random() * upperLetters.length)];
}

function lowerCase() {
    return lowerLetters[Math.floor(Math.random() * lowerLetters.length)];
}

function numberCase() {
    return numbers[Math.floor(Math.random() * numbers.length)];
}

function symbolCase() {
    return symbols[Math.floor(Math.random() * symbols.length)];
}

function gerarSenha() {
    const senha = [];

    if (upperEl.checked) {
        senha.push(upperCase());
    }
    if (lowerEl.checked) {
        senha.push(lowerCase());
    }
    if (numberEl.checked) {
        senha.push(numberCase());
    }
    if (symbolEl.checked) {
        senha.push(symbolCase());
    }

    if (pw.length === 0) return '';

    return senha[(Math.floor(Math.random() * senha.length))]

}

function criarSenha() {
    const len = lengthEl.value;
    let password = '';
    for (i = 0; i < len; i++) {
        password += gerarSenha();
    }
    pwEl.innerText = password;
}

generateEl.addEventListener('click', criarSenha);

