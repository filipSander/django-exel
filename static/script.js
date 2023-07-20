document.addEventListener('DOMContentLoaded', () => {
    // Анимация инпутов кнопки.
    let fields = document.querySelectorAll('.field__file');
    Array.prototype.forEach.call(fields, function (input) {
        let label = input.nextElementSibling,
        labelVal = label.querySelector('.field__file-fake').innerText;
        
        input.addEventListener('change', function (e) {
            label.querySelector('.fake' + String(e.target.id)).innerText = '✔️';
        });
    });

    let file_dields = document.querySelectorAll('.field__file');
    Array.prototype.forEach.call(file_dields, function (input) {
        input.addEventListener("change", handleFiles, false);
    });

    function handleFiles() {
        const [file] = this.files
        if (file) {
            const classname = "." + String(this.id)
            console.log(classname)
            console.log(file)
            document.querySelector(classname).src = URL.createObjectURL(file)
        }
    }
    
})

const sendForm = (e) => 
{
    e.preventDefault();

    const form = e.target;
    const url = form.action;
    const id = e.target.getAttribute('data-id')
    const tocken = document.querySelector('.cfrs_tocken input').value
    
    let name = document.getElementById('name-' + id).value;
    let place = document.getElementById('place-' + id).value;
    let facturer = document.getElementById('facturer-' + id).value;
    let facturer_сountry = document.getElementById('facturer_сountry-' + id).value;
    let desc = document.getElementById('desc-' + id).value;
    let image = document.getElementById('l' + id).files[0];
    
    const formData = new FormData()
    formData.append('id', id);
    formData.append('file', image);
    formData.append('name', name);
    formData.append('place', place);
    formData.append('facturer', facturer);
    formData.append('facturer_сountry', facturer_сountry);
    formData.append('descripton', desc);
    console.log(sendData(url, formData, name, tocken))
}



const sendData = async (url, data, name, tocken) => {
    const headers = new Headers({
        'X-CSRFToken': tocken,
        'csrfmiddlewaretoken': tocken,
    });
    const response = await fetch(url, {
        method: 'POST',
        body: data,
        headers
    })
    if (response.ok){
        console.log(data)
        message( name + " Запись обновленна.")
    }else{
        message(name + " Ошибка при обновлении записи.")
        throw new Error(`Ошибка, адресс ${url}, статус ${response}`)
    }
    return await response.json()
}

const message = (message) => {
    document.querySelector(".messages").innerHTML = `<div class="alert alert-warning alert-dismissible fade show" role="alert"><strong>Сообщение.</strong>  ${message}<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`
}