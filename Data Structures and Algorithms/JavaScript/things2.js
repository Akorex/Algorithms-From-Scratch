// continues from things

// Promise

let fifteen = Promise.resolve(1);
fifteen.then(value => console.log(`Got ${value}`));

const promise = new Promise((resolve, reject) => {
    // do something asynchronous here
    // if operation is successful, we call the resolve method
    // if operation is unsuccessful, we call the reject method
});

let myPromise = new Promise(() => {
    console.log("This is really weird");
})


function getWeather() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Sunny");
        }, 100);
    })
}


function onSuccess(data) {
    console.log(`Success: ${data}`);
}

function onError(error) {
    console.log(`error: ${error}`);
}


getWeather().then(onSuccess, onError);

// polymorphism

function filter(array, f) {
    let result = []
    for (let i = 0; i < array.length ; i++) {
        let item = array[i]
        if (f(item)) {
            result.push(item)
        }
    }

    return result;
}

console.log(filter([1, 2, 3, 4], _ => _ < 3))

