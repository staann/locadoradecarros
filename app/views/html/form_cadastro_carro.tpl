% rebase('app/views/html/menu.tpl',title='Cadastro de carros')

<div class="container mt-5">
    <h2 class="mb-4">Cadastre o carro:</h2>
    <form action="/processar_cadastro_carro" method="POST">

        <div class="mb-3">
            <label for="id" class="form-label">Identificacao</label>
            <input readonly type="text" class="form-control" id="id" name="id" required value={{carro.id}} >
        </div>

        <div class="mb-3">
            <label for="Marca" class="form-label">Marca</label>
            <input type="text" class="form-control" id="marca" name="marca" required value={{carro.marca}}>
        </div>
        <div class="mb-3">
            <label for="modelo" class="form-label">Modelo</label>
            <input type="text" class="form-control" id="modelo" name="modelo" required value={{carro.modelo}}>
        </div>
        <div class="mb-3">
            <label for="ano" class="form-label">Ano</label>
            <input type="number" class="form-control" id="ano" name="ano" required value={{carro.ano}}>
        </div>
        <div class="mb-3">
            <label for="categoria" class="form-label">Categoria </label>
            <input type="text" class="form-control" id="categoria" name="categoria" required value={{carro.categoria}}>
        </div>
        <div class="mb-3">
            <label for="preco_diaria" class="form-label">Preço Diária (R$)</label>
            <input type="number" class="form-control" id="preco_diaria" name="preco_diaria" step="0.01" required value={{carro.preco_por_dia}}>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="disponivel" name="disponivel" {{'checked' if carro.status else ''}} >
            <label class="form-check-label" for="disponivel">Disponível para locação</label>
        </div>
        <button type="submit" class="btn btn-primary">Cadastrar Carro</button>
    </form>
    <br>
    <a href="/carros" class="btn btn-link">Voltar para a lista de carros</a>
</div>