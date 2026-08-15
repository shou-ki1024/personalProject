function sigma() {
    let test = ["sigma", "black", "rusdi"];
    for (let i = 0; i < test.length; i++) {
        setTimeout(() =>{
        document.getElementById("test").textContent = test[i];
        console.log("${test[i]}");
    }, i*1000)
    }
}
