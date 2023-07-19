document.addEventListener('DOMContentLoaded', () => {
    // Анимация инпутов кнопки.
    let fields = document.querySelectorAll('.field__file');
    Array.prototype.forEach.call(fields, function (input) {
        let label = input.nextElementSibling,
        labelVal = label.querySelector('.field__file-fake').innerText;
        
        input.addEventListener('change', function (e) {
                console.log(String(e.target.id))
            label.querySelector('.fake' + String(e.target.id)).innerText = '✔️';
        });
    });

    
})

function sendForm(e)
{
    e.preventDefault();

    const form = e.target;
    const url = form.action;
    const id = e.target.getAttribute('data-id')
    const tocken = document.querySelector('.cfrs_tocken input').value
    console.log(tocken)
    console.log(id)
    
    let name = document.getElementById('name-' + id).value;
    let place = document.getElementById('place-' + id).value;
    let facturer = document.getElementById('facturer-' + id).value;
    let facturer_сountry = document.getElementById('facturer_сountry-' + id).value;
    let desc = document.getElementById('desc-' + id).value;
    
    sendAjax(url,id,name,place,facturer,facturer_сountry,desc, tocken);
}

function sendAjax(url,id,name,place,facturer,facturer_сountry,desc,tocken)
{
    let req = createRequest();
    alert(req);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            if(req.status == 200) alert('Отправка формы выполнена');
        }
    }   
    url = url+'?id='+id+'&name='+name+'&place='+place+'&facturer='+facturer+'&facturer_сountry='+facturer_сountry+'&descripton='+desc
    console.log(url)
    req.open('POST',url,true);
    req.setRequestHeader("csrftoken", tocken)
    req.send(null);
}

function createRequest()
{
    var Request = false;
    if (window.XMLHttpRequest)
        Request = new XMLHttpRequest();
    else if (window.ActiveXObject)
    {
        try
        {
            Request = new ActiveXObject('Microsoft.XMLHTTP');
        }
        catch (CatchException)
        {
            Request = new ActiveXObject('Msxml2.XMLHTTP');
        }
    }

    if (!Request)
        alert('Невозможно создать XMLHttpRequest');

    return Request;
}