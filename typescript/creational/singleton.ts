class Singleton{
    private static instance: Singleton;

    private constructor(){}; // Remove option to create instance via "new" constructor

    public static getInstance(): Singleton{
        if(!Singleton.instance){
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }
}

function clientCode(){
    let single1 = Singleton.getInstance();
    let single2 = Singleton.getInstance();

    if(single1 === single2){
        console.log('They are the same');
    }else{
        console.log('Wrong output');
    }
}

clientCode();
