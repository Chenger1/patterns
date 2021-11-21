class AmountManager{
    multiply(salary: number): number{
        return salary * 4;
    }
}

class User{
    public username: string;
    
    constructor(username: string){
        this.username = username;
    }
}

class UserManager{
    protected users: {'user': User, 'salary': number}[] = [];

    public addUser(user: User, salary: number){
        this.users.push({'user': user, 'salary': salary});
    }

    public reportUsers(){
        for(let user of this.users){
            console.log(`User: ${user['user'].username} with ${user.salary}`);
        }
    }

    public getUsers(): string{
        let result = '';
        for(let item of this.users){
            result += `User: ${item.user.username} with salary: ${item.salary}\n`;
        }
        return result;
    }
}

class Facade{
    protected amountManager: AmountManager;
    protected userManager: UserManager;

    constructor(amountManager: AmountManager = null, userManager: UserManager = null){
        this.amountManager = amountManager || new AmountManager();
        this.userManager = userManager || new UserManager();
    }

    public addNewUser(user: User, salary: number){
        this.userManager.addUser(user, this.amountManager.multiply(salary));
    }

    public getUsers(): string{
        return this.userManager.getUsers();
    }
}

function clideCode(){
    const amount_manager = new AmountManager();
    const facade = new Facade(amount_manager);
    const user = new User('John');
    const user2 = new User('John2');
    facade.addNewUser(user, 100);
    facade.addNewUser(user2, 150);
    console.log(facade.getUsers());
}

clideCode();
