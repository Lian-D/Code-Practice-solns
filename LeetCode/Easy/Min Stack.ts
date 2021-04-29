class MinStack {
    minStack: Array<number>;
    stack: Array<number>;
    minTop: number;
    stackTop: number;

    constructor() {
        this.minStack = new Array<number>();
        this.stack = new Array<number>();
    }

    push(val: number): void {
        if (this.minStack.length == 0) {
            this.minStack.push(val);
            this.stack.push(val);
            this.minTop = val;
            this.stackTop = val;

        } else if(val <= this.minTop) {
            this.minStack.push(val);
            this.stack.push(val);
            this.minTop = val;
            this.stackTop = val;
        } else {
            this.stack.push(val);
            this.stackTop = val;
        }
    }

    pop(): void {
        let val:number = this.stack.pop();
        this.stackTop = this.stackTop = this.stack[this.stack.length-1];
        if (this.minTop == val) {
            this.minStack.pop();
            this.minTop = this.minStack[this.minStack.length-1];
        }
    }

    top(): number {
        return this.stackTop;
    }

    getMin(): number {
        return this.minTop;

    }
}
