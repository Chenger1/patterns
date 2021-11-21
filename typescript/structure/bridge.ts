class Abstraction{
    protected implementation: Implementation

    constructor(implementation){
        this.implementation = implementation;
    }

    public doSomeJob(): string{
        return this.implementation.doSomeImplementationJob();
    }
}


class Implementation{
    public doSomeImplementationJob(): string{
        return 'Some Job';
    }
} 

class AnotherImplementation extends Implementation{
    constructor(){
        super();
    }
    public doSomeImplementationJob(): string {
        return 'Some another Job';
    }
}

function clientCode(){
    const implementation = new Implementation();
    const abstraction = new Abstraction(implementation);
    console.log(abstraction.doSomeJob());
    const another_implementation = new AnotherImplementation();
    const another_abstraction = new Abstraction(another_implementation);
    console.log(another_implementation.doSomeImplementationJob());
}

clientCode();

