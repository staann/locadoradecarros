% rebase('app/views/html/menu.tpl',title='login')
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aluguel de Carros - Página Inicial</title>
    <link rel="stylesheet" href="static/css/login_page.css"> <!-- Adicione um arquivo CSS para estilização -->
</head>
<body class="body-login">
    <div class="login-container">
        <h1>Login</h1>
        <form action="/login" method="post">
            <div class="form-group">
                <label for="username">Usuário:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Senha:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="btn">Entrar</button>
        </form>
    </div>
</body>
</html>