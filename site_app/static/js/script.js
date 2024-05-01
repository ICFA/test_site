function change_theme(){
    document.body.classList.toggle('dark-theme')
}

function change_text_size(){
    document.body.classList.toggle('grand-size')
}

function change_position(){
    document.body.classList.toggle('text-align-center')
}

function calculation(){
    var list = document.querySelectorAll('#tala');
    var v = [];
    for (let i = 0; i < list.length; i++) {
        v.push(parseFloat(list[i].textContent.split(": ")[1].replace("%", "")));
      }
    var avg = v.reduce( ( p, c ) => p + c, 0 ) / v.length;
    var result = [v.min(), avg.toFixed(1), v.max()];
    document.getElementById("demonstrate").innerHTML = result.join(" / ");
}

Array.prototype.min = function() {
    return Math.min.apply(null, this);
};

Array.prototype.max = function() {
    return Math.max.apply(null, this);
};