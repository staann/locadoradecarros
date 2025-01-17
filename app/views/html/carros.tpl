<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aluguel de Carros - Página Inicial</title>
    <link rel="stylesheet" href="static/css/carros.css"> <!-- Adicione um arquivo CSS para estilização -->
</head>
<header>
    <nav>
        <div class="logo" >
            <h1>AlugaCar</h1>
        </div>
        <ul class="menu">
            <li><a href="#sobre">Sobre</a></li>
            <li><a href="/carros">Veículos</a></li>
            <li><a href="#servicos">Serviços</a></li>
            <li><a href="#contato">Contato</a></li>
        </ul>
        <div class="login">
            <a href="login.html" class="botao">Entrar</a>
        </div>
    </nav>
</header>
<body>
    <div style="text-align: center;" >
        <h2>Listagem dos carros</h2>
        <table class="table" width="200px" align="center" border="1">
            <thead>
                <tr>
                    <th>Fabricante</th>
                    <th>Modelo</th>
                    <th>Ano</th>
                    <th>Categoria</th>
                    <th>Preço Diária</th>
                    <th>Disponível</th>
                </tr>
            </thead>
            <tbody>
                % for carro in carros:
                    <tr>
                        <td>{{ carro.marca }}</td>
                        <td>{{ carro.modelo }}</td>
                        <td>{{ carro.ano }}</td>
                        <td>{{ carro.categoria }}</td>
                        <td>{{ carro.preco_por_dia }}</td>
                        <td>{{'Disponivel' if carro.status else 'Indisponivel'}}</td>
                    </tr>
                % end
            </tbody>
        </table>
        <a href="/cadastrar_carro">Cadastrar novo carro</a>
    </div>
</body>
</html>
<br>