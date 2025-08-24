function wopen() { // прикрепи к кнопке в html
    window.open("dogcheck.html", "_blank");
}
let t1 = document.getElementById("1");
let t2 = document.getElementById("2");
let t3 = document.getElementById("3");
let b1 = document.getElementById("btn")

let count = 0;

b1.hidden = true;

function talk() {
    count += 1;
    if (count == 1) {
        t1.hidden = false;
    } else if (count == 2) {
        t2.hidden = false;
    } else if (count == 3) {
        t3.hidden = false;
        b1.hidden = false;
    } else if (count > 3 && count < 10) {
        alert("Мне нечего тебе говорить. Нажми на кнопку сверху от меня и не дай ИМ меня разбудить")
        alert("А не то...")
    } else {
        alert("Мне надоело. Отправляйся на остров и дай мне поспать")
        setTimeout(wopen(), 4000)
    }
}