<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aluguel de Carros - Página Inicial</title>
    <link rel="stylesheet" href="static/css/menu.css"> <!-- Adicione um arquivo CSS para estilização -->
</head>
<body>
    <header>
        <nav>
            <div class="logo">
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

    <section class="hero">
        <div class="hero-texto">
            <h2>Alugue o carro ideal para sua viagem</h2>
            <p>Encontre conforto, economia e segurança com os melhores veículos disponíveis.</p>
            <a href="#veiculos" class="botao">Ver Carros Disponíveis</a>
        </div>
    </section>

    <section id="sobre" class="sobre">
        <div class="container">
            <h2>Sobre Nós</h2>
            <p>Somos uma empresa dedicada a oferecer o melhor serviço de aluguel de carros, com uma frota variada e atendimento de qualidade. Seu destino, nossa prioridade!</p>
        </div>
    </section>

    <section id="veiculos" class="veiculos">
        <div class="container">
            <h2>Nossos Veículos</h2>
            <div class="veiculos-grid">
                <div class="veiculo">
                    <img src="images/suv.jpg" alt="SUV">
                    <h3>SUV</h3>
                    <p>A partir de R$150/dia</p>
                </div>
                <div class="veiculo">
                    <img src="images/economico.jpg" alt="Econômico">
                    <h3>Econômico</h3>
                    <p>A partir de R$90/dia</p>
                </div>
                <div class="veiculo">
                    <img src="images/luxo.jpg" alt="Luxo">
                    <h3>Luxo</h3>
                    <p>A partir de R$300/dia</p>
                </div>
            </div>
        </div>
    </section>

    <section id="servicos" class="servicos">
        <div class="container">
            <h2>Serviços</h2>
            <ul>
                <li>Aluguel diário, semanal ou mensal</li>
                <li>Assistência 24 horas</li>
                <li>Frota revisada e higienizada</li>
                <li>Reserva online fácil e rápida</li>
            </ul>
        </div>
    </section>

    <section id="contato" class="contato">
        <div class="container">
            <h2>Entre em Contato</h2>
            <form action="submit_form.php" method="POST">
                <label for="nome">Nome:</label>
                <input type="text" id="nome" name="nome" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="mensagem">Mensagem:</label>
                <textarea id="mensagem" name="mensagem" rows="5" required></textarea>

                <button type="submit" class="botao">Enviar</button>
            </form>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 AlugaCar. Todos os direitos reservados.</p>
        </div>
    </footer>
</body>
</html>
