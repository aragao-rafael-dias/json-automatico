async function submitData() {
    const data = {
        nome: document.getElementById('nome').value,
        latitude: document.getElementById('latitude').value,
        longitude: document.getElementById('longitude').value,
        descricao: document.getElementById('descricao').value
    };

    console.log(data)

    try {
        const response = await fetch('/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        alert(result.message || result.error);
        } catch (error) {
            alert('Submissão de informações falhou. Tente novamente.');
        }
}