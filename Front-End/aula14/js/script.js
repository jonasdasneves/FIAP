function validar(){
    var usuario = document.getElementById("user");
    var senha = document.getElementById("pw");
    var erroUser = document.getElementById("erroUser");
    var erroSenha = document.getElementById("erroSenha")
    var erro = document.getElementById("msgErro")

    if(usuario.value == ''){
        
        erroUser.innerText = 'Campo Usuário obrigatório';
    }
    else{
        erroUser.innerText = '';
        if(senha.value == ''){
            erroSenha.innerText = 'Campo Senha obrigatório';
            senha.focus();
        }
        else{
            erroSenha.innerText = ''
            if(usuario.value == 'admin' && senha.value == '123'){
                localStorage.setItem('logado','true');
                localStorage.setItem('msgErro','0');
                window.location.href = 'perfil.html'
            }
            else{
                erro.innerText = 'Usuário e senha incorretos'
            }
        }
    }
}