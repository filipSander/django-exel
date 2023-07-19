document.addEventListener('DOMContentLoaded', () => {
    // Анимация инпутов кнопки.
    let fields = document.querySelectorAll('.field__file');
    Array.prototype.forEach.call(fields, function (input) {
        let label = input.nextElementSibling,
        labelVal = label.querySelector('.field__file-fake').innerText;
        
        input.addEventListener('change', function (e) {
                console.log(String(event.target.id))
            label.querySelector('.fake' + String(event.target.id)).innerText = '✔️';
        });
    });

    
})