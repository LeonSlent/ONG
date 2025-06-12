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

function mostrarSecao(id) {
  const secoes = ['secao-dados', 'secao-tarefas', 'secao-cadastros'];
  secoes.forEach(secao => {
    document.getElementById(secao).style.display = (secao === id) ? 'block' : 'none';
  });
s
  document.querySelectorAll('.nav .btn').forEach(btn => {
    if (btn.textContent === id.split('-')[1].toUpperCase()) {
      btn.classList.add('ativo');
    } else {
      btn.classList.remove('ativo');
    }
  });
}
