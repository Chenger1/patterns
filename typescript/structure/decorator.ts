class User{
    public username: string;
    public is_staff: boolean;

    constructor(username, is_staff){
        this.username = username;
        this.is_staff = is_staff;
    }
}

class DB{
    public data: number[] = [1,2,3,4,5];

    public makeQuery(callback: (data)=>string): string{
        return callback(this.data);
    }
}


interface DecaratorInterface{
    makeQuery(callback: (data)=>string): string;
}

class Decorator implements DecaratorInterface{
    protected decorated: DB
    protected user: User

    constructor(decorated: DB, user: User){
        this.decorated = decorated;
        this.user = user;
    }

    public makeQuery(callback: (data)=>string): string{
        if(this.user.is_staff){
            return callback(this.decorated.data);
        }else{
            return `This user:${this.user.username} does not have access`;
        }
    }
}


function clideCode(){
    const db = new DB();
    const admin = new User('Admin', true);
    const decorator = new Decorator(db, admin);
    console.log(decorator.makeQuery((data) => {return data.join(':')}));

    const user = new User('John', false);
    const new_decorator = new Decorator(db, user);
    console.log(new_decorator.makeQuery((data) => {return data.join(':')}));

}

clideCode();
