class Stack {
    constructor() {
        // we store the entries to the stack in a js array
        this.stack = [];
    }

    len() {
        return (this.stack.length);
    }

    is_empty() {
        //returns true if the given stack is empty
        return (this.stack.length == 0);
    }

    push(e) {
        // Adds an element to the top of the stack
        this.stack.push(e);
    }

    top(){
        // returns but do not remove the element at the top of the stack
        // raises exception if the stack is empty

        if (this.stack.length == 0) {
            throw new Error("The stack is empty");
        }
        return this.stack[this.stack.length-1];
    }

    pop(){
        // removes and returns the element at the top of the stack
        // raises exception if the stack is empty

        if (this.stack.length == 0) {
            throw new Error("The stack is empty");
        }
        return this.stack.pop();
    }
}


s = new Stack();
console.log(s.len());
s.push(5);
console.log(s.len());
console.log(s.top());
console.log(s.pop());