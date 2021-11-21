interface Subject{
    operation();
}

class SomeSubject implements Subject{
    operation() {
        console.log('Operation from subject');
    }
}

class ProxyObj implements Subject{
    private subject: SomeSubject;

    constructor(subject: SomeSubject){
        this.subject = subject;
    }

    operation() {
        this.checkAccess();
        this.log();
        this.subject.operation();
    }

    checkAccess(){
        console.log('Proxy checks access');
    }

    log(){
        console.log('Proxy logs');
    }
}

function clientCode(subject: Subject){
    subject.operation();
}


const subject = new SomeSubject();
clientCode(subject);
console.log('-------');
const proxy = new ProxyObj(subject);
clientCode(proxy);

