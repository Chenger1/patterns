abstract class Creator{
    public abstract createProduct(): Product;

    public makeCall(){
        const product = this.createProduct();
        return product.call();
    }
}


class CreateSmartphone extends Creator{
    public createProduct(): Product {
        return new Smartphone();
    }
}


class CreateLaptop extends Creator{
    public createProduct(): Product {
        return new Laptop();
    }
}


interface Product{
    call();
}


class Smartphone implements Product{
    public call() {
        console.log('Call from phone');
    }
}

class Laptop implements Product{
    public call() {
        console.log('Call from laptop (Google Meet)');
    }
}

function clientCode(creator: Creator){
    creator.makeCall();
}

clientCode(new CreateSmartphone());
clientCode(new CreateLaptop());
