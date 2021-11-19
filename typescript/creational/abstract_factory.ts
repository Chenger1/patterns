interface AbstractFactory{
    createPhone();
    createLaptop();
}

interface AbstractPhone{
    makeCall();
}

interface AbstractLaptop{
    makeCode();
}

class CreateGoogle implements AbstractFactory{
    public createPhone() {
        return new GooglePhone();
    }

    public createLaptop() {
        return new GoogleLaptop();
    }
}

class CreateAsus implements AbstractFactory{
    public createPhone() {
        return new AsusPhone();
    }

    public createLaptop() {
        return new AsusLaptop();
    }
}

class GooglePhone implements AbstractPhone{
    public makeCall() {
        console.log('Call from Google phone');
    }
}

class GoogleLaptop implements AbstractLaptop{
    public makeCode() {
        console.log('Code from Google Laptop');
    }
}

class AsusPhone implements AbstractPhone{
    public makeCall() {
        console.log('Call from Asus phone');
    }
}

class AsusLaptop implements AbstractLaptop{
    public makeCode() {
        console.log('Code from Asus Laptop');
    }
}


function clientCode(creator: AbstractFactory){
    const phone = creator.createPhone();
    const laptop = creator.createLaptop();
    phone.makeCall();
    laptop.makeCode();
}

clientCode(new CreateGoogle());
clientCode(new CreateAsus());
