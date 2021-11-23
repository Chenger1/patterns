interface Handler{
    setNext(handler: Handler): Handler;
    handle(request: string): string;
}


abstract class AbstractHandler implements Handler{
    private nextHandler: Handler;
    
    public setNext(handler: Handler): Handler {
        this.nextHandler = handler;
        return handler;
    }
    handle(request: string): string {
        if(this.nextHandler){
            return this.nextHandler.handle(request);
        }
        return null;
    }
}

class FirstHandler extends AbstractHandler{
    public handle(request: string): string {
        if(request === 'first'){
            return 'First Handler';
        }
        return super.handle(request);
    }
} 

class SecondHandler extends AbstractHandler{
    public handle(request: string): string {
        if(request === 'second'){
            return 'Second Handler';
        }
        return super.handle(request);
    }
} 


function clientCode(handler: Handler){
    const words = ['first', 'second', 'third'];

    for(let word of words){
        console.log(handler.handle(word));
    }
}

const first = new FirstHandler();
const second = new SecondHandler();

first.setNext(second);

clientCode(first);
