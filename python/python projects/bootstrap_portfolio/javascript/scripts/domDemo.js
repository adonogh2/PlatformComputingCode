console.log(document);
console.log(document.URL);
console.log(document.inputEncoding);

function afterLoading() {
    let list1 = document.getElementsByTagName("li");
    console.log(list1 + "length of list1 is" + list1.length)

    for(let i=0;i<list1.length;i++) {
        console.log(list1[i].innerHTML);
        console.log(list1[i].textContent)
    }

    let tdNode = document.getElementById("checkingBalance");
    tdNode.textContent = "CHANGED!";   //this is important for the hw!!!!!!!

    const text = document.createTextNode("Text added to bottom of page.");
    const p = document.createElement("p");
    p.appendChild(text)

    const divEnd = document.getElementById("end");
    divEnd.appendChild(p);
}

function depositChecking() {
    let tdNode = document.getElementById("checkingBalance");
    let checking = parseInt(tdNode.textContent, 10);
    checking += 100;
    tdNode.textContent = checking;
}

function depositSavings() {
    let tdNode = document.getElementById("savingsBalance");
    let savings = parseInt(tdNode.textContent, 10);
    savings += 100;
    tdNode.textContent = savings;
    if (savings >= 100) {
        let tdNode2 = document.getElementById("bankAccount");
        tdNode2.textContent = "Bank Account";
    }
}

function emptySavings() {
    let tdNode = document.getElementById("savingsBalance");
    let savings = parseInt(tdNode.textContent, 10);
    savings = 0; //-= savings
    tdNode.textContent = savings;
    let tdNode1 = document.getElementById("bankAccount");
    tdNode1.textContent = "Alert: Savings Empty";
    

}