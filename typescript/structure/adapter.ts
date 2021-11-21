class JsonResponse{
    public returnResponse(text, status): string{
        return JSON.stringify({'text': text, 'status': status});
    }
}


class UserRequest{
    public handleRequest(args: string[]): string{
        return JSON.stringify(args);
    }
}


class Adapter extends UserRequest{
    public adaptee: JsonResponse

    constructor(adaptee: JsonResponse){
        super()
        this.adaptee = adaptee;
    }

    public handleRequest(args: string[]): string{
        const text = args[0];
        const status = args[1];
        return this.adaptee.returnResponse(text, status);
    }
}

function cliendCode(){
    const json_response = new JsonResponse();
    const user_request = new Adapter(json_response);
    console.log(user_request.handleRequest(['My Status', '200']));
}

cliendCode();
