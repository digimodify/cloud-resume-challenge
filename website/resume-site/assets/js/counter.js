const counter = document.querySelector(".visits");

async function updateCounter() {
    let response = await fetch("https://h7fsqmvotxduazvf4ghmbka6y40igcjx.lambda-url.us-east-1.on.aws/");
    let data = await response.json();
    counter.innerHTML = `${data.counter}`; // Assuming data contains a "counter" key
}

updateCounter();
