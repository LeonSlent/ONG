const botoesFiltro = document.querySelectorAll(".btn-filtro");
botoesFiltro.addEventListener("click", (evento) =>{
    filtrarAnimais();
})

function filtrarAnimais() {
    const botaoFiltro = document.getElementById(this.id);
    const categoria = botaoFiltro.value;
    let animaisFiltrados = filtrarAnimais(categoria);
    exibirAnimais(animaisFiltrados);
}

