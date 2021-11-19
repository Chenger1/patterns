interface Builder{
    buildPartOne();
    buildPartTwo();
    buildPartThree();
    getProduct();
}

class ProductBuilder implements Builder{
    public product: Product1
    constructor(){
        this.reset()
    }

    reset(){
        this.product = new Product1();
    }

    buildPartOne() {
        this.product.parts.push('Part A');
    }
    buildPartTwo() {
        this.product.parts.push('Part B');
    }
    buildPartThree() {
        this.product.parts.push('Part C');
    }

    getProduct(){
        let product = this.product;
        this.reset();
        return product;
    }
}

class Director{
    public builder: Builder;
    constructor(builder){
        this.builder = builder;
    }

    makeBase(){
        this.builder.buildPartOne();
        this.builder.buildPartTwo();
        return this.builder.getProduct();
    }

    makeFull(){
        this.builder.buildPartOne();
        this.builder.buildPartTwo();
        this.builder.buildPartThree();
        return this.builder.getProduct();
    }
}


interface AsbtractProduct{
    parts: string[],
    showParts();
}

class Product1 implements AsbtractProduct{
    parts: string[] = [];
    showParts() {
        for(let part of this.parts){
            console.log(part);
        }
    }
}

function clientCode(){
    const builder = new ProductBuilder();
    const director = new Director(builder);
    let product = director.makeBase();
    product.showParts();
    product = director.makeFull();
    product.showParts();
}

clientCode();
