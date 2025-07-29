document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("cep").addEventListener("blur", function () {
        let cep = this.value.replace(/\D/g, '');

        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(res => res.json())
                .then(data => {
                    if (!data.erro) {
                        document.getElementById('endereco').value = data.logradouro;
                        document.getElementById('bairro').value = data.bairro;
                        document.getElementById('cidade').value = data.localidade;
                        document.getElementById('uf').value = data.uf;
                    } else {
                        alert("CEP não encontrado.");
                    }
                })
                .catch(() => alert("Erro ao buscar CEP."));
        } else {
            alert("CEP inválido.");
        }
    });
});
