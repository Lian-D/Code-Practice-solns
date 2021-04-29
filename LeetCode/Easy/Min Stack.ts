class MinStack {
    minStack: Array<number>;
    stack: Array<number>;

    constructor() {
        this.minStack = new Array<number>();
        this.stack = new Array<number>();
    }

    push(val: number): void {
        if (this.minStack.length == 0) {
            this.minStack.push(val);
            this.stack.push(val);

        } else if(val <= this.minStack[this.minStack.length-1]) {
            this.minStack.push(val);
            this.stack.push(val);
            console.log("pushing min"+val);

        } else {
            this.stack.push(val);
            console.log("pushing max"+val);
        }
    }

    pop(): void {
        let val:number = this.stack.pop();
        if (this.minStack[this.minStack.length-1] == val) {
            this.minStack.pop();
        }
    }

    top(): number {
        console.log(this.minStack);
        return this.stack[this.stack.length-1];
    }

    getMin(): number {
        console.log(this.stack);
        return this.minStack[this.minStack.length-1]

    }
}