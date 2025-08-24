
//анимация собаки
let dog1 = document.getElementById("ob1")
let dog2 = document.getElementById("ob2")
let dog3 = document.getElementById("ob3")
let dog4 = document.getElementById("ob4")
let dog5 = document.getElementById("ob5")

let fd = document.getElementById("field")

function dedLol() { // прикрепи к кнопке в html
    window.open("YOUDIED.html", "_blank");
}

let kraken = document.getElementById("kraken")

const lenght = 1300

dog1.onclick = move(dog1, 5)
dog2.onclick = move(dog2, 10)
dog3.onclick = move(dog3, 15)
dog4.onclick = move(dog4, 6)
dog5.onclick = move(dog5, 9)

function move(obj, slowness) {

    let start = Date.now(); // запомнить время начала

    let timer = setInterval(function () {
        // сколько времени прошло с начала анимации?
        let timePassed = Date.now() - start;

        if (timePassed >= 18000) {
            clearInterval(timer); // закончить анимацию через 2 секунды
            return;
        }

        // отрисовать анимацию на момент timePassed, прошедший с начала анимации
        draw(timePassed);
        obj.onclick = doubleClick;


    }, 20);
    // в то время как timePassed идёт от 0 до 2000
    // left изменяет значение от 0px до 400px
    function draw(timePassed) {
        obj.style.marginLeft = timePassed / slowness + 'px';
    }

    function doubleClick() {
        start = 0
        move(obj, slowness)
    }
}

function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return left = rect.left + window.scrollX

}

function check() {
    if (getOffset(dog1) + 120 >= lenght || getOffset(dog2) >= lenght || getOffset(dog3) >= lenght || getOffset(dog4) >= lenght || getOffset(dog5) >= lenght) {
        dedLol()
        alert("ой-ой")
    }
}
setInterval(check, 999999999999)